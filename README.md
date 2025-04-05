# 🎯 Regex to NFA/DFA Converter (Web Version)

A powerful, educational tool that takes a **Regular Expression (Regex)** and visually converts it to:

- ✅ Postfix notation (Shunting Yard Algorithm)
- ✅ **NFA** using **Thompson’s Construction**
- ✅ **DFA** using **Subset Construction**
- ✅ Fully visualized using `graphviz`
- ✅ Delivered as a **web-based interface** using **Flask**

---

## 🗂 Project Structure

```
RegEx-to-NFA-Converter/
│
├── public/                     # Static files (e.g., JSON test cases)
├── src/
│   ├── app.py                  # 🔥 Flask web app entry point
│   ├── parser/                 # Infix ➜ Postfix (Shunting Yard)
│   ├── nfa/                    # NFA builder (Thompson)
│   ├── nfa_to_dfa/             # DFA converter (Subset Construction)
│   ├── visualizer/             # Graphviz-based NFA/DFA drawing
├── visualizer/                # React/HTML UI components
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🔥 Features

- ✅ Converts valid regular expressions into **Postfix Notation**
- ✅ Builds **NFA** using Thompson’s Algorithm
- ✅ Converts NFA ➜ DFA using Subset Construction
- ✅ Renders visual graphs using `graphviz`
- ✅ Accepts complex regex like:  
  `((a(b(c?(d+)?)*))|(e+f))*`

---

## ⚙ How to Run the Web App

### 1. 📦 Install Python Packages

Make sure you have Python 3.7+ installed.

```bash
pip install flask graphviz
```

### 2. 🧱 Install Graphviz (System Package)

> Needed for rendering the visual graphs

- **Windows:** Download from https://graphviz.org/download/
- **Linux:** `sudo apt install graphviz`
- **macOS:** `brew install graphviz`

✅ Make sure the `bin/` directory is in your PATH (for dot executable).

---

### 3. 🚀 Run the Web App

```bash
cd src
python app.py
```

Then open:

```
http://127.0.0.1:5000
```

You’ll see a **one-page interface** where you can:
- Input a regex
- View the postfix conversion
- View the NFA & DFA diagrams
- View transition tables and states

---

## 🧪 Example Test Inputs

| Regex | Description |
|-------|-------------|
| `a(b|c)*` | Basic Kleene star + union |
| `((ab)?|c*d)*e` | Complex nested expression |
| `a?(b+c)*d` | Optional, alternation, repetition |
| `((a|b)c)*d*e+` | Deep group nesting |
| `a(b(c)?d)*|e+f` | Grouped optional & concatenation |

---

## 🛠 Developer Notes

- All outputs are saved in `src/nfa_graph/` or `dfa_graph/` as `.png`
- Graph filenames are based on input regex (sanitized)
- Supports regex tokens: `a-z`, `A-Z`, `0-9`, `|`, `*`, `+`, `?`, `.`

---

## 📝 Commit Log Example

> Last Fix:  
```
🔧 Fix: Corrected parser logic for postfix conversion with nested operators
```
---
## 🧾 Additional Resources

### 📘 Project Documentation

- 📄 **Word Document**:  
  You can find the detailed project report in Word format here:  
  [📥 Download Project Documentation](./Regex-to-NFA .docx) 
 
### 📓 Notion Workspace

- 📚 **Notion Page**:  
  Explore our team notes, planning, and additional resources here:  
  [🔗 Open Notion Workspace](https://furtive-dietician-ff7.notion.site/REGEX-TO-NFA-Converter-1c81adc35e658074ba47c8100a938a9e)

---

## 📜 License

MIT License ©

---

## 👨‍💻 Team

> Add your team members' names, GitHub links, and student IDs here.

---
