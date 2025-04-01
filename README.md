# RegEx-to-NFA-Converter

A simple web-based tool that parses regular expressions (regex) and visualizes their equivalent Non-deterministic Finite Automata (NFA).

---

## 📁 Project Directory Structure

![Project Folder Structure](./image.png)

---

## 🧠 Regex Parser (C++)

We implemented the **regex parsing step** in C++ using the Shunting Yard algorithm to convert infix expressions to postfix. This step prepares the expression for further processing into an NFA.

📄 **Code Location**:  
`src/parser/infix_to_postfix.cpp`

### ✅ Key Features:
- Inserts explicit concatenation operators (`.`) where needed
- Supports:
  - Grouping with `()`
  - Union using `|` or `+`
  - Kleene Star `*`
- Normalizes user-friendly syntax (e.g., converts `+` to `|`)
- Clean, testable output ready for Thompson’s Construction

### 🔄 Planned Enhancements:
- Expand character ranges like `[0-9]` into `(0|1|...|9)`
- Translate `A+` into `A.A*` (one or more)
- Translate `A?` into `(A|ε)` (optional)

### 🔢 Example:
Input: a(b|c)* Parsed: a.(b|c)* Postfix: a b c | * .


---

## ✨ Features Overview

- Parses regular expressions with support for:
  - Union (`|`)
  - Concatenation (`.`)
  - Kleene Star (`*`)
- Converts infix to postfix for easier NFA construction
- Generates NFAs using Thompson’s Construction algorithm
- Visually displays the NFA graph in a clean one-page web interface

---

## 💻 Tech Stack

- HTML, CSS, JavaScript
- Visualization: [Cytoscape.js](https://js.cytoscape.org/) or [D3.js](https://d3js.org/)
- Core logic (parser/NFA builder): C++ and/or JavaScript

---

## 📜 License

MIT License (or your preferred open-source license)

---

Let me know if you want to include your team members or usage instructions next!
