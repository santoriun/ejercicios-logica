"""
Recrea el juego piedra, papel o tijeras, donde jueges contra la maquina. termina el que gane 3 veces.
En este ejercicio se deben emplear condicionales y bucles, ademas de tener en cuenta que la maquina debe seleccionar una opcion aleatoria.
"""

# Participan dos usuarios y los dos seleccinan una opcion. Si son iguales se repite, Si son distintas gana uno de los dos.
# Como se gana -> Piedra le gana a tijeras, tijeras le gana a papal y papel le gana a piedra. (debe de existir un acomulador para los puntos).
import random

victorias_usuario = 0
victorias_maquina = 0
# Valor para mostrar que se saco.
opciones_dict={
    "1" : "Piedra",
    "2" : "Papel",
    "3" : "Tijeras"
}

while victorias_usuario < 3 and victorias_maquina < 3:

    # piedra es igual a 1 - papel es igual a 2 - tijeras es igual 3.

    opcion_usuario = input("Selecciona:\n[1] Piedra.\n[2] Papel.\n[3] Tijeras\n")
    # Opciones aleatorias para que la maquina seleccione.
    opciones = ["1","2","3"]
    opcione_maquina = random.choice(opciones)

    
    print("*"*20)
    print(f"Tu escoges {opciones_dict[opcion_usuario]} y la maquina {opciones_dict[opcione_maquina]}")

    if opcion_usuario == opcione_maquina:
        print('Fue un empate')
    elif opcion_usuario == "1" and opcione_maquina == "3":
        print("Tu sacas piedra la maquina tijeras. Genial Ganaste!!!")
        victorias_usuario+=1
    elif opcion_usuario == "2" and opcione_maquina == "1":
            print("Tu sacas papel la maquina piedras. Genial Ganaste!!!")
            victorias_usuario+=1
    elif opcion_usuario == "3" and opcione_maquina == "2":
            print("Tu sacas tijeras la maquina papel. Genial Ganaste!!!")
            victorias_usuario+=1
    else:
        
        print(f"Ohh perdiste!!! La maquina saco {opciones_dict[opcione_maquina]} y tu sacaste {opciones_dict[opcion_usuario]}")
        victorias_maquina += 1

    print("-------------- tabla de ganadores----------------")      
    print(f"Quien va ganando: \nMaquina {victorias_maquina}\nTu {victorias_usuario}")          
    