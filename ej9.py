import networkx as nx
import matplotlib.pyplot as plt

class RedSemantica:
    def __init__(self):
        self.grafo = nx.DiGraph()
        self.relaciones = {
            "Perro": [
                ("es un", "Mamífero"),
                ("tiene", "4 patas"),
                ("tiene", "cola"),
                ("emite sonido", "ladra"),
                ("es mascota de", "Humano"),
                ("come", "Carne")
            ],
            "Gato": [
                ("es un", "Mamífero"),
                ("tiene", "4 patas"),
                ("tiene", "cola"),
                ("emite sonido", "maúlla"),
                ("es mascota de", "Humano"),
                ("come", "Pescado")
            ],
            "Mamífero": [("es un", "Animal")],
            "Pájaro": [
                ("es un", "Ave"),
                ("tiene", "plumas"),
                ("puede", "volar"),
                ("pone", "huevos"),
                ("emite sonido", "canta")
            ],
            "Ave": [("es un", "Animal")],
            "Humano": [
                ("tiene", "Inteligencia"),
                ("puede", "aprender"),
                ("crea", "Tecnología"),
                ("trabaja en", "Profesión"),
                ("consume", "Alimentos")
            ],
            "Profesión": [
                ("incluye", "Médico"),
                ("incluye", "Ingeniero"),
                ("incluye", "Maestro"),
                ("incluye", "Científico"),
                ("incluye", "Artista")
            ],
            "Médico": [("trabaja en", "Hospital")],
            "Ingeniero": [("trabaja en", "Empresa de tecnología")],
            "Maestro": [("trabaja en", "Escuela")],
            "Científico": [("investiga", "Ciencia")],
            "Artista": [("crea", "Arte")],
            "Inteligencia": [("permite", "Aprender")],
            "Aprender": [("genera", "Conocimiento")],
            "Conocimiento": [("es base de", "Ciencia")],
            "Ciencia": [("impulsa", "Tecnología")],
            "Tecnología": [("transforma", "Sociedad")],
            "Sociedad": [("vive en", "Ciudades")],
            "Ciudades": [("tienen", "Transporte")],
            "Transporte": [("incluye", "Autos"), ("incluye", "Bicicletas"), ("incluye", "Aviones"), ("incluye", "Trenes")],
            "Robot": [
                ("es un", "Máquina"),
                ("puede tener", "Inteligencia Artificial"),
                ("se usa en", "Industria")
            ],
            "Máquina": [("puede tener", "Inteligencia Artificial")],
            "Inteligencia Artificial": [("es usada en", "Automatización")],
            "Automatización": [("mejora", "Eficiencia")],
            "Eficiencia": [("reduce", "Costos")],
            "Costos": [("afecta", "Economía")],
            "Ecosistema": [("incluye", "Bosque"), ("incluye", "Océano"), ("incluye", "Desierto"), ("incluye", "Montaña")],
            "Bosque": [("tiene", "Árboles"), ("alberga", "Animales")],
            "Océano": [("tiene", "Agua"), ("alberga", "Peces"), ("es", "Salado")],
            "Desierto": [("tiene", "Arena"), ("es", "Caluroso"), ("alberga", "Cactus")],
            "Montaña": [("tiene", "Rocas"), ("puede tener", "Nieve"), ("es", "Alta")]
        }

    def agregar_relacion_automatica(self, nodo):
        """Agrega automáticamente una relación basada en el nodo ingresado."""
        if nodo in self.relaciones:
            for relacion, nodo2 in self.relaciones[nodo]:
                self.grafo.add_edge(nodo, nodo2, label=relacion)
                print(f"Se agregó la relación: {nodo} --({relacion})--> {nodo2}")
        else:
            print(f"No se encontró una relación predefinida para {nodo}.")

    def mostrar_relaciones(self):
        """Muestra todas las relaciones de la red en texto."""
        if not self.grafo.edges:
            print("No hay relaciones en la red semántica.")
        else:
            for nodo1, nodo2, data in self.grafo.edges(data=True):
                print(f"{nodo1} --({data['label']})--> {nodo2}")

    def visualizar_red(self):
        """Dibuja la red semántica."""
        if not self.grafo.edges:
            print("No hay relaciones para visualizar.")
            return
        
        plt.figure(figsize=(14, 9))
        pos = nx.spring_layout(self.grafo, seed=42)
        
        nx.draw(self.grafo, pos, with_labels=True, node_size=3500, node_color="lightblue", font_size=10, edge_color="gray")
        etiquetas = nx.get_edge_attributes(self.grafo, 'label')
        nx.draw_networkx_edge_labels(self.grafo, pos, edge_labels=etiquetas, font_size=9, font_color="red")
        
        plt.title("Red Semántica Compleja", fontsize=14)
        plt.show()


red = RedSemantica()


while True:
    nodo = input("Ingrese un nombre (o 'salir' para terminar): ")
    if nodo.lower() == 'salir':
        break
    red.agregar_relacion_automatica(nodo)


print("\n📌 Relaciones en la Red Semántica:")
red.mostrar_relaciones()

red.visualizar_red()
