import algorithm_loop

if __name__ == '__main__':
    
    '''
        Nota interna:
            String 1 > debe ser el completo.
            String 2 > debe ser el que esta enmascarado o incompleto.
    '''

    input_str_1 = input("Ingrese el primer string: ")
    input_str_2 = input("Ingrese el segundo string: ")
    print('\nComparando...\n')


    #Controlar el llamado al algorithm en funcion de que tan completo es el input string 2
    if "*" in input_str_2:
        porcentage = algorithm_loop.algorithm_string_mask(input_str_1=input_str_1, input_str_2=input_str_2)
        message = f'El nombre "{input_str_1}" comparado con "{input_str_2}", tiene un porcentaje de coincidencia de {porcentage}%. Ignorando los *.'
    else:
        porcentage = algorithm_loop.algorithm_string_complete(input_str_1=input_str_1, input_str_2=input_str_2)
        message = f'El nombre "{input_str_1}" comparado con "{input_str_2}", tiene un porcentaje de coincidencia de {porcentage}%.'

    print(message)