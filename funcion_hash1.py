"""
Crear una tabla hash, con una capacidad de 50 posiciones aplicando la formula Clave MOD 50.
Aplicar también la resolución de colisiones con la formula (Clave + 1) MOD 50.
Los valores a trabajar son [40, 50, 62, 103, 204, 304, 328].
"""

class TablaHash:
    def __init__(self, cantidad_posiciones: int = 50) -> None:
        self.cantidad_posiciones = cantidad_posiciones
        self.tabla = [None] * cantidad_posiciones

    def _generar_indice(self, valor: int) -> int:
        # Función Hash (CLAVE MOD 50).
        return valor % self.cantidad_posiciones

    def guardar_valor(self, valor: int) -> None:
        indice_base = self._generar_indice(valor)
        
        # Sondeo lineal aplicacion de fórmula (CLAVE + i) MOD 50.
        for i in range(self.cantidad_posiciones):
            indice_actual = (indice_base + i) % self.cantidad_posiciones
            
            # Validacion si la casilla está vacia o ya contiene el mismo valor.
            if self.tabla[indice_actual] is None or self.tabla[indice_actual] == valor:
                self.tabla[indice_actual] = valor
                return
           
        raise OverflowError("La tabla hash está llena.")

    def obtener_valor(self, valor: int) -> int | None:
        indice_base = self._generar_indice(valor)
        
        # Búsqueda con sondeo lineal.
        for i in range(self.cantidad_posiciones):
            indice_actual = (indice_base + i) % self.cantidad_posiciones
            contenido = self.tabla[indice_actual]
            
            if contenido == valor:
                return contenido
            if contenido is None:
                break
                
        return None


if __name__ == '__main__':

    # Valores planteados en la actividad.
    lista_valores = [40, 50, 62, 103, 204, 304, 328]

    tabla1 = TablaHash(cantidad_posiciones=50)

    for valor in lista_valores:
        tabla1.guardar_valor(valor)

    for i, contenido in enumerate(tabla1.tabla):
        print(f'Casilla {i} : Valor {contenido}')

    # Busqueda
    busqueda_valor =tabla1.obtener_valor(304)

    # Impresion del resultado.
    print(f'\nEl valor obtenido es: {busqueda_valor}')
