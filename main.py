from datetime import datetime
from typing import List

class Horaire:
    """
    Cette classe permet de modéliser un horaire de bus.
    """

    def __init__(self, heure: int, minute: int, ligne: 'Ligne'):
        self.heure = heure
        self.minute = minute
        self.ligne = ligne

    def __str__(self):
        return f"{self.heure:02d}:{self.minute:02d} ({self.ligne})"


class Ligne:
    """
    Cette classe représente une ligne de bus.
    """

    def __init__(self, nom: str):
        self.nom = nom

    def __str__(self):
        return f"Ligne {self.nom}"


class Station:
    """
    Cette classe représente une station de bus.
    """

    def __init__(self, nom: str):
        self.nom = nom
        self.horaires_semaine = {}
        self.horaires_weekend = {}
        self.horaires_feries = {}

    def add_horaire_semaine(self, jour: str, horaires: List[Horaire]):
        self.horaires_semaine[jour] = horaires

    def add_horaire_weekend(self, jour: str, horaires: List[Horaire]):
        self.horaires_weekend[jour] = horaires

    def add_horaire_ferie(self, date: str, horaires: List[Horaire]):
        self.horaires_feries[date] = horaires


class Calendrier:
    """
    Cette classe représente le calendrier des horaires de bus.
    """

    def __init__(self):
        self.stations = {}

    def ajouter_station(self, station: Station):
        self.stations[station.nom] = station

    def afficher_horaires(self):
        for nom, station in self.stations.items():
            print(f"Station: {nom}")
            print("Horaires en semaine:")
            for jour, horaires in station.horaires_semaine.items():
                print(f" - {jour}: {[str(horaire) for horaire in horaires]}")
            print("Horaires le weekend:")
            for jour, horaires in station.horaires_weekend.items():
                print(f" - {jour}: {[str(horaire) for horaire in horaires]}")
            print("Horaires les jours fériés:")
            for date, horaires in station.horaires_feries.items():
                print(f" - {date}: {[str(horaire) for horaire in horaires]}")

def ajouter_station_avec_horaires(calendrier, nom_station, horaires_semaine, horaires_weekend, horaires_feries):
    station = Station(nom_station)
    for jour, horaires in horaires_semaine.items():
        station.add_horaire_semaine(jour, horaires)
    for jour, horaires in horaires_weekend.items():
        station.add_horaire_weekend(jour, horaires)
    for date, horaires in horaires_feries.items():
        station.add_horaire_ferie(date, horaires)
    calendrier.ajouter_station(station)

# Création des lignes de bus
ligne1 = Ligne("4")
ligne2 = Ligne("2")

# Création du calendrier
calendrier = Calendrier()

# Ajout des stations avec leurs horaires
ajouter_station_avec_horaires(
    calendrier,
    "SEYNOD_NEIGEOS",
    {"Lundi": [Horaire(6, 4, ligne1), Horaire(6, 24, ligne1), Horaire(6, 44, ligne1), ]},  # Ajoutez les horaires pour chaque jour de la semaine
    {"Samedi": [Horaire(6, 4, ligne1), Horaire(6, 24, ligne1), Horaire(6, 44, ligne1), ...]},  # Ajoutez les horaires pour chaque jour du weekend
    {}  # Aucun horaire pour les jours fériés pour cette station
)

ajouter_station_avec_horaires(
    calendrier,
    "Saint-Jean",
    {"Lundi": [Horaire(6, 8, ligne1), Horaire(6, 28, ligne1), Horaire(6, 48, ligne1), ...]},
    {"Samedi": [Horaire(6, 8, ligne1), Horaire(6, 28, ligne1), Horaire(6, 48, ligne1), ...]},
    {}
)

ajouter_station_avec_horaires(
    calendrier,
    "L.P._Gordini",
    {"Lundi": [Horaire(6, 10, ligne1), Horaire(6, 30, ligne1), Horaire(6, 50, ligne1), ...]},
    {"Samedi": [Horaire(6, 10, ligne1), Horaire(6, 30, ligne1), Horaire(6, 50, ligne1), ...]},
    {}
)

ajouter_station_avec_horaires(
    calendrier,
    "IPAC-St-Michel",
    {"Lundi": [Horaire(6, 15, ligne1), Horaire(6, 35, ligne1), Horaire(6, 55, ligne1), ...]},
    {"Samedi": [Horaire(6, 15, ligne1), Horaire(6, 35, ligne1), Horaire(6, 55, ligne1), ...]},
    {}
)

ajouter_station_avec_horaires(
    calendrier,
    "Lycée_Gabriel Fauré",
    {"Lundi": [Horaire(6, 18, ligne1), Horaire(6, 38, ligne1), Horaire(6, 58, ligne1), ...]},
    {"Samedi": [Horaire(6, 18, ligne1), Horaire(6, 38, ligne1), Horaire(6, 58, ligne1), ...]},
    {}
)

ajouter_station_avec_horaires(
    calendrier,
    "GARE",
    {"Lundi": [Horaire(6, 21, ligne1), Horaire(6, 41, ligne1), Horaire(7, 1, ligne1), ...]},
    {"Samedi": [Horaire(6, 21, ligne1), Horaire(6, 41, ligne1), Horaire(7, 1, ligne1), ...]},
    {}
)

ajouter_station_avec_horaires(
    calendrier,
    "Lycée_Berthollet",
    {"Lundi": [Horaire(6, 25, ligne1), Horaire(6, 45, ligne1), Horaire(7, 5, ligne1), ...]},
    {"Samedi": [Horaire(6, 25, ligne1), Horaire(6, 45, ligne1), Horaire(7, 5, ligne1), ...]},
    {}
)

ajouter_station_avec_horaires(
    calendrier,
    "Plaine_Novel",
    {"Lundi": [Horaire(6, 29, ligne1), Horaire(6, 49, ligne1), Horaire(7, 9, ligne1), ...]},
    {"Samedi": [Horaire(6, 29, ligne1), Horaire(6, 49, ligne1), Horaire(7, 9, ligne1), ...]},
    {}
)

ajouter_station_avec_horaires(
    calendrier,
    "Evire",
    {"Lundi": [Horaire(6, 33, ligne1), Horaire(6, 53, ligne1), Horaire(7, 13, ligne1), ...]},
    {"Samedi": [Horaire(6, 33, ligne1), Horaire(6, 53, ligne1), Horaire(7, 13, ligne1), ...]},
    {}
)

ajouter_station_avec_horaires(
    calendrier,
    "Ponchy",
    {"Lundi": [Horaire(6, 36, ligne1), Horaire(6, 56, ligne1), Horaire(7, 16, ligne1), ]},
    {"Samedi": [Horaire(6, 36, ligne1), Horaire(6, 56, ligne1), Horaire(7, 16, ligne1), ]},
    {}
)

ajouter_station_avec_horaires(
    calendrier,
    "I.U.T.",
    {"Lundi": [Horaire(6, 38, ligne1), Horaire(6, 58, ligne1), Horaire(7, 18, ligne1), ]},
    {"Samedi": [Horaire(6, 38, ligne1), Horaire(6, 58, ligne1), Horaire(7, 18, ligne1), ]},
    {}
)

ajouter_station_avec_horaires(
    calendrier,
    "CAMPUS",
    {"Lundi": [Horaire(6, 39, ligne1), Horaire(6, 59, ligne1), Horaire(7, 19, ligne1), ]},
    {"Samedi": [Horaire(6, 39, ligne1), Horaire(6, 59, ligne1), Horaire(7, 19, ligne1), ]},
    {}
)

# Affichage des horaires
calendrier.afficher_horaires()

  
import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        
    def add_node(self, value):
        self.nodes.add(value)
        if value not in self.edges:
            self.edges[value] = []
        
    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append((to_node, weight))
        
def dijkstra(graph, start, option, departure_time):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = departure_time
    
    heap = [(departure_time, start)]
    while heap:
        current_distance, current_node = heapq.heappop(heap)
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph.edges[current_node]:
            new_distance = current_distance
            if option == 'Shortest':
                new_distance += 1
            elif option == 'Fastest':
                new_distance += weight
            elif option == 'Foremost':
                new_distance = min(new_distance, weight)  # Utilise l'heure d'arrivée la plus tôt
            
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))
    del distances[start]
    return distances

# Exemple d'utilisation
graph = Graph()
graph.add_node('SEYNOD_NEIGEOS')
graph.add_node('Saint-Jean')
graph.add_node('L.P._Gordini ')
graph.add_node('IPAC-St-Michel')

graph.add_edge('SEYNOD_NEIGEOS', 'Saint-Jean', 5)  # temps de trajet de 5 minutes
graph.add_edge('Saint-Jean', 'L.P._Gordini ', 10)  # temps de trajet de 10 minutes
graph.add_edge('SEYNOD_NEIGEOS', 'IPAC-St-Michel', 15)  # temps de trajet de 15 minutes
graph.add_edge('IPAC-St-Michel', 'Saint-Jean', 20)  #  temps de trajet de 20 minutes
graph.add_edge('SEYNOD_NEIGEOS', 'L.P._Gordini ', 25)  # temps de trajet de 25 minutes
graph.add_edge('L.P._Gordini ', 'Saint-Jean', 30)  # temps de trajet de 30 minutes

heure_depart = 10  # Heure de départ

# Plus court chemin
chemin_plus_court = dijkstra(graph, 'SEYNOD_NEIGEOS', 'Shortest', heure_depart)
print("Plus court chemin:", chemin_plus_court)

# Chemin le plus rapide
chemin_plus_rapide = dijkstra(graph, 'SEYNOD_NEIGEOS', 'Fastest', heure_depart)
print("Chemin le plus rapide:", chemin_plus_rapide)

# Chemin le plus tôt
chemin_plus_tot = dijkstra(graph, 'SEYNOD_NEIGEOS', 'Foremost', heure_depart)
print("Chemin le plus tôt:", chemin_plus_tot)
