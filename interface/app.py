import customtkinter as ctk

from core.grafo import criar_grafo
from core.algoritmos import calcular_rota
from interface.visualizacao import VisualizacaoGrafo


class Aplicacao(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Otimizador de Rotas")
        self.geometry("1200x750")

        self.G = criar_grafo()

        self.sidebar = ctk.CTkFrame(self, width=250)
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)

        self.area_grafo = ctk.CTkFrame(self)
        self.area_grafo.pack(
            side="right",
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        ctk.CTkLabel(
            self.sidebar,
            text="OTIMIZADOR DE ROTAS",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        # Origem
        ctk.CTkLabel(self.sidebar, text="Origem").pack()

        self.origem = ctk.CTkComboBox(
            self.sidebar,
            values=list(self.G.nodes)
        )
        self.origem.pack(pady=10)

        # Destino
        ctk.CTkLabel(self.sidebar, text="Destino").pack()

        self.destino = ctk.CTkComboBox(
            self.sidebar,
            values=list(self.G.nodes)
        )
        self.destino.pack(pady=10)

        # Algoritmo
        ctk.CTkLabel(self.sidebar, text="Algoritmo").pack()

        self.algoritmo = ctk.CTkComboBox(
            self.sidebar,
            values=["Dijkstra", "Bellman-Ford"]
        )
        self.algoritmo.pack(pady=10)

        self.resultado = ctk.CTkLabel(
            self.sidebar,
            text="Aguardando cálculo..."
        )
        self.resultado.pack(pady=20)

        ctk.CTkButton(
            self.sidebar,
            text="Calcular rota",
            command=self.calcular
        ).pack(pady=10)

        self.visualizacao = VisualizacaoGrafo(
            self.area_grafo
        )

        self.visualizacao.desenhar(self.G)

    def calcular(self):

        origem = self.origem.get()
        destino = self.destino.get()
        algoritmo = self.algoritmo.get()

        caminho, distancia = calcular_rota(
            self.G, origem, destino, algoritmo
        )

        if caminho is None:
            self.resultado.configure(text=distancia)
            return

        self.resultado.configure(
            text=f"Rota: {' → '.join(caminho)}\n"
                 f"Custo: {distancia:.2f}"
        )

        self.visualizacao.desenhar(
            self.G, caminho
        )