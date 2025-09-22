# Definición de la clase Tienda para gestionar información de tiendas de electrodomésticos
class Tienda :
    # Variables de clase que son comunes para todas las instancias
    tipo = "Electrodomésticos"  # Tipo de tienda
    abierta = True             # Estado de la tienda (abierta/cerrada)

    # Constructor de la clase
    def __init__(self,nombre,direccion, n_empreados, ventas):
        self.nombre = nombre           # Nombre de la tienda
        self.direccion = direccion     # Dirección física de la tienda
        self.n_empreados = n_empreados # Número de empleados
        self.ventas = ventas           # Lista de ventas

    # Propiedad que calcula el total de ventas
    @property  
    def totalVentas(self):
        return sum(self.ventas)

    # Método que calcula el promedio de ventas por empleado
    def promedioVentasXEmpleado(self):
        if 0 in self.ventas:
            return (sum(self.ventas)/len(self.ventas))/self.n_empreados - self.ventas.count(0)
        elif self.n_empreados == 0:
            return (sum(self.ventas)/len(self.ventas))/1
        else:
            return (sum(self.ventas)/len(self.ventas))/self.n_empreados

    # Método que retorna el nombre y dirección de la tienda
    def nombreYdireccion(self):
        return f" El nombre de  la tienda : {self.nombre} su direccion es {self.direccion}"

    # Propiedad que obtiene las ventas del último mes
    @property
    def ventasUltimoMes(self):
        return self.ventas[-1]

    # Método que calcula la proyección de ventas según un valor x
    def proyeccionVentas(self,x):
        if x < 1000:
            self.ventas = [i * 1.120 for i in self.ventas if isinstance(i, float)]  # Aumento del 12%
        elif 1000 <= x:
            self.ventas = [i * 1.150 for i in self.ventas if isinstance(i, float)]  # Aumento del 15%
        return self.ventas

# Creación de instancias de tiendas y pruebas de los métodos
tiendaA = Tienda("MiTienda", "Calle Falsa 123", 5, [10.00, 150.0, 200.0])
tiendaB = Tienda("OtraTienda", "Avenida Siempre Viva 456", 0, [0, 0, 0])
tiendaC = Tienda("TiendaC", "Boulevard Central 789", 3, [300.0, 400.0, 500.0, 600.0])

# Bucle que muestra las ventas del último mes de cada tienda
# y muestra el nombre y dirección si la dirección contiene "Avenida"
for i in [tiendaA, tiendaB, tiendaC]:
    print(i.ventasUltimoMes)
    if "Avenida" in i.direccion:
        print(i.nombreYdireccion())