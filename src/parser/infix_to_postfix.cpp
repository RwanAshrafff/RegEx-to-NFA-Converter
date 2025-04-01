#include <bits/stdc++.h>
#define el "\n"
#define Hossiny ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);

using namespace std;

// precedence levels : * > . > |
int precedence(char c) {
    if (c == '*') return 3;
    if (c == '.') return 2; 
    if (c == '|') return 1;
    return 0;
}

string insertConcatOperators(const string& regex) {
    string result;
    for (size_t i = 0; i < regex.length(); ++i) {
        char curr = regex[i];
        result += curr;

        if (i + 1 < regex.length()) {
            char next = regex[i + 1];

            bool currIsToken = isalnum(curr) || curr == '*' || curr == ')';
            bool nextIsToken = isalnum(next) || next == '(';

            if (currIsToken && nextIsToken) {
                result += '.';
            }
        }
    }
    return result;
}


string infixToPostfix(string expr) {
    stack<char> opStack;
    string postfix;

    // Replace '+' with '|' for union
    for (char& c : expr) {
        if (c == '+') c = '|';
    }

    for (size_t i = 0; i < expr.length(); ++i) {
        char c = expr[i];
        if (c == ' ') continue;

        if (isalnum(c)) {
            postfix += c;
            postfix += ' ';
        }
        else if (c == '(') {
            opStack.push(c);
        }
        else if (c == ')') {
            while (!opStack.empty() && opStack.top() != '(') {
                postfix += opStack.top();
                postfix += ' ';
                opStack.pop();
            }
            if (!opStack.empty()) opStack.pop(); // remove '('
        }
        else {
            while (!opStack.empty() && precedence(c) <= precedence(opStack.top())) {
                postfix += opStack.top();
                postfix += ' ';
                opStack.pop();
            }
            opStack.push(c);
        }
    }

    while (!opStack.empty()) {
        postfix += opStack.top();
        postfix += ' ';
        opStack.pop();
    }

    return postfix;
}


int main() {
    Hossiny

    string input;
    cout << "Enter a regex expression: ";
    getline(cin, input);

    string prepared = insertConcatOperators(input);
    string postfix = infixToPostfix(prepared);

    cout << "\nPrepared Infix (with . inserted): " << prepared << el;
    cout << "Postfix Expression: " << postfix << el;

    return 0;
}
