import csv
import os

class Grafo:
    def __init__(self):
        self.city = []
        self.conn = []
        self.cityFile = 'cidades.csv'
        self.connFile = 'conexoes.csv'
        self.csvExiste()

    def csvExiste(self):
        if not os.path.exists(self.cityFile):
            with open(self.cityFile, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['nome'])

        if not os.path.exists(self.connFile):
            with open(self.connFile, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                # cabeçalho
                writer.writerow(['cidade1', 'cidade2', 'distancia'])

    def regCity(self, name):
        for c in self.city:
            if c.name.lower() == name.lower():
                return c, False

        new_city = City(name)
        self.city.append(new_city)
        self.cadCityCSV(name)
        return new_city, True

    def cadCityCSV(self, name):
        with open(self.cityFile, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0].strip().lower() == name.lower():
                    return 

        with open(self.cityFile, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([name])

    def regConn(self, name1, name2, dist):
        city1, _ = self.regCity(name1)
        city2, _ = self.regCity(name2)

        for edge in self.conn:
            if (edge.origin == city1 and edge.destiny == city2) or (edge.origin == city2 and edge.destiny == city1):
                print("Conexão já existe.")
                return False

        edge = Edge(city1, city2, dist)
        city1.conn.append(edge)
        city2.conn.append(edge)
        city1.nb.append(city2)
        city2.nb.append(city1)
        self.conn.append(edge)

        self.cadConnCSV(name1, name2, dist)
        # print("Conexão registrada com sucesso.")
        return True

    def cadConnCSV(self, name1, name2, dist):
        with open(self.connFile, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 3 and row[0].strip().lower() == name1.lower() and row[1].strip().lower() == name2.lower():
                    return

        with open(self.connFile, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([name1, name2, dist])

    def readCSV(self):
        # Carrega cidades
        if os.path.exists(self.cityFile):
            with open(self.cityFile, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader, None)
                for row in reader:
                    if row:
                        self.regCity(row[0].strip())

        # Carrega conexões
        if os.path.exists(self.connFile):
            with open(self.connFile, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader, None)
                for row in reader:
                    if len(row) >= 3:
                        try:
                            name1 = row[0].strip()
                            name2 = row[1].strip()
                            dist = float(row[2].strip().replace(",", "."))
                            self.regCSV(name1, name2, dist)
                        except ValueError:
                            continue

    def regCSV(self, name1, name2, dist):
        city1, _= self.regCity(name1)
        city2, _= self.regCity(name2)

        if any((edge.origin == city1 and edge.destiny == city2) or (edge.origin == city2 and edge.destiny == city1) for edge in self.conn):
            return

        edge = Edge(city1, city2, dist)
        city1.conn.append(edge)
        city2.conn.append(edge)
        city1.nb.append(city2)
        city2.nb.append(city1)
        self.conn.append(edge)

    def infoCity(self):
        if not self.city:
            print("Nenhuma cidade cadastrada.")
            return
        print("Cidades cadastradas:")
        for c in self.city:
            print(f"- {c.name}")

    def infoConn(self):
        if not self.conn:
            print("Nenhuma conexão registrada.")
            return
        print("Conexões entre cidades:")
        for edge in self.conn:
            print(f"{edge.origin.name} ↔ {edge.destiny.name} = {edge.dist:.1f} km")

    def neighbors_of(self, name):
        for c in self.city:
            if c.name.lower() == name.lower():
                if not c.nb:
                    print(f"{c.name} não possui cidades vizinhas.")
                    return
                print(f"Vizinhos de {c.name}:")
                for neighbor in c.nb:
                    print(f"- {neighbor.name}")
                return
        print("Cidade não encontrada.")


class City:
    def __init__(self, name):
        self.name = name
        self.conn = []
        self.nb = []

class Edge:
    def __init__(self, origin, destiny, dist):
        self.origin = origin
        self.destiny = destiny
        self.dist = dist
