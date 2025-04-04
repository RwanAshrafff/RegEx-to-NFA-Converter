from parser.infix_to_postfix import insert_concat_operators, infix_to_postfix
from nfa.Thompson_Converter import compile
from nfa_to_dfa.DFA_Converter import nfa_to_dfa
from visualizer.draw_nfa import draw_nfa
from visualizer.draw_dfa import draw_dfa

if __name__ == "__main__":
    try:
        regex = input("Enter a regex expression: ")

        prepared = insert_concat_operators(regex)
        postfix = infix_to_postfix(prepared)

        print("\nPrepared Infix (with . inserted):", prepared)
        print("Postfix Expression:", postfix)

        # Build NFA
        result_nfa = compile(postfix)
        draw_nfa(result_nfa)
        print("\n✅ NFA built successfully.")
        
        # Convert to DFA
        result_dfa = nfa_to_dfa(result_nfa)
        draw_dfa(result_dfa)
        print("✅ DFA built successfully.")
        
    except ValueError as ve:
        print("❌ Error:", str(ve))
        exit()
