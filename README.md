# 🎯 RegEx-to-NFA-Converter (Python Version)

A powerful tool that **parses regular expressions (regex)** and visualizes their equivalent **Non-deterministic Finite Automata (NFA)** using **Thompson’s Construction**, and then optionally converts and displays the equivalent **Deterministic Finite Automata (DFA)** — all in **Python**.

---

## 📁 Project Directory Structure

```
REGEX-TO-NFA-CONVERTER/
│
├── public/
│   └── nfa_examples.json                # (Optional) Sample regex test cases
│
├── src/
│   ├── parser/                          # Infix ➤ Postfix parser
│   │   ├── __init__.py
│   │   └── infix_to_postfix.py
│   │
│   ├── nfa/                             # Thompson NFA builder
│   │   ├── __init__.py
│   │   └── Thompson_Converter.py
│   │
│   ├── nfa_to_dfa/                      # DFA converter from NFA
│   │   ├── __init__.py
│   │   └── DFA_Converter.py
│   │
│   ├── visualizer/                      # Visual rendering using Graphviz
│   │   ├── draw_nfa.py
│   │   └── draw_dfa.py
│
├── main.py                              # Entry point (regex ➤ NFA ➤ DFA ➤ visualization)
├── nfa_graph/                           # Folder auto-created to save graphs
├── LICENSE
├── image.png                            # Optional project diagram
└── README.md
```

---

## 🔄 What This Project Does

### ✅ Complete Regex Processing Pipeline:
1. Input a valid regex (ex: `a(b|c)*`)
2. ➤ Convert **infix ➤ postfix** using Shunting Yard Algorithm
3. ➤ Generate an NFA using **Thompson’s Construction**
4. ➤ Convert NFA ➤ DFA (Subset Construction)
5. ➤ Visualize both NFA & DFA using **Graphviz**
6. ➤ Automatically save PNGs with filenames based on regex

---

## 🧠 Regex Parsing

📄 `parser/infix_to_postfix.py`

- Automatically adds concatenation (`.`)
- Validates characters: `a-z, A-Z, 0-9, |, *, +, ?, ., (, )`
- Handles operator precedence:
  - `*`, `+`, `?` → highest
  - `.` → middle
  - `|` → lowest

---

## 🧱 NFA Construction

📄 `nfa/Thompson_Converter.py`

- Creates an NFA using Thompson’s Construction
- Handles:
  - Literals
  - Kleene Star `*`
  - One-or-more `+`
  - Optional `?`
  - Union `|`
  - Concatenation `.`
- Transitions include **epsilon (ε)**

---

## 🔁 DFA Conversion

📄 `nfa_to_dfa/DFA_Converter.py`

- Converts an NFA to an equivalent DFA
- Uses **Subset Construction Algorithm**
- DFA states are labeled and visualized separately
- Ensures determinism (no ε-transitions, no multiple edges)

---

## 🖼 Graph Visualization (NFA + DFA)

📄 `visualizer/draw_nfa.py`, `draw_dfa.py`

- Uses **Graphviz** to create and render:
  - State diagrams with labels
  - Directed arrows (`→`)
  - Loops and branches
- Accept states are highlighted (double circles)
- Graphs are auto-opened on generation
- Output files saved as:

```
nfa_<regex>.png
dfa_<regex>.png
```

Example:
```
Regex: a(b|c)* ➤ Saves: nfa_a_b_c_.png & dfa_a_b_c_.png
```

---

## 💻 Tech Stack

| Component        | Tool/Library              |
|------------------|---------------------------|
| Regex Parser     | Custom Python             |
| NFA Generation   | Thompson’s Algorithm      |
| DFA Conversion   | Subset Construction       |
| Graph Rendering  | `graphviz` (Python lib)   |
| CLI Interface    | Python `input()`          |
| (Planned) Web UI | HTML/JS + Cytoscape       |

---

## 🧪 Example Input

```text
Regex: a(b|c)*d

Prepared Infix: a.(b|c)*.d
Postfix: a b c | * . d .
```

✅ Output:
- `nfa_a_b_c_d_.png`
- `dfa_a_b_c_d_.png`

---

## 📦 Installation & Setup

### 1. Clone the Project

```bash
git clone https://github.com/<your-username>/regex-to-nfa-converter.git
cd regex-to-nfa-converter
```

### 2. Install Python Requirements

```bash
pip install graphviz
```

### 3. Install Graphviz System Package (required for rendering)

- **Windows:** https://graphviz.org/download/  
  ✅ Add the `bin/` folder to your system PATH
- **Linux:** `sudo apt install graphviz`
- **macOS:** `brew install graphviz`

---

## ▶️ How to Run

```bash
python src/main.py
```

🔤 Then input your regex when prompted.  
📁 Output graph files will appear in the working directory.

---

## 📝 Notes

- ✅ Graphs use safe filenames based on the input regex
- ⚠️ Make sure your regex only includes allowed characters
- Future upgrades will include:
  - Frontend interface
  - NFA ➤ DFA table generation
  - DFA minimization (optional)

---

## 📜 License

MIT License

---

## 👥 Team

> Add your name(s), student ID(s), and GitHub links here.

---
