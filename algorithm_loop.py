import comparator

# Funcion para strings completos sin mascaras de *
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

    porcentage_final = float("{:.2f}".format(sum(array_percentage_final)/len(array_percentage_final)))
    return porcentage_final



# Funcion para cuando el string 2 tiene *** en el nombre o cuando es más corto c/elemento al splitearlo
def algorithm_string_mask(input_str_1, input_str_2):
    '''
    Ejemplos de inputs:
        input_str_1 = 'Holaaloh Fedeadef'
        input_str_2 = 'Hola**** Fede****'
    '''
    str_2_list = input_str_2.split(' ')

    str_2_list_splited = []
    for item in str_2_list:
        str_2_list_splited.append(item.strip("*"))

    array_str_1 = input_str_1.split(' ')
    array_str_2 = str_2_list_splited

    # Arreglo final, donde guardo los mejores % de cada vuelta del bucle
    array_percentage_final = []

    # Comparar de a un elemento del arreglo 2 con todas las del arreglo 1 pero usando el mismo largo q contiene el string más corto
    for index_str_2 in array_str_2:
        array_percentage_intermediate = []
        for index_str_1 in array_str_1:
            index_str_1_to_compare = index_str_1[:len(index_str_2)]
            comparator_porcentage = comparator.name_comparator(index_str_2, index_str_1_to_compare)
            array_percentage_intermediate.append(float(comparator_porcentage))

        max_value = max(array_percentage_intermediate)
        
        array_percentage_final.append(float(max_value))

    porcentage_final = float("{:.2f}".format(sum(array_percentage_final)/len(array_percentage_final)))
    return porcentage_final
