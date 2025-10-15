lista = ["Mateo", "Pablo", "Izan", "Emmanuel", "Federico"]
nombres_largos = list(filter(lambda x: len(x) > 5, lista))

if len(nombres_largos) > 0:
    print(f"Hay {len(nombres_largos)} nombres con mas de 5 letras: {nombres_largos}")
else:
    print("No hay ningun nombre com mas de 5 letras")