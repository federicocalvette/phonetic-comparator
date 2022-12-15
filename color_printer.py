from colorama import init, Fore, Back, Style


def printer(input_str_1, input_str_2, porcentage, contain_mask):
    # Para restablecer colores después de cada impresión inicializar debo el módulo con init(autoreset=True) en lugar de init().
    init(autoreset=True)

    # Selecciono el color en funcion del %
    if porcentage >= 85:
        color = Fore.GREEN
    elif 70 < porcentage < 85:
        color = Fore.YELLOW
    else:
        color = Fore.RED

    # Determino el msj para el caso con o sin *. E imprimo con el color correspondiente
    if contain_mask:
        message = f'El nombre "{input_str_1}" comparado con "{input_str_2}", tiene un porcentaje de coincidencia de {color + str(porcentage) +"%"+ Fore.RESET}. Ignorando los *.'
    else:
        message = f'El nombre "{input_str_1}" comparado con "{input_str_2}", tiene un porcentaje de coincidencia de {color + str(porcentage) +"%"+ Fore.RESET}.'

    print(message + '\n')

