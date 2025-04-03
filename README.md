# 🎯 RegEx-to-NFA-Converter (Python Version)

A simple, educational tool that **parses regular expressions (regex)** and visualizes their equivalent **Non-deterministic Finite Automata (NFA)** using **Thompson’s Construction** — implemented entirely in **Python**.

---

## 📁 Project Directory Structure

```
REGEX-TO-NFA-CONVERTER/
│
├── public/
│   └── nfa_examples.json            # (Optional) Predefined NFA test cases
│
├── src/
│   ├── nfa/
│   │   ├── __init__.py
│   │   └── Thompson_Converter.py    # NFA builder (Thompson’s construction)
│   │
│   ├── parser/
│   │   ├── __init__.py
│   │   └── infix_to_postfix.py      # Regex parser (infix ➤ postfix)
│   │
│   ├── ui/
│   │   └── visualizer/
│   │       └── draw_nfa.py          # Graphviz-based visualizer
│
├── main.py                          # Main entry point to run the pipeline
├── nfa_graph.png                    # Output visualization (generated)
├── image.png                        # (Optional) Project diagram
├── .gitignore
├── LICENSE
└── README.md
```

## 🔄 What This Project Does

### ✅ Full Conversion Pipeline:

1. **Input a regex**
2. ➤ Insert concatenation (`.`) where needed
3. ➤ Convert **infix ➤ postfix** (Shunting Yard)
4. ➤ Generate NFA using **Thompson’s Construction**
5. ➤ Visualize the NFA as a graph with states & transitions

---

## 🧠 Regex Parsing (Python)

📄 `parser/infix_to_postfix.py`

- Inserts explicit `.` for concatenation
- Converts user-friendly syntax to machine-friendly postfix
- Supports:
  - Grouping `()`
  - Union `|` or `+`
  - Kleene Star `*`
  - Optional `?`
  - One or more `+`

---

## 🧱 NFA Construction (Thompson’s Algorithm)

📄 `nfa/Thompson_Converter.py`

- Builds an NFA from the postfix expression
- Represents each state with a `label`, `edge1`, and `edge2`
- All transitions support epsilon `ε` where needed

---

## 🖼 NFA Graph Visualization

📄 `visualizer/draw_nfa.py`

We use `graphviz` to visually draw your NFA with:
- Labeled transitions (`a`, `b`, or `ε`)
- Directed arrows between states
- Start and Accept states clearly highlighted

### ✅ Example Graph

- Start ➝ `a` ➝ `b` ➝ Accept
- Loops for `a*`, branches for `a|b`, etc.

---

## 💻 Tech Stack

| Component        | Tool/Library              |
|------------------|---------------------------|
| Regex Parsing     | Custom Python logic       |
| NFA Generation    | Thompson’s Algorithm in Python |
| Graph Visualization | `graphviz` (via Python package) |
| CLI Interface     | Python's built-in `input()` |
| (Planned) Web UI  | HTML, JS, Cytoscape.js or D3.js |

---

## 🧪 Example Input

```
Regex: a(b|c)*d
Prepared Infix: a.(b|c)*.d
Postfix: a b c | * . d .
```

✅ You’ll see a visual NFA graph open with correct transitions and layout!

---

## 📦 Installation & Setup

### 1. Clone the Project

```bash
git clone https://github.com/your-username/regex-to-nfa-converter.git
cd regex-to-nfa-converter
```

### 2. Install Python Libraries

```bash
pip install graphviz
```

### 3. (Important) Install Graphviz System Package

- **Windows:** Download from https://graphviz.org/download/
- **Linux:** `sudo apt install graphviz`
- **macOS:** `brew install graphviz`

> ✅ Be sure to add Graphviz’s `bin/` to your system PATH so `.render()` works

---

## ▶️ How to Run

```bash
python main.py
```

Then input any regex like:

```
a(b|c)*d
```

📸 The program will:
- Print prepared and postfix form
- Show a visual **NFA graph**

---

## 📜 License

MIT License (or your preferred one)

---

## 👥 Team

> Add your names and student IDs here

---
