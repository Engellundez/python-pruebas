ingreso_mensual = 72000
gasto_mensual = 80000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual > 3000:
        print("bien pa, estas bien")
    elif  ingreso_mensual - gasto_mensual < 0:
        print ("Estás en deficit")
    else:
        print ("y pa, estas gastando un chingo, veremos si comes.")
    
elif ingreso_mensual > 1000:
    print("Estás bien en Latinoamérica")
    
    
elif ingreso_mensual > 500:
    print("Estás bien en Argentina")
    
    
elif ingreso_mensual > 200:
    print("Estás bien en Venezuela")
    
else:
    print("Eres pobre :(")