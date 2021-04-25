alumnos = []

while True:
    try:
        cantidad_alumnos = int(
            input('Ingresar cantidad de alumnos a ingresar: '))
        break
    except:
        print("Ingrese solo números")

for count in range(cantidad_alumnos):
    # crear objeto alumno
    alumnos.append({})
    alumno = alumnos[count]
    # asignar nombres al alumno
    alumno["nombres"] = input(f'Ingresar los nombres de alumno {count + 1}:\n')

    # asignar 5 notas al alumno
    alumno["notas"] = []
    i = 0
    while i < 5:
        try:
            alumno["notas"].append(int(input(f'Ingrese nota {i + 1}: ')))
            i += 1
        except:
            print("Ingrese sólo números")

    # calcular promedio de 5 notas
    promedio = 0
    for nota in alumno["notas"]:
        promedio += nota
    alumno["promedio"] = promedio / 5

    # calcular nota mínima y máxima
    alumno["nota_min"] = min(alumno["notas"])
    alumno["nota_max"] = max(alumno["notas"])


print(alumnos)
