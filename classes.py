class vertex:
    def __init__(self, cityName):
        self.cityName = cityName
        self.conn = []
        self.nb = []

    def __repr__(self):
        return f"Vertice: ('{self.cityName}')"
    def __hash__(self):
        return hash(self.cityName)
    
    # Se tem o mesmo nome é o mesmo
    # e se o OBJ OTHER for de outra classe ja entrega FALSE (nao compara se nao tiver sentido)
    # ***isinstance*** verifica se o OBJ faz parta da classe "tal" ou seja igual a (se o dado OTHER for da classe VERTEX retorna True se nao False) E SERVE PRA CLASSES QUE HERDAM OUTRAS CLASSES TBM
    def __eq__(self, other):
        if isinstance(other, vertex):
            return self.cityName == other.cityName
        return False
    
    def infoNb(self):
        # usar list comprehension q é mais facil
        return [v.cityName for v in self.nb]
    
    def infoConn(self):
        # usar list comprehension q é mais facil
        return [c.infoEdge() for c in self.conn]
    
    def infoVert(self):
        return f"City: {self.cityName}\nNeighbors: {self.infoNb()}"   
     
class Edge:
    def __init__(self, origin, destiny, dist):
        self.oirigin = origin
        self.destiny = destiny
        self.dist = dist

    def infoEdge(self):
        return f"{self.origin.cityName} to {self.destiny.cityName} ({self.dist} km)"
        

class Graf:
    def __init__(self):
        self.city = []
        self.conn = []
    
    def infoCity(self):
        return [c.infoVert() for c in self.city]
    
    def infoConnect(self):
        return [c.infoEdge() for c in self.conn]
    
    def regCity(self, cityName):
        for city in self.