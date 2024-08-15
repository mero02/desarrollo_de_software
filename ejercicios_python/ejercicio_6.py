from datetime import datetime 

class Libro:
    def __init__(self, titulo, autor, anio, genero):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero
    
    def obtener_info(self):
        return f"Titulo: {self.titulo} - Autor: {self.autor} - Año: {self.anio} - Genero: {self.genero}"

    def es_clasico(self):
        if(( datetime.now().year - self.anio) > 50):
            return True
        else:
            return False
        
if __name__ == "__main__":
    l1 = Libro("Los dias del venado","Liliana Bodoc", 2000, 'F')
    l2 = Libro("Festin de cuervos","George R.R. Martin",2005,'M')

    print(l1.obtener_info())
    print(l2.obtener_info())

    print(l1.es_clasico())
    print(l2.es_clasico())