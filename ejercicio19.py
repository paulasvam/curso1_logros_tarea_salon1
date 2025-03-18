def juego_espacial():
    print("REGLAS DEL JUEGO.")
    print("1. Debes de escribir de la opcion que prefieras.")
    print("2. En caso de no escribir alguna de las opciones mostradas e ingresar una opcion no existente el juego finalizara.")
    print("3. DISFRUTA LA AVENTURA ESPACIAL.")
    
    
    print("\n¡ALERTAAAA! Un extraterrestre se ha infiltrado en la nave espacial.")
    print("Necesitas escapar antes de que sea demasiado tarde.")
    
    # Nivel 2: Salir al pasillo
    print("\nEstás en la cabina de mando. Tienes dos opciones:")
    print("1. SALIR al pasillo a revisar.")
    print("2. ESCONDERTE detrás de la cabina de control.")
    
    eleccion1 = input("Elige una opción (SALIR/ESCONDERTE): ").strip().upper()
    
    if eleccion1 == "SALIR":
        # Nivel 2: Salir al pasillo
        print("\nSales al pasillo a revisar. Mientras revisas empiezas a escuchar ruidos extraños.")
        print("Tienes tres opciones:")
        print("1. INVESTIGAR de donde salen los ruidos.")
        print("2. CORRER hacia la escotilla de emergencia.")
        print("3. REGRESAR a la cabina de mando.")
        
        eleccion2 = input("Elige una opción (INVESTIGAR/CORRER/REGRESAR): ").strip().upper()
        
        if eleccion2 == "INVESTIGAR":
            # Nivel 3: Investigar el ruido
            print("\nTe acercas al origen de los ruidos y descubres al extraterrestre.")
            print("Tienes dos opciones:")
            print("1. ATACAR al extraterrestre.")
            print("2. ESCAPAR.")
            
            eleccion3 = input("Elige una opción (ATACAR/ESCAPAR): ").strip().upper()
            
            if eleccion3 == "ATACAR":
                print("\nAtacas al extraterrestre, pero es más fuerte. ¡Has sido capturado por el extraterrestre! Fin del juego.")
            elif eleccion3 == "ESCAPAR":
                print("\nLogras escapar del extraterrestre y te diriges a la escotilla de emergencia. ¡Has logrado ecapar del extraterrestre!")
            else:
                print("Opción no válida. Fin del juego.")
        
        elif eleccion2 == "CORRER":
            # Nivel 3: Correr hacia la escotilla
            print("\nCorres hacia la escotilla de emergencia, pero el extraterrestre te ve.")
            print("Tienes dos opciones:")
            print("1. INTENTAR cerrar la escotilla de emergencia.")
            print("2. OCULTARTE en una habitacion cercana.")
            
            eleccion3 = input("Elige una opción (INTENTAR/OCULTARTE): ").strip().upper()
            
            if eleccion3 == "INTENTAR":
                print("\nIntentas cerrar la escotilla lo mas rapido posible, pero el extraterrestre te atrapa. Fin del juego.")
            elif eleccion3 == "OCULTARTE":
                print("\nTe ocultas y el extraterrestre pasa de largo. Logras escapar por la escotilla. ¡Has logrado ecapar del extraterrestre!")
            else:
                print("Opción no válida. Fin del juego.")

        elif eleccion2 == "REGRESAR":
            print("\nRegresas a la cabina de mando y te sientes seguro por un momento, pero el extraterrestre también vuelve. Fin del juego.")
        else:
            print("Opción no válida. Fin del juego.")

    elif eleccion1 == "ESCONDERTE":
        # Nivel 2: Esconderse detrás del panel
        print("\nTe escondes detrás de la cabina de control. Pero escuchas al extraterrestre moverse.")
        print("Tienes dos opciones:")
        print("1. SALIR de tu escondite.")
        print("2. ESPERAR a que se aleje.")
        
        eleccion2 = input("Elige una opción (SALIR/ESPERAR): ").strip().upper()
        
        if eleccion2 == "SALIR":
            # Nivel 3: Salir para buscar ayuda
            print("\nSales de tu escondite y te encuentras cara a cara con el extraterrestre.")
            print("Tienes dos opciones:")
            print("1. INTENTAR escapar de él.")
            print("2. CORRER hacia el laboratorio.")
            
            eleccion3 = input("Elige una opción (INTENTAR/CORRER): ").strip().upper()
            
            if eleccion3 == "INTENTAR":
                print("\nIntentas escapar del extraterrestre, pero eres atacado. ¡Has sido capturado! Fin del juego.")
            elif eleccion3 == "CORRER":
                print("\nCorres hacia el laboratorio y logras activar el sistema de autodestrucción de la habitacion en donde se encuentra el estraterrestre. ¡Has logrado ecapar del extraterrestre!")
            else:
                print("Opción no válida. Fin del juego.")

        elif eleccion2 == "ESPERAR":
            # Nivel 3: Esperar a que se aleje
            print("\nEsperas pacientemente y el extraterrestre se aleja.")
            print("Tienes dos opciones:")
            print("1. SALIR de tu escondite y buscar una salida.")
            print("2. REGRESAR al puente de mando.")
            
            eleccion3 = input("Elige una opción (SALIR/REGRESAR): ").strip().upper()
            
            if eleccion3 == "SALIR":
                print("\nSales de tu escondite y encuentras la escotilla abierta. ¡Has logrado ecapar del extraterrestre!")
            elif eleccion3 == "REGRESAR":
                print("\nRegresas a la cabina de mando, pero el extraterrestre te encuentra. Fin del juego.")
            else:
                print("Opción no válida. Fin del juego.")

        else:
            print("Opción no válida. Fin del juego.")

    else:
        print("Opción no válida. Fin del juego.")

# Iniciar el juego
juego_espacial()