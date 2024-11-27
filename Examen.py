class Calificaciones:
    def __init__(self):
        self.alumnos = []

    def agregar_alumno(self):
        nombre = input("Ingrese el nombre del estudiante: ")
        matricula = input(f"Ingrese la matrícula de {nombre}: ")
        materias = int(input(f"Ingrese la cantidad de materias aprobadas de {nombre}: "))
        promedio = float(input(f"Ingrese el promedio de {nombre}: "))
        self.alumnos.append({"nombre": nombre, "matricula": matricula, "materias": materias, "promedio": promedio})
        print(f"Alumno {nombre} agregado a la lista de calificaciones.\n")

    def seleccion_nombres(self):
        for i in range(len(self.alumnos)):
            min_idx = i
            for j in range(i + 1, len(self.alumnos)):
                if self.alumnos[j]["nombre"] < self.alumnos[min_idx]["nombre"]:
                    min_idx = j
            self.alumnos[i], self.alumnos[min_idx] = self.alumnos[min_idx], self.alumnos[i]
        self.mostrar_alumnos("Orden por selección (nombres)")

    def quicksort_materias(self, inicio, fin):
        if inicio < fin:
            pivote_idx = self.particionar(inicio, fin)
            self.quicksort_materias(inicio, pivote_idx - 1)
            self.quicksort_materias(pivote_idx + 1, fin)

    def particionar(self, inicio, fin):
        pivote = self.alumnos[fin]["materias"]
        i = inicio - 1
        for j in range(inicio, fin):
            if self.alumnos[j]["materias"] < pivote:
                i += 1
                self.alumnos[i], self.alumnos[j] = self.alumnos[j], self.alumnos[i]
        self.alumnos[i + 1], self.alumnos[fin] = self.alumnos[fin], self.alumnos[i + 1]
        return i + 1

    def mostrar_alumnos(self, metodo):
        print(f"\n{metodo} - Lista de alumnos:")
        for alumno in self.alumnos:
            print(f"Nombre: {alumno['nombre']}, Matrícula: {alumno['matricula']}, "
                  f"Materias aprobadas: {alumno['materias']}, Promedio: {alumno['promedio']}")
        print("\n")

escuela = Calificaciones()

while True:
    opcion = input(
        "Lista de alumnos:\n"
        "1. Agregar un alumno\n"
        "2. Ordenar alfabéticamente por nombres (selección directa)\n"
        "3. Ordenar por materias aprobadas (Quicksort)\n"
        "4. Salir\n"
        "Seleccione una opción: ")
    
    if opcion == "1":
        escuela.agregar_alumno()
    elif opcion == "2":
        escuela.seleccion_nombres()
    elif opcion == "3":
        if len(escuela.alumnos) > 0:
            escuela.quicksort_materias(0, len(escuela.alumnos) - 1)
            escuela.mostrar_alumnos("Orden por Quicksort (materias aprobadas)")
        else:
            print("No hay alumnos registrados para ordenar.\n")
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Intente nuevamente.\n")
