
"""

"""

def calcular_presupuesto(compras: list, presupuesto_maximo: float) -> dict:
    total_acumulado = 0.0
    mas_caro_nombre = None
    mas_caro_precio = 0
    sobrepasa = False
    
    try:

        for producto in compras:

            if producto["precio"] <= 0:
                print(f"El precio del producto ({producto["nombre"]}) no puede procesado por ser menor o igual a 0")
            
            else:
                total_acumulado += producto["precio"]

            if producto["precio"] > mas_caro_precio:
                mas_caro_precio = producto["precio"]
                mas_caro_nombre = producto["nombre"]

        # Validar si sobrepasa
        if total_acumulado > presupuesto_maximo:
            sobrepasa = True
    except TypeError as e:
        print("El valor pasado por parametro a la funcion no no es un entero o una lista, revisa.")
        return

    resumen = {
        "total": total_acumulado,
        "sobrepasa": sobrepasa,
        "producto_mas_caro": mas_caro_nombre
    }

    return resumen


if __name__ == '__main__':
    # --- Pruebas de ejecución ---
    lista_1 = [
        {"nombre": "Teclado", "precio": 150},
        {"nombre": "Mouse", "precio": 80},
        {"nombre": "Monitor", "precio": 300}
    ]

    # Prueba A: Debería calcular bien los 530 de total y el producto más caro (Monitor)
    print(calcular_presupuesto(lista_1, "a"))

    # Prueba B: ¿Qué pasa si la lista está vacía?
    print(calcular_presupuesto([], 100))

    # Prueba C: ¿Qué pasa si hay precios negativos o productos en descuento total (0)?
    lista_2 = [{"nombre": "Muestra gratis", "precio": -1},{"nombre":"platano","precio":10}]
    print(calcular_presupuesto(lista_2, 50))


