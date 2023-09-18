import datetime

class Persona:
    def __init__(self, cod_persona, nombre, ap_paterno, ap_materno, fecha_nac):
        self.cod_persona = cod_persona
        self.nombre = nombre
        self.ap_paterno = ap_paterno
        self.ap_materno = ap_materno
        self.fecha_nac = fecha_nac

    def imprimir(self):
        nombres = self.nombre
        apellidos = self.ap_paterno + ' ' + self.ap_materno
        cod_persona = self.cod_persona
        fecha_nac = self.fecha_nac
        return f' {nombres=},  {apellidos=}, {cod_persona=}, {fecha_nac=}'


class Autor(Persona):  # Hereda de Persona
    def __init__(self, cod_persona, nombre, ap_paterno, ap_materno, fecha_nac, codigo_autor, pais, editorial):
        super().__init__(cod_persona, nombre, ap_paterno, ap_materno, fecha_nac)
        self.codigo_autor = codigo_autor
        self.pais = pais
        self.editorial = editorial

    def imprimir(self):
        per_data = super().imprimir()
        codigo_autor = self.codigo_autor
        pais = self.pais
        editorial = self.editorial
        return f'Datos del autor son: {per_data}, Código de autor: {codigo_autor}, {pais=}, {editorial=}'

class Libro:
    def __init__(self, cod_libro, titulo, año, tomo, autor):
        self.cod_libro = cod_libro
        self.titulo = titulo
        self.año = año
        self.tomo = tomo
        self.autor = autor
    @staticmethod
    def guardar_datos_libros(nombre_archivo):
        try:
            with open(nombre_archivo, 'w') as archivo:
                archivo.write(f'Reporte de Libros - Fecha: {datetime.date.today()}\n')
                for libro in Libro.datos_libros:
                    archivo.write(f'Código del libro: {libro.cod_libro}\n')
                    archivo.write(f'Título: {libro.titulo}\n')
                    archivo.write(f'Año: {libro.año}\n')
                    archivo.write(f'Tomo: {libro.tomo}\n')
                    archivo.write(f'Código del autor: {libro.autor.codigo_autor}\n')
                    archivo.write(f'País del autor: {libro.autor.pais}\n')
                    archivo.write(f'Editorial del autor: {libro.autor.editorial}\n')
                    archivo.write(f'Código de la persona del autor: {libro.autor.cod_persona}\n')
                    archivo.write(f'Nombre del autor: {libro.autor.nombre}\n')
                    archivo.write(f'Apellido paterno del autor: {libro.autor.ap_paterno}\n')
                    archivo.write(f'Apellido materno del autor: {libro.autor.ap_materno}\n')
                    archivo.write(f'Fecha de nacimiento del autor: {libro.autor.fecha_nac}\n')
                    archivo.write('\n')  # Separador entre libros
            print(f'Los datos de los libros se han guardado en el archivo "{nombre_archivo}"')
        except Exception as e:
            print(f'Ocurrió un error al guardar los datos de los libros en el archivo: {e}')



    def imprimir(self):
        return f'Datos del libro: Código: {self.cod_libro}, Título: {self.titulo}, Año: {self.año}, Tomo: {self.tomo}\n{self.autor.imprimir()}'



# Clase de negocio para el mantenimiento de autores
class AutorNegocio:
    def __init__(self):
        self.listado_autores = []

    def registrar_autor(self, codigo_autor, pais, editorial, cod_persona, ap_paterno, ap_materno, fecha_nacimiento, nombre=""):
        autor = Autor(codigo_autor, pais, editorial, cod_persona, ap_paterno, ap_materno, fecha_nacimiento, nombre)
        self.listado_autores.append(autor)

    def obtener_autores(self):
        return self.listado_autores

    def editar_autor(self, codigo_autor, pais, editorial, cod_persona, ap_paterno, ap_materno, fecha_nacimiento, nombre=""):
        for autor in self.listado_autores:
            if autor.codigo_autor == codigo_autor:
                autor.pais = pais
                autor.editorial = editorial
                autor.cod_persona = cod_persona
                autor.ap_paterno = ap_paterno
                autor.ap_materno = ap_materno
                autor.fecha_nacimiento = fecha_nacimiento
                autor.nombre = nombre
                return f'Se editó correctamente al autor con código: {codigo_autor}'
        return 'No se encontró un autor con ese código'

    def eliminar_autor(self, codigo_autor):
        for autor in self.listado_autores:
            if autor.codigo_autor == codigo_autor:
                self.listado_autores.remove(autor)
                return f'Se eliminó correctamente al autor con código: {codigo_autor}'
        return 'No se encontró un autor con ese código'


# Clase de negocio para el mantenimiento de libros
class LibroNegocio:
    def __init__(self):
        self.listado_libros = []

    def registrar_libro(self, cod_libro, titulo, año, tomo, autor):
        libro = Libro(cod_libro, titulo, año, tomo, autor)
        self.listado_libros.append(libro)

    def obtener_libros(self):
        return self.listado_libros

    def editar_libro(self, cod_libro, titulo, año, tomo, cod_autor, pais, editorial, cod_persona, ap_paterno, ap_materno, fecha_nacimiento, nombre=""):
        for libro in self.listado_libros:
            if libro.cod_libro == cod_libro:
                libro.titulo = titulo
                libro.año = año
                libro.tomo = tomo
                libro.autor.codigo_autor = cod_autor
                libro.autor.pais = pais
                libro.autor.editorial = editorial
                libro.autor.cod_persona = cod_persona
                libro.autor.ap_paterno = ap_paterno
                libro.autor.ap_materno = ap_materno
                libro.autor.fecha_nacimiento = fecha_nacimiento
                libro.autor.nombre = nombre
                return f'Se editó correctamente el libro con código: {cod_libro}'
        return 'No se encontró un libro con ese código'

    def eliminar_libro(self, cod_libro):
        for libro in self.listado_libros:
            if libro.cod_libro == cod_libro:
                self.listado_libros.remove(libro)
                return f'Se eliminó correctamente el libro con código: {cod_libro}'
        return 'No se encontró un libro con ese código'



# Clase de negocio para generar reportes en un archivo de texto
class ReporteNegocio:
    def generar_reporte_libros(self, nombre_archivo, listado_libros):
        try:
            with open(nombre_archivo, 'w') as archivo:
                for libro in listado_libros:
                    archivo.write(libro.imprimir())
                    archivo.write('\n\n')  # Separador entre libros
            return f'Se generó el reporte de libros en el archivo: {nombre_archivo}'
        except Exception as e:
            return f'Ocurrió un error al generar el reporte de libros: {e}'


# Instancias de las clases de negocio
autor_negocio = AutorNegocio()
libro_negocio = LibroNegocio()
reporte_negocio = ReporteNegocio()

# Función para mostrar el menú principal
def mostrar_menu():
    while True:
        print("##########################")
        print("Menú Principal:")
        print("1. Autor")
        print("2. Libro")
        print("3. Generar Reporte de Libros")
        print("4. Salir")
        print("##########################")

        seleccion = input("Seleccione una opción: ")

        if seleccion == "1":
            mostrar_menu_autor()
        elif seleccion == "2":
            mostrar_menu_libro()
        elif seleccion == "4":
            generar_reporte_libros()
        elif seleccion == "5":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


# Función para mostrar el menú de opciones de Autor
def mostrar_menu_autor():
    while True:
        print("##########################")
        print("Menú Autor:")
        print("1. Registrar Autor")
        print("2. Listar Autores")
        print("3. Editar Autor")
        print("4. Eliminar Autor")
        print("5. Regresar al Menú Principal")
        print("##########################")

        seleccion = input("Seleccione una opción: ")

        if seleccion == "1":
            registrar_autor()
        elif seleccion == "2":
            listar_autores()
        elif seleccion == "3":
            editar_autor()
        elif seleccion == "4":
            eliminar_autor()
        elif seleccion == "5":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


# Función para registrar un autor
def registrar_autor():
    cod_autor = input('Ingrese código de autor: ')
    pais = input('Ingrese país del autor: ')
    editorial = input('Ingrese editorial del autor: ')

    cod_persona = input('Ingrese código de la persona que es autor: ')
    autor_nombre = input('Ingrese nombre del autor: ')
    autor_ap_paterno = input('Ingrese apellido paterno del autor: ')
    autor_ap_materno = input('Ingrese apellido materno del autor: ')
    autor_fecha_nac = input('Ingrese fecha de nacimiento del autor: ')

    autor_negocio.registrar_autor(cod_autor, pais, editorial, cod_persona, autor_ap_paterno, autor_ap_materno, autor_fecha_nac, autor_nombre)
    print(f'Registró correctamente al autor con código: {cod_autor}')


# Función para listar autores
def listar_autores():
    autores = autor_negocio.obtener_autores()
    print("Código \t Nombre \t Apellidos \t País \t Editorial")
    for autor in autores:
        print(f'{autor.codigo_autor} \t {autor.nombre} \t {autor.ap_paterno} {autor.ap_materno} \t {autor.pais} \t {autor.editorial}')


# Función para editar autor
def editar_autor():
    cod_autor = input('Ingrese el código del autor a editar: ')
    pais = input('Ingrese nuevo país del autor: ')
    editorial = input('Ingrese nueva editorial del autor: ')

    cod_persona = input('Ingrese nuevo código de la persona que es autor: ')
    autor_nombre = input('Ingrese nuevo nombre del autor: ')
    autor_ap_paterno = input('Ingrese nuevo apellido paterno del autor: ')
    autor_ap_materno = input('Ingrese nuevo apellido materno del autor: ')
    autor_fecha_nac = input('Ingrese nueva fecha de nacimiento del autor: ')

    resultado = autor_negocio.editar_autor(cod_autor, pais, editorial, cod_persona, autor_ap_paterno, autor_ap_materno, autor_fecha_nac, autor_nombre)
    print(resultado)


# Función para eliminar autor
def eliminar_autor():
    cod_autor = input('Ingrese el código del autor a eliminar: ')
    resultado = autor_negocio.eliminar_autor(cod_autor)
    print(resultado)


# Función para mostrar el menú de opciones de Libro
def mostrar_menu_libro():
    while True:
        print("##########################")
        print("Menú Libro:")
        print("1. Registrar Libro")
        print("2. Listar Libros")
        print("3. Editar Libro")
        print("4. Eliminar Libro")
        print("5. Regresar al Menú Principal")
        print("##########################")

        seleccion = input("Seleccione una opción: ")

        if seleccion == "1":
            registrar_libro()
        elif seleccion == "2":
            listar_libros()
        elif seleccion == "3":
            editar_libro()
        elif seleccion == "4":
            eliminar_libro()
        elif seleccion == "5":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


# Función para registrar un libro
def registrar_libro():
    cod_libro = input('Ingrese código de libro: ')
    titulo = input('Ingrese título del libro: ')
    año = input('Ingrese año del libro: ')
    tomo = input('Ingrese tomo del libro: ')

    cod_autor = input('Ingrese código del autor del libro: ')
    pais = input('Ingrese país del autor del libro: ')
    editorial = input('Ingrese editorial del autor del libro: ')

    cod_persona = input('Ingrese código de la persona del autor del libro: ')
    autor_nombre = input('Ingrese nombre del autor del libro: ')
    autor_ap_paterno = input('Ingrese apellido paterno del autor del libro: ')
    autor_ap_materno = input('Ingrese apellido materno del autor del libro: ')
    autor_fecha_nac = input('Ingrese fecha de nacimiento del autor del libro: ')

    autor = Autor(cod_autor, pais, editorial, cod_persona, autor_ap_paterno, autor_ap_materno, autor_fecha_nac, autor_nombre)
    libro_negocio.registrar_libro(cod_libro, titulo, año, tomo, autor)
    print(f'Registró correctamente el libro con código: {cod_libro}')


# Función para listar libros
def listar_libros():
    libros = libro_negocio.obtener_libros()
    print("Código \t Título \t Año \t Tomo \t Nombre del Autor")
    for libro in libros:
        print(f'{libro.cod_libro} \t {libro.titulo} \t {libro.año} \t {libro.tomo} \t {libro.autor.nombre}')


# Función para editar libro
def editar_libro():
    cod_libro = input('Ingrese el código del libro a editar: ')
    titulo = input('Ingrese nuevo título del libro: ')
    año = input('Ingrese nuevo año del libro: ')
    tomo = input('Ingrese nuevo tomo del libro: ')

    cod_autor = input('Ingrese nuevo código del autor del libro: ')
    pais = input('Ingrese nuevo país del autor del libro: ')
    editorial = input('Ingrese nueva editorial del autor del libro: ')

    cod_persona = input('Ingrese nuevo código de la persona del autor del libro: ')
    autor_nombre = input('Ingrese nuevo nombre del autor del libro: ')
    autor_ap_paterno = input('Ingrese nuevo apellido paterno del autor del libro: ')
    autor_ap_materno = input('Ingrese nuevo apellido materno del autor del libro: ')
    autor_fecha_nac = input('Ingrese nueva fecha de nacimiento del autor del libro: ')

    resultado = libro_negocio.editar_libro(cod_libro, titulo, año, tomo, cod_autor, pais, editorial, cod_persona, autor_ap_paterno, autor_ap_materno, autor_fecha_nac, autor_nombre)
    print(resultado)


# Función para eliminar libro
def eliminar_libro():
    cod_libro = input('Ingrese el código del libro a eliminar: ')
    resultado = libro_negocio.eliminar_libro(cod_libro)
    print(resultado)





# Función para generar el reporte de libros en un archivo de texto
def generar_reporte_libros():
    nombre_archivo = 'reporte_libros.txt'
    listado_libros = libro_negocio.obtener_libros()
    resultado = reporte_negocio.generar_reporte_libros(nombre_archivo, listado_libros)
    print(resultado)



# Iniciar la aplicación
mostrar_menu()
