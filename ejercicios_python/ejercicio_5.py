def getPeliculas(peliculas):
    i = 0
    for i in range(5):
        nombre = input("Ingrese el nombre de pelicula ")
        anio = input("Ingrese el año de estreno ")
        pelicula = {'anio': anio, 'nombre': nombre}
        peliculas.append(pelicula)
    return peliculas

def showPeliculas (peliculas):
    peliculas.sort(key=lambda pelicula: pelicula['nombre'])
    i = 0
    for i in range(5):
        print(f"Pelicula: {peliculas[i]['nombre']} - Año: {peliculas[i]['anio']}")
        

if __name__ == "__main__":
    peliculas = []
    getPeliculas(peliculas)
    showPeliculas(peliculas)