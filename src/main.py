from parser.infix_to_postfix import insert_concat_operators, infix_to_postfix
from nfa.Thompson_Converter import compile
from nfa_to_dfa.DFA_Converter import nfa_to_dfa
from visualizer.draw_nfa import draw_nfa
from visualizer.draw_dfa import draw_dfa
import re

# Helper: sanitize regex for use as filename
def sanitize_filename(regex):
    return re.sub(r'\W+', '_', regex)

if __name__ == "__main__":
    try:
        regex = input("Enter a regex expression: ")

        prepared = insert_concat_operators(regex)
        postfix = infix_to_postfix(prepared)

        print("\nPrepared Infix (with . inserted):", prepared)
        print("Postfix Expression:", postfix)

        # Generate safe name for graph files
        safe_name = sanitize_filename(regex)

        # Build NFA and visualize
        result_nfa = compile(postfix)
        draw_nfa(result_nfa, filename=f"nfa_{safe_name}")
        print("\n✅ NFA built and saved as 'nfa_" + safe_name + ".png'")

        # 🔁 Convert to DFA and visualize
        result_dfa = nfa_to_dfa(result_nfa)
        draw_dfa(result_dfa, filename=f"dfa_{safe_name}")
        print("✅ DFA built and saved as 'dfa_" + safe_name + ".png'")

    except ValueError as ve:
        print("❌ Error:", str(ve))
        exit()
