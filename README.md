# RegEx-to-NFA-Converter
A web-based tool that parses a regex and visualizes its equivalent NFA.
## Project Structure
regex-to-nfa-converter/
│
├── 📁 src/                  # Source code
│   ├── parser/             # Code for infix → postfix
│   ├── nfa/                # Thompson's construction code
│   ├── ui/                 # HTML, CSS, JS frontend
│   └── main.js             # Entry point or integration logic
│
├── 📁 public/              # Static assets (optional)
│   └── nfa_examples.json   # Sample regex and expected outputs
│
├── README.md               # Project description + instructions
├── .gitignore              # Files to ignore in version control
└── LICENSE                 # Open-source license if needed
