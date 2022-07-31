import time

print('----------------Programa para saber si es es hora de salir del trabajo------------------')


fecha_sistema = time.localtime()

hora_sistema = fecha_sistema.tm_hour


if hora_sistema >= 15:

    print('Es hora de salir, son las ', str(hora_sistema), ' horas. Feliz noche!')

else:

    horas_restantes = 15 - hora_sistema

    print('Te faltan: ', horas_restantes, ' para irte a casa. ')
