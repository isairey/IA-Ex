import networkx as nx
import matplotlib.pyplot as plt

class RedSemantica:
    def __init__(self):
        self.grafo = nx.DiGraph()

    def agregar_relacion(self, nodo1, relacion, nodo2):
        """Agrega una relación dirigida entre dos nodos."""
        self.grafo.add_edge(nodo1, nodo2, label=relacion)

    def mostrar_relaciones(self):
        """Muestra las relaciones en la red semántica."""
        for nodo1, nodo2, data in self.grafo.edges(data=True):
            print(f"{nodo1} --({data['label']})--> {nodo2}")

    def inferir_relacion(self, origen, destino):
        """Verifica si hay un camino entre dos nodos."""
        if nx.has_path(self.grafo, origen, destino):
            path = nx.shortest_path(self.grafo, origen, destino)
            return f"Sí, existe una relación: {' → '.join(path)}"
        return "No hay relación entre estos nodos."

    def visualizar_red(self):
        """Dibuja la red semántica."""
        plt.figure(figsize=(10, 6))
        pos = nx.spring_layout(self.grafo)
        nx.draw(self.grafo, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, edge_color="gray")
        etiquetas = nx.get_edge_attributes(self.grafo, 'label')
        nx.draw_networkx_edge_labels(self.grafo, pos, edge_labels=etiquetas, font_size=9, font_color="red")
        plt.title("Red Semántica Compleja", fontsize=12)
        plt.show()
red = RedSemantica()
red.agregar_relacion("Perro", "es un", "Mamífero")
red.agregar_relacion("Gato", "es un", "Mamífero")
red.agregar_relacion("Mamífero", "es un", "Animal")
red.agregar_relacion("Pájaro", "es un", "Ave")
red.agregar_relacion("Ave", "es un", "Animal")
red.agregar_relacion("Pájaro", "tiene", "Plumas")
red.agregar_relacion("Perro", "tiene", "Patas")
red.agregar_relacion("Perro", "come", "Carne")
red.agregar_relacion("Gato", "come", "Pescado")
red.agregar_relacion("Humano", "tiene", "Inteligencia")
red.agregar_relacion("Inteligencia", "permite", "Aprender")
red.agregar_relacion("Aprender", "genera", "Conocimiento")

print("\n Relaciones en la Red Semántica:")
red.mostrar_relaciones()

print("\n🔎 ¿El Perro es un Animal?")
print(red.inferir_relacion("Perro", "Animal"))

print("\n🔎 ¿La inteligencia genera conocimiento?")
print(red.inferir_relacion("Inteligencia", "Conocimiento"))

red.visualizar_red()
