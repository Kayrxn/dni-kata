from src.tabla_asignacion import TablaAsignacion


class Dni:
    def __init__(self, dni: str = ""):
        self.tabla_asignacion = TablaAsignacion()
        self.establecer_dni(dni)
        # indicadores de validez que se establecen al validar
        self.numero_sano = False
        self.letra_sana = False

    def establecer_dni(self, dni: str):
        """Establece el DNI (sin validar)."""
        self.dni_original = dni.strip()
        dni_sano = self.dni_original.replace("-", "").replace(" ", "").upper()
        if len(dni_sano) == 0:
            self.numero_personal = ""
            self.letra_asignacion = ""
        else:
            self.numero_personal = dni_sano[:-1]
            self.letra_asignacion = dni_sano[-1]
        # Al cambiar el DNI, invalidamos las comprobaciones previas
        self.numero_sano = False
        self.letra_sana = False

    def obtener_dni(self) -> str:
        return self.dni_original

    def obtener_numero_sano(self) -> bool:
        return self.numero_sano

    def obtener_letra_sana(self) -> bool:
        return self.letra_sana

    def obtener_parte_alfabetica(self) -> str:
        return self.letra_asignacion

    def obtener_parte_numerica(self) -> str:
        return self.numero_personal if self.numero_sano else ""

    def comprobar_formato(self) -> bool:
        """Comprueba que el formato del CIF/DNI tiene número sano y la letra está permitida."""
        numero_ok = self.numero_personal.isdigit() and len(self.numero_personal) == 8
        letra_ok = (
            self.letra_asignacion.isalpha()
            and self.tabla_asignacion.isLetraPermitida(self.letra_asignacion)
        )
        return numero_ok and letra_ok

    def comprobar_validez(self) -> bool:
        """Valida el formato del DNI (establece numero_sano y letra_sana)."""
        self.numero_sano = (
            self.numero_personal.isdigit() and len(self.numero_personal) == 8
        )
        self.letra_sana = (
            self.letra_asignacion.isalpha()
            and self.tabla_asignacion.isLetraPermitida(self.letra_asignacion)
        )
        return self.numero_sano and self.letra_sana

    def comprobar_letra(self) -> bool:
        """Comprueba que la letra coincide con la letra calculada a partir del número."""
        if not self.numero_sano:
            return False
        letra_esperada = self.tabla_asignacion.calcularLetra(self.numero_personal)
        return letra_esperada == self.letra_asignacion

    def obtener_letra(self):
        """Devuelve la letra del DNI si el número es sano, o None si no lo es."""
        return None if not self.numero_sano else self.letra_asignacion

    def __repr__(self) -> str:
        return f"Dni('{self.dni_original}')"

    def __str__(self) -> str:
        return f"{self.numero_personal}-{self.letra_asignacion}"
