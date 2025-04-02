from parser.infix_to_postfix import insert_concat_operators, infix_to_postfix
from nfa.Thompson_Converter import compile

if __name__ == "__main__":
    try:
        regex = input("Enter a regex expression: ")

        prepared = insert_concat_operators(regex)
        postfix = infix_to_postfix(prepared)

        print("\nPrepared Infix (with . inserted):", prepared)
        print("Postfix Expression:", postfix)

        result_nfa = compile(postfix)
        print("\n✅ NFA built successfully.")
        
    except ValueError as ve:
        print("❌ Error:", str(ve))
        exit()
