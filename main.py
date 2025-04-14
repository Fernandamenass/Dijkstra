import networkx as nx
import matplotlib.pyplot as plt

def leer_nodos_desde_archivo(ruta):
    grafo = nx.Graph()
    with open(ruta, 'r') as archivo:
        num_nodos = int(archivo.readline().split('#')[0].strip())
        print(f"Número de nodos: {num_nodos}")

        num_aristas = int(archivo.readline().split('#')[0].strip())
        print(f"Número de aristas: {num_aristas}")

        grafo.add_nodes_from(range(num_nodos))
        print("Nodos agregados al grafo:", list(grafo.nodes))

        print("Aristas:")
        for _ in range(num_aristas):
            linea = archivo.readline().split('#')[0].strip()
            u, v, peso = map(int, linea.split())
            grafo.add_edge(u, v, weight=peso)
            print(f"  {u} ---- {v}   ({peso})")

        nodo_inicio = int(archivo.readline().split('#')[0].strip())
        print(f"Nodo de inicio: {nodo_inicio}")

        nodo_final = int(archivo.readline().split('#')[0].strip())
        print(f"Nodo final: {nodo_final}")

    return grafo, nodo_inicio, nodo_final

def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo.nodes}
    distancias[inicio] = 0
    predecesores = {}  # Nuevo: para reconstruir la ruta
    visitados = []

    while len(visitados) < len(grafo.nodes):
        nodo_actual = None
        for nodo in grafo.nodes:
            if nodo not in visitados:
                if nodo_actual is None or distancias[nodo] < distancias[nodo_actual]:
                    nodo_actual = nodo

        if nodo_actual is None:
            break

        for vecino in grafo.neighbors(nodo_actual):
            if vecino not in visitados:
                peso = grafo[nodo_actual][vecino]['weight']
                nueva_distancia = distancias[nodo_actual] + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    predecesores[vecino] = nodo_actual  # Guarda de dónde vino

        visitados.append(nodo_actual)

    return distancias, predecesores

# Función para reconstruir la ruta más corta usando los predecesores
def reconstruir_ruta(predecesores, inicio, fin):
    ruta = []
    actual = fin
    while actual != inicio:
        ruta.append(actual)
        actual = predecesores.get(actual)
        if actual is None:
            return []  # No hay ruta
    ruta.append(inicio)
    ruta.reverse()
    return ruta

def mostrar_grafo(grafo):
    pos = nx.spring_layout(grafo)
    nx.draw(grafo, pos, with_labels=True, node_size=500, node_color="skyblue",
            font_size=12, font_weight="bold", edge_color="gray")
    labels = nx.get_edge_attributes(grafo, 'weight')
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
    plt.title("Visualización del Grafo")
    plt.show()

if __name__ == "__main__":
    ruta_archivo = "/Users/alumna/Desktop/7º Semestre/Dijkstra/Nodos.txt"
    grafo, nodo_inicio, nodo_final = leer_nodos_desde_archivo(ruta_archivo)

    distancias, predecesores = dijkstra(grafo, nodo_inicio)
    ruta_mas_corta = reconstruir_ruta(predecesores, nodo_inicio, nodo_final)

    print(f"\nDistancia mínima desde el nodo {nodo_inicio} al nodo {nodo_final}: {distancias[nodo_final]}")
    if ruta_mas_corta:
        print("Ruta más corta:", " -> ".join(map(str, ruta_mas_corta)))
    else:
        print("No existe una ruta entre los nodos seleccionados.")

    mostrar_grafo(grafo)
