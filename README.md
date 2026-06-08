# Graph Theory 101 & NetworkX
## PyCon Italia 2026 — Bologna, 28 May 2026
### Silva Bashllari

#### Overview
Talk materials and interactive code examples from PyCon Italia 2026. It was intended for an audience of total beginners.
The talk argues that doing stuff with data is more than just ML — graph theory is a powerful mathematical tool that is underrepresented in the Python/data science community, and this talk is a small step toward changing that.

#### Contents
slides/          ← talk slides (PDF)
examples/
└── graphth101.py  ← interactive marimo notebook with all code examples

#### Topics Covered

- What is a graph — nodes, edges, weights, notation G = (V, E, W)
- Directed vs undirected graphs
- Graph traversal — walks, paths, trails, circuits, cycles
- Strong connectivity
- Centrality — degree centrality, eigenvector centrality
- Real examples — Medici family network, epidemic spreading, trade networks

#### How to Run the Examples
bash# Install dependencies
pip install -r requirements.txt

#### Launch the interactive notebook, this uses Marimo:
marimo edit examples/graphth101.py
Then open the URL shown in your terminal in your browser.

#### Tech Stack
Python, NetworkX, Matplotlib, Marimo

#### License
Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
