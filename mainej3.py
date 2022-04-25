from manejadorbidimensional import manejador


if __name__ == '__main__':

    unmanejador= manejador()
    unmanejador.cargarListaCamion()
    unmanejador.cargarlistacosecha()
    op=0
    while op!=-1:
        print('1-mostrar cantidad de kgs deacargados')
        print('2-mostrar lista dia')
        print('-1-ingrese -1 para finalizar')
        op=int(input('\n seleccione una opcion'))
        if(op == 1):
            id = int(input('ingrese ID del camionero: '))
            if(id>=1 and id<=20):
                print('Cantidad de kilos descargados: {}kgs'.format(unmanejador.mostrarkilos(id-1)))
            else: print(' id incorrecta')
        if(op == 2):  #mostrar lista día
            dia = int(input('\nElegir día de la semana(numero correspondiente del 1 al 7 ):'))
            if(dia>=1 and dia<=7):
                unmanejador.mostrardia(dia-1)


            else: print(' día incorrecto')



