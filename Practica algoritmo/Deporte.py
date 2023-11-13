# sep=" " end=" "
# Programa para calcular los programa de estado a diferentes deportista
# calculo y se guarde en la varible 
becario= 500*0.975 
junior = 500-800*0.1525
senior = 800-1000*0.2050
bajored = 1000-1500*0.2530;
altored = 1500 * 0.3500;
#opciones del menu
print("\nSeleccione una opción: \n")
#Menú
print ("1.Becarios\n2.Junior\n3.Senior\n4.Bajo Rendimiento\n5.Alto Redimiento\n")
# La entrada por teclado de un numero
menu = int(input("¿Cuál opcion?: "))
# construcion de menú usando condicionales 
if(menu == 1 ):
    #
    print("\n El incremento aplicado al Becario es: ",round (becario,2))
elif(menu == 2):
    #
    print("\n El incremento aplicado al Junior es: ",round(junior,2))
elif(menu == 3):
    #
    print("\n El incremento aplicado al Senior es: ",round(senior,2))
elif(menu == 4):
    #
    print("\n El incremento aplicado al de Bajo Rendimiento es: ",round(bajored,2))
elif (menu == 5):
    #
    print("\n El incremento aplicado al de Alto Redimiento es: ",round(altored,2))
else :
    print("\n salir de menu")
# varible que almacena el resultado
resultmes= (0.975+0.1525+0.2050+0.2530+0.3500)*31
resultano= resultmes*365
totalmes= (becario+junior+senior+bajored+altored)*31 
totalano= (becario+junior+senior+bajored+altored)*365 
# se manda imprimir el resultado de las variable 
# se usa round para rendondiar la cifra  sinificativas
print("\n El total de incremento por mes es: ", round( resultmes,2))
print("\n El total de incremento por ano es: ",round( resultano,2))
print("\n El total de alteta que beneficia de PAN DEPORTE al mes es: ",round( totalmes,2))
print("\n El total de alteta que beneficia de PAN DEPORTE al ano es: ",round (totalano,2))

print ("\n Fin del programa\n") 
  


