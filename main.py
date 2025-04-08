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

    return grafo, nodo_inicio

if __name__ == "__main__":
    ruta_archivo = "/Users/alumna/Desktop/7º Semestre/Dijkstra/Nodos.txt" #Pegar la ruta del archivo
    grafo, nodo_inicio = leer_nodos_desde_archivo(ruta_archivo)
