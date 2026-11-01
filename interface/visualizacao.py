import networkx as nx
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class VisualizacaoGrafo:

    def __init__(self, parent):
        self.parent = parent
        self.canvas = None

    def desenhar(self, G, caminho=None):

        fig, ax = plt.subplots(figsize=(9, 6))

        pos = nx.spring_layout(G, k=0.7, seed=42)

        nx.draw_networkx_nodes(
            G, pos,
            node_size=700,
            node_color="lightblue",
            ax=ax
        )

        nx.draw_networkx_nodes(
            G, pos,
            nodelist=["BS"],
            node_size=900,
            node_color="lightgreen",
            ax=ax
        )

        nx.draw_networkx_labels(G, pos, ax=ax)

        nx.draw_networkx_edges(
            G, pos,
            edge_color="gray",
            alpha=0.5,
            arrows=True,
            ax=ax
        )

        # Destaca a rota calculada
        if caminho:
            arestas_rota = list(zip(caminho, caminho[1:]))

            nx.draw_networkx_edges(
                G, pos,
                edgelist=arestas_rota,
                edge_color="red",
                width=3,
                arrows=True,
                ax=ax
            )

        ax.set_axis_off()

        # Remove visualização anterior
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        self.canvas = FigureCanvasTkAgg(
            fig, master=self.parent
        )

        self.canvas.draw()
        self.canvas.get_tk_widget().pack(
            fill="both", expand=True
        )

        plt.close(fig)