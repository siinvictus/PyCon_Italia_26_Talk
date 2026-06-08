import marimo

__generated_with = "0.23.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## <center>Graph Theory 101 and NetworkX in Python
    ### Silva Bashllari, PyCon Italia 2026, Bologna, Thursday 28 May.

    The following is a set of small examples on what can be done with graph theory and networkX in Python. This is part of the talk I gave at PyCon Italia. The talk was intented for absolute beginners and thus the notebook reflects that.
    """)
    return


@app.cell
def _():
    import networkx as nx
    import matplotlib.pyplot as plt

    return nx, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### <center> Creating Graphs
    Graphs can be both undirected or directed.
    They can be created out as an instance and then nodes and edges are added to them, or they can be created through an existing list of edges (which automatically adds the corresponding nodes) or through a list of nodes.
    """)
    return


@app.cell
def _(nx, plt):
    G = nx.Graph()
    G.add_edges_from([("A","B"), ("A","C"), ("B","D"), ("A","D")])

    D = nx.DiGraph()
    D.add_edges_from([("A","B"), ("A","C"), ("B","D"), ("A","D")])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    nx.draw(G, with_labels=True, ax=ax1)
    ax1.set_title("Undirected Graph")
    nx.draw(D, with_labels=True, ax=ax2)
    ax2.set_title("Directed Graph")
    plt.tight_layout()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You can always add notes and edges <i>incrementally.
    """)
    return


@app.cell
def _(nx, plt):
    G2 = nx.Graph()
    G2.add_nodes_from(["A","B","C","D"])
    G2.add_edges_from([("A","B"), ("A","C")])
    G2.add_node("E")
    G2.add_edge("B","D")

    nx.draw(G2, with_labels=True)
    plt.gca()
    return


@app.cell
def _(nx, plt):

    G3 = nx.Graph([("A","B"), ("B","C"), ("C","D")])

    G_weighted = nx.Graph()
    G_weighted.add_weighted_edges_from([
        ("A","B", 3), ("A","C", 5), ("B","D", 2), ("A","D", 4)
    ])

    pos = nx.spring_layout(G_weighted)
    nx.draw(G_weighted, pos, with_labels=True)
    labels = nx.get_edge_attributes(G_weighted, 'weight')
    nx.draw_networkx_edge_labels(G_weighted, pos, edge_labels=labels)
    plt.title("Weighted Graph")
    plt.show()
    return


if __name__ == "__main__":
    app.run()
