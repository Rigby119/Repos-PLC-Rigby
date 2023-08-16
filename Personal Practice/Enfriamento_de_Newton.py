import math

t_max=float(input("Dame la temperatura máxima: "))
t_a=float(input("\nDame la temperatura ambiente: "))
const=t_max-t_a
tiempo_1=float(input("\nDame un dato cualquiera\n\nTiempo: "))
temp_1=float(input("\nTemperatura: "))
const_k=(math.log(((temp_1-t_a)/const),math.e))/(-tiempo_1)

time_values=[]
temp_values=[]

data=int(input("\n¿Cuántos datos hay disponibles?\n\n>>> "))

for i in range(0, data):
    time_values.append(float(input("\nDame el tiempo #"+str(i+1))))

for i in time_values:
    result=const*(math.exp(-1*const_k*i))+t_a
    temp_values.append(result)

print(f"Los datos del tiempo son los siguientes:\n{time_values}\n\nLos datos de la temperatura son los siguientes:\n{temp_values}")