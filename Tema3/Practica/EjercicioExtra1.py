def añadir_libro(libros):
    titulo = input("Introduce el título del libro: ")
    autor = input("Introduce el autor del libro: ")
    libros.append({"Titulo": titulo, "Autor": autor, "Alquilado": False})
    print(f'Libro "{titulo}" de {autor} añadido.')

def mostrar_libros(libros):
    if not libros:
        print("No hay libros en la biblioteca.")
        return
    for i, libro in enumerate(libros, start=1):
        estado = "Alquilado" if libro["Alquilado"] else "Disponible"
        print(f"{i}. {libro['Titulo']} de {libro['Autor']} - {estado}")

def buscar_libro(libros):
    titulo = input("Introduce el título del libro a buscar: ")
    encontrados = [libro for libro in libros if libro['Titulo'].lower() == titulo.lower()]
    if encontrados:
        for libro in encontrados:
            estado = "Alquilado" if libro["Alquilado"] else "Disponible"
            print(f'Encontrado: "{libro["Titulo"]}" de {libro["Autor"]} - {estado}')
    else:
        print(f'No se encontró ningún libro con el título "{titulo}".')

def eliminar_libro(libros):
    titulo = input("Introduce el título del libro a eliminar: ")
    for libro in libros:
        if libro['Titulo'].lower() == titulo.lower():
            libros.remove(libro)
            print(f'Libro "{titulo}" eliminado.')
            return
    print(f'No se encontró ningún libro con el título "{titulo}".')

def alquilar_libro(libros):
    titulo = input("Introduce el título del libro a alquilar: ")
    for libro in libros:
        if libro['Titulo'].lower() == titulo.lower():
            if not libro['Alquilado']:
                libro['Alquilado'] = True
                print(f'Libro "{titulo}" alquilado.')
            else:
                print(f'El libro "{titulo}" ya está alquilado.')
            return
    print(f'No se encontró ningún libro con el título "{titulo}".')

def devolver_libro(libros):
    titulo = input("Introduce el título del libro a devolver: ")
    for libro in libros:
        if libro['Titulo'].lower() == titulo.lower():
            if libro['Alquilado']:
                libro['Alquilado'] = False
                print(f'Libro "{titulo}" devuelto.')
            else:
                print(f'El libro "{titulo}" no estaba alquilado.')
            return
    print(f'No se encontró ningún libro con el título "{titulo}".')

libros = [
    {"Titulo": "Python Data Science Handbook", "Autor": "Jake VanderPlas", "Alquilado": False},
    {"Titulo": "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow", "Autor": "Aurélien Géron", "Alquilado": True},
    {"Titulo": "Pattern Recognition and Machine Learning", "Autor": "Christopher M. Bishop", "Alquilado": False},
    {"Titulo": "Deep Learning", "Autor": "Ian Goodfellow, Yoshua Bengio, Aaron Courville", "Alquilado": True},
    {"Titulo": "The Elements of Statistical Learning", "Autor": "Trevor Hastie, Robert Tibshirani, Jerome Friedman", "Alquilado": False},
    {"Titulo": "Data Science for Business", "Autor": "Foster Provost, Tom Fawcett", "Alquilado": False},
    {"Titulo": "Bayesian Data Analysis", "Autor": "Andrew Gelman et al.", "Alquilado": True},
    {"Titulo": "Introduction to the Theory of Computation", "Autor": "Michael Sipser", "Alquilado": False},
    {"Titulo": "Artificial Intelligence: A Modern Approach", "Autor": "Stuart Russell, Peter Norvig", "Alquilado": True},
    {"Titulo": "Computer Vision: Algorithms and Applications", "Autor": "Richard Szeliski", "Alquilado": False},
    {"Titulo": "Data Science from Scratch", "Autor": "Joel Grus", "Alquilado": True},
    {"Titulo": "The Art of Statistics", "Autor": "David Spiegelhalter", "Alquilado": False},
    {"Titulo": "Python Machine Learning", "Autor": "Sebastian Raschka, Vahid Mirjalili", "Alquilado": True},
    {"Titulo": "An Introduction to Statistical Learning", "Autor": "Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani", "Alquilado": False},
    {"Titulo": "Fundamentals of Data Engineering", "Autor": "Joe Reis, Matt Housley", "Alquilado": False},
    {"Titulo": "Storytelling with Data", "Autor": "Cole Nussbaumer Knaflic", "Alquilado": True},
    {"Titulo": "Building Machine Learning Powered Applications", "Autor": "Emmanuel Ameisen", "Alquilado": False},
    {"Titulo": "Practical Statistics for Data Scientists", "Autor": "Peter Bruce, Andrew Bruce", "Alquilado": True},
    {"Titulo": "SQL for Data Scientists", "Autor": "Renee M. P. Teate", "Alquilado": False},
    {"Titulo": "Data Engineering on Azure", "Autor": "Vlad Riscutia", "Alquilado": True}
]

while True:
    print("\nMenu Biblioteca ")
    print("1. Añadir libro")
    print("2. Mostrar libros")
    print("3. Buscar libro")
    print("4. Eliminar libro")
    print("5. Alquilar libro")
    print("6. Devolver libro")
    print("7. Salir")
    
    seleccion = input("Selecciona una opción (1-7): ")

    match seleccion:
        case "1":
            añadir_libro(libros)
        case "2":
            mostrar_libros(libros)
        case "3":
            buscar_libro(libros)
        case "4":
            eliminar_libro(libros)
        case "5":
            alquilar_libro(libros)
        case "6":
            devolver_libro(libros)
        case "7":
            print("¡Hasta luego!")
            break
        case _:
            print("Opción no válida. Por favor, elige una opción del 1 al 7.")
