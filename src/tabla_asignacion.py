class TablaAsignacion:
    def __init__(self):
        self.tabla = [
            "T",
            "R",
            "W",
            "A",
            "G",
            "M",
            "Y",
            "F",
            "P",
            "D",
            "X",
            "B",
            "N",
            "J",
            "Z",
            "S",
            "Q",
            "V",
            "H",
            "L",
            "C",
            "K",
            "E",
        ]

    def getTabla(self):
        return self.tabla

    def getLetra(self, posicion):
        try:
            return self.tabla[posicion]
        except IndexError:
            return "Posición letra fuera de rango"

    def getModulo(self):
        return len(self.getTabla())

    def isLetraPermitida(self, letra):
        return letra in self.getTabla()

    def calcularLetra(self, numero_dni):
        posicion = int(numero_dni) % self.getModulo()
        return self.getLetra(posicion)
