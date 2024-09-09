print("Funciones creadas por el usuario")
# Las funciones
def Mi_lista():
    amigos = ["Luis","Marco","Oscar"]
    for dominguez in amigos:
        print(dominguez)

def Mi_tupla():
    lenguajes = ("C++","Java","Python")
    for lista in lenguajes:
        print(lista)

def Mi_conjunto():
    frutas = {"Manzana","Platano","Durazno"}
    for comida in frutas:
        print(comida)

def Mi_diccionario():
    auto = {
        "Marca":"Ford",
        "Modelo":"Figo",
        "Color":"Rojo"
    }
    for datos in auto:
        print(auto[datos])
# Llamadas a funciones
print("Mi lista")
Mi_lista()
print("Mi tupla")
Mi_tupla()
print("Mi conjunto")
Mi_conjunto()
print("Mi diccionario")
Mi_diccionario()