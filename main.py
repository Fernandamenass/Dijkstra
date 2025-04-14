import networkx as nx #Librería para trabajar con grafos
import matplotlib.pyplot as plt #Librería para graficar

# Función para leer archivo de texto
def leer_nodos_desde_archivo(ruta):
    grafo = nx.Graph()
    with open(ruta, 'r') as archivo:
        # Leer el número de nodos
        num_nodos = int(archivo.readline().split('#')[0].strip())
        print(f"Número de nodos: {num_nodos}")

        # Leer el número de aristas
        num_aristas = int(archivo.readline().split('#')[0].strip())
        print(f"Número de aristas: {num_aristas}")

        # Añadir nodos al grafo
        grafo.add_nodes_from(range(num_nodos))
        print("Nodos agregados al grafo:", list(grafo.nodes))

        # Leer cada arista con su peso y añadirlas al grafo
        print("Aristas:")
        for _ in range(num_aristas):
            linea = archivo.readline().split('#')[0].strip() # Ignorar comentarios
            u, v, peso = map(int, linea.split()) # Separar nodos y peso
            grafo.add_edge(u, v, weight=peso)
            print(f"  {u} ---- {v}   ({peso})")

        # Leer el nodo de inicio y el nodo final
        nodo_inicio = int(archivo.readline().split('#')[0].strip())
        print(f"Nodo de inicio: {nodo_inicio}")

        nodo_final = int(archivo.readline().split('#')[0].strip())
        print(f"Nodo final: {nodo_final}")

    return grafo, nodo_inicio, nodo_final

# Función de Dijkstra
def dijkstra(grafo, inicio):
    #Inicializar todas las distancias como infinito, excepto el nodo inicial
    distancias = {nodo: float('inf') for nodo in grafo.nodes}
    distancias[inicio] = 0 # La distancia del nodo inicial a sí mismo es 0
    predecesores = {}  # Rastrear el camino óptimo
    visitados = [] # Nodos ya visitados

    # Mientras haya nodos no visitados
    while len(visitados) < len(grafo.nodes):
        # Seleccionar el nodo no visitado con la distancia más corta
        nodo_actual = None
        for nodo in grafo.nodes:
            if nodo not in visitados:
                if nodo_actual is None or distancias[nodo] < distancias[nodo_actual]:
                    nodo_actual = nodo

        if nodo_actual is None:
            break # No hay nodos vecinos restantes

        # Actualizar las distancias de los nodos vecinos
        for vecino in grafo.neighbors(nodo_actual):
            if vecino not in visitados:
                peso = grafo[nodo_actual][vecino]['weight']
                nueva_distancia = distancias[nodo_actual] + peso
                # Si la nueva distancia es menor, actualizar la distancia
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    predecesores[vecino] = nodo_actual  # Guarda de dónde vino

        # Marcar el nodo actual como visitado
        visitados.append(nodo_actual)

    return distancias, predecesores

# Reconstruye la ruta más corta
def reconstruir_ruta(predecesores, inicio, fin):
    ruta = []
    actual = fin
    # Retroceder desde el nodo final hasta el inicial
    while actual != inicio:
        ruta.append(actual)
        actual = predecesores.get(actual)
        if actual is None:
            return []  # No hay ruta
    ruta.append(inicio) # Agregar el nodo inicial al final
    ruta.reverse()  # Invertir
    return ruta

# Función para visualizar el grafo 
def mostrar_grafo(grafo):
    pos = nx.spring_layout(grafo) # Calcular disposición de los nodos
    nx.draw(grafo, pos, with_labels=True, node_size=500, node_color="skyblue",
            font_size=12, font_weight="bold", edge_color="gray")
    # Mostrar pesos
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
