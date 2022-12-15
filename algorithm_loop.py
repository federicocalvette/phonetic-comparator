import comparator

input_str_1 = 'Hpla Fede q'
input_str_2 = 'Hola Aede q'


# Strings s/* o tmbn llamado completo, ya que no tiene mask en el nombre
def algorithm_string_complete(input_str_1, input_str_2):
    # Arreglos
    array_str_1 = input_str_1.split(' ')
    array_str_2 = input_str_2.split(' ')

    # Arreglo final, donde guardo los mejores % de cada vuelta del bucle
    array_percentage_final = []

    # Comparar de a un elemento del arreglo 1 con todas las del arreglo 2
    for index_str_1 in array_str_1:
        array_percentage_intermediate = []

        for index_str_2 in array_str_2:
            comparator_porcentage = comparator.name_comparator(index_str_1, index_str_2)
            array_percentage_intermediate.append(float(comparator_porcentage))

        max_value = max(array_percentage_intermediate)

        array_percentage_final.append(float(max_value))

    print(array_percentage_final)
    porcentage_final = float("{:.2f}".format(sum(array_percentage_final)/len(array_percentage_final)))
    print(porcentage_final)

    return porcentage_final




