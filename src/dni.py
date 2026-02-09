from tabla_asignacion import TablaAsignacion


class Dni:
    def __init__(self, dni: str):
        self.dni_original = dni.strip()
        self.tabla_asignacion = TablaAsignacion()

        dni_sano = self.dni_original.replace("-", "").replace(" ", "").upper()
        if len(dni_sano) == 0:
            self.numero_personal = ""
            self.letra_asignacion = ""
        else:
            self.numero_personal = dni_sano[:-1]
            self.letra_asignacion = dni_sano[-1]

        def es_numero_personal_valido(self) -> bool:
            """Comprueba que la parte numérica tiene 8 dígitos y solo contiene números."""
            return self.numero_personal.isdigit() and len(self.numero_personal) == 8

        def es_letra_valida(self) -> bool:
            """Comprueba que la letra está permitida en la tabla de asignación."""
            return (
                self.letra_asignacion.isalpha()
                and self.tabla_asignacion.isLetraPermitida(self.letra_asignacion)
            )
