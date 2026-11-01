import networkx as nx

def calcular_rota(G, origem, destino, algoritmo):

    try:
        if algoritmo == "Dijkstra":

            caminho = nx.dijkstra_path(
                G, origem, destino, weight="weight"
            )

            distancia = nx.dijkstra_path_length(
                G, origem, destino, weight="weight"
            )

        elif algoritmo == "Bellman-Ford":

            caminho = nx.bellman_ford_path(
                G, origem, destino, weight="weight"
            )

            distancia = nx.bellman_ford_path_length(
                G, origem, destino, weight="weight"
            )

        else:
            raise ValueError("Algoritmo inválido")

        return caminho, distancia

    except (nx.NetworkXNoPath, nx.NodeNotFound) as erro:
        return None, str(erro)