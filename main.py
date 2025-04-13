#Biblioteca de Python para el estudio de grafos y análisis de redes
import networkx as nx

#Funcion que va a leer el archivo txt desde una ruta especifica
def leer_nodos_desde_archivo(ruta):
    grafo = nx.Graph() # Crea el grafo vacío

    with open(ruta, 'r') as archivo: #Se lee el archivo desde read (r)
        #Lee los datos de sus respectivas lineas
        num_nodos = int(archivo.readline().split('#')[0].strip())
        print(f"Número de nodos: {num_nodos}")

        num_aristas = int(archivo.readline().split('#')[0].strip())
        print(f"Número de aristas: {num_aristas}")

        # Agrega los nodos al grafo
        grafo.add_nodes_from(range(num_nodos))
        print("Nodos agregados al grafo:", list(grafo.nodes))

        print("Aristas:")
        for _ in range(num_aristas):
            linea = archivo.readline().split('#')[0].strip()
            u, v, peso = map(int, linea.split()) #Separa por espacio y convierte a entero
            grafo.add_edge(u, v, weight=peso)
            print(f"  {u} ---- {v}   ({peso})")

        nodo_inicio = int(archivo.readline().split('#')[0].strip())
        print(f"Nodo de inicio: {nodo_inicio}")

        nodo_final = int(archivo.readline().split('#')[0].strip())
        print(f"Nodo final: {nodo_final}")

    return grafo, nodo_inicio, nodo_final

def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo.nodes} #Inicializa las distancias a infinito porque todavía no sabemos la distancia real
    distancias[inicio] = 0 #El nodo de inicio esta con distancia 0
    visitados = [] #Lista de nodods visitados

    #Checar los nodos que aun no han sido visitados
    #La función len() en Python devuelve la cantidad de elementos de una lista, diccionario, conjunto, etc.
    while len(visitados) < len(grafo.nodes):
        nodo_actual = None
        for nodo in grafo.nodes:
            if nodo not in visitados:
                if nodo_actual is None or distancias[nodo] < distancias[nodo_actual]:
                    nodo_actual = nodo

        #Si no hay nodo actual, significa que todos los nodos han sido visitados
        if nodo_actual is None:
            break

        #El grafo.neighbors() viene de la biblioteca de networkx que devuelve una lista de nodos vecinos
        #Returns an iterator over all neighbors of node n.
        for vecino in grafo.neighbors(nodo_actual):
            if vecino not in visitados: 
                peso = grafo[nodo_actual][vecino]['weight'] #(u,v, peso)
                nueva_distancia = distancias[nodo_actual] + peso #Actualiza la distancia del path total hasta el momento
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia

        visitados.append(nodo_actual) #Agrega el nodo actual a la lista de visitados

    return distancias

if __name__ == "__main__":
    ruta_archivo = "/Users/alumna/Desktop/7º Semestre/Dijkstra/Nodos.txt" #Pegar la ruta del archivo
    grafo, nodo_inicio, nodo_final = leer_nodos_desde_archivo(ruta_archivo)

    distancias = dijkstra(grafo, nodo_inicio)

    print(f"\nDistancia mínima desde el nodo {nodo_inicio} al nodo {nodo_final}: {distancias[nodo_final]}")

