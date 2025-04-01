# RegEx-to-NFA-Converter

A web-based tool that parses a regex and visualizes its equivalent NFA.

## Project Structure
regex-to-nfa-converter/ 
│ ├── 📁 src/
      │ ├── parser/ # Code for infix → postfix 
      │ ├── nfa/ # Thompson's construction code 
      │ ├── ui/ # HTML, CSS, JS frontend 
      │ ├── main.js # Entry point or integration logic 
│ ├── 📁 public/
      │ ├── nfa_examples.json # Sample regex and expected outputs 
│ ├── 📁 report/
      │ ├── Project_Report.pdf # Final report (to be added later) 
      │ ├── README.md # Project description + instructions 
├── .gitignore # Files to ignore in version control 
├── LICENSE # Open-source license if needed

## Features

- Supports regex parsing with union (`|`), concatenation, and Kleene star (`*`)
- Converts regex to postfix notation using the Shunting Yard algorithm
- Builds NFA using Thompson’s construction
- Graphically displays the resulting NFA using a JavaScript visualization library

## Tech Stack

- HTML/CSS/JavaScript
- [Cytoscape.js](https://js.cytoscape.org/) or [D3.js](https://d3js.org/) for visualization

## License

MIT or choose another license suitable for your team.
