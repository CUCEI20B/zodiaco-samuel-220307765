dia = int(input("Ingresa tu dia de nacimiento\t"))
mes = int(input("Ingresa tu mes de nacimiento\t"))

if  (mes==1 and dia >=20) or (mes==2 and dia<=18):
    print("Tu signo es Acuario")
elif (mes==2 and dia >=19) or (mes==3 and dia<=20):
    print("Tu signo es Piscis")
elif (mes==3 and dia >=21) or (mes==4 and dia<=19):
    print("Tu signo es Aries")
elif (mes==4 and dia >=20) or (mes==5 and dia<=20):
    print("Tu signo es Tauro")
elif (mes==5 and dia >=21) or (mes==6 and dia<=20):
    print("Tu signo es Geminis")
elif (mes==6 and dia >=21) or (mes==7 and dia<=22):
    print("Tu signo es Cancer")
elif (mes==7 and dia >=23) or (mes==8 and dia<=22):
    print("Tu signo es Leo")
elif (mes==8 and dia >=23) or (mes==9 and dia<=22):
    print("Tu signo es Virgo")
elif (mes==9 and dia >=23) or (mes==10 and dia<=22):
    print("Tu signo es Libra")
elif (mes==10 and dia >=23) or (mes==11 and dia<=21):
    print("Tu signo es Escorpion")
elif (mes==11 and dia >=22) or (mes==12 and dia<=21):
    print("Tu signo es Sagitario")
elif (mes==12 and dia >=22) or (mes==1 and dia<=19):
    print("Tu signo es Capricornio")