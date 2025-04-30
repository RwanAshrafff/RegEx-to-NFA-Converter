from flask import Flask, render_template, request, jsonify, send_from_directory
from parser.infix_to_postfix import insert_concat_operators, infix_to_postfix
from nfa.Thompson_Converter import compile, state, nfa
from nfa_to_dfa.DFA_Converter import nfa_to_dfa
from visualizer.draw_nfa import draw_nfa
from visualizer.draw_dfa import draw_dfa
import os
import re
from collections import defaultdict

app = Flask(__name__,
            template_folder='visualizer/templates',
            static_folder='visualizer/static')
app.config['UPLOAD_FOLDER'] = 'visualizer/static/graphs'

def sanitize_filename(regex):
    return re.sub(r'\W+', '_', regex)

def get_state_id(state, state_id_map, state_counter):
    if state not in state_id_map:
        state_id_map[state] = f"q{state_counter[0]}"
        state_counter[0] += 1
    return state_id_map[state]

def extract_transitions(nfa):
    transitions = []
    state_id_map = {}
    state_counter = [0]
    visited = set()
    stack = [nfa.initial]

    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)

        src_id = get_state_id(current, state_id_map, state_counter)

        if current.edge1:
            label = current.label if current.label else 'ε'
            dest_id = get_state_id(current.edge1, state_id_map, state_counter)
            transitions.append((src_id, label, dest_id))
            stack.append(current.edge1)

        if current.edge2:
            dest_id = get_state_id(current.edge2, state_id_map, state_counter)
            transitions.append((src_id, 'ε', dest_id))
            stack.append(current.edge2)

    return transitions, state_id_map

def generate_nfa_description(nfa):
    transitions, state_id_map = extract_transitions(nfa)
    initial_id = state_id_map[nfa.initial]
    accept_id = state_id_map[nfa.accept]
    
    description = {
        'initial': initial_id,
        'accept': accept_id,
        'transitions': []
    }
    
    for src, label, dest in transitions:
        description['transitions'].append({
            'source': src,
            'label': label,
            'target': dest,
            'is_final': dest == accept_id
        })
    
    return description

def generate_transition_table(nfa):
    transitions, state_id_map = extract_transitions(nfa)
    accept_id = state_id_map[nfa.accept]
    
    transition_map = defaultdict(list)
    for src, label, dest in transitions:
        transition_map[(src, label)].append(dest)
    
    table_data = []
    for (src, label), dests in sorted(transition_map.items()):
        table_data.append({
            'state': src,
            'symbol': label,
            'next_states': [{'id': d, 'is_final': d == accept_id} for d in dests]
        })
    
    return table_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        data = request.get_json()
        regex = data['regex'].replace(' ', '')
        
        prepared = insert_concat_operators(regex)
        postfix = infix_to_postfix(prepared)
        
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        safe_name = sanitize_filename(regex)
        
        result_nfa = compile(postfix)
        nfa_filename = f"nfa_{safe_name}"
        draw_nfa(result_nfa, filename=f"{app.config['UPLOAD_FOLDER']}/{nfa_filename}")
        
        result_dfa = nfa_to_dfa(result_nfa)
        dfa_filename = f"dfa_{safe_name}"
        draw_dfa(result_dfa, filename=f"{app.config['UPLOAD_FOLDER']}/{dfa_filename}")
        
        return jsonify({
            'success': True,
            'regex': regex,
            'prepared': prepared,
            'postfix': postfix,
            'nfa_image': f"{nfa_filename}.png",
            'dfa_image': f"{dfa_filename}.png",
            'nfa_description': generate_nfa_description(result_nfa),
            'transition_table': generate_transition_table(result_nfa)
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/graphs/<filename>')
def serve_graph(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    import os

    os.makedirs('visualizer/static/graphs', exist_ok=True)
    os.makedirs('visualizer/static/css', exist_ok=True)
    os.makedirs('visualizer/static/js', exist_ok=True)

    port = int(os.environ.get("PORT", 5000))

    app.run(debug=False, host='0.0.0.0', port=port)
