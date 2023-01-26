import random 

#se ocupa random y se le dan las opciones a elegir
eleccionrandom=(random.choice(['piedra', 'papel' , 'tijeras']))

eleccion=input('Elija \n1-Piedra \n2-Papel  \n3-Tijeras\n')
decision= ''
while True:
    if eleccion =='1':
        decision='piedra'
        print('usted a escojido piedra ')
        print('el oponente elijio'+ eleccionrandom)
        if decision == eleccionrandom:
            print('Han empatado')
            break

        elif eleccionrandom == 'papel':
            print('has perdido')
            break

        elif eleccionrandom == 'tijeras':
            print('has ganado')
            break




    elif eleccion =='2':
        desicion='papel'
        print('usted a escojido papel ')
        print('el oponente elijio'+ eleccionrandom)
        if decision == eleccionrandom:
            print('Han empatado')
            break        
        elif eleccionrandom == 'tijeras':
            print('has perdido')
            break

        elif eleccionrandom == 'piedra':
            print('has ganado')
            break




    elif eleccion =='3':
        decision=='tijeras'
        print('usted a escojido tijeras ')
        print('el oponente elijio '+ eleccionrandom)
        if decision == eleccionrandom:
            print('Han empatado')
            break
        elif eleccionrandom == 'piedra':
            print('has perdido')
            break

        elif eleccionrandom == 'papel':
            print('has ganado')
            break       
        
        



    else:
        print('escoja una opcion correcta')
        break


