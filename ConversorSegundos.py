segundos = int(input("Digite o valor em segundos que deseja converter "))

dias = segundos // 86400 #descobrir Dias
resto_dias = segundos % 86400 #descobrir o restante segundosXdias

horas = resto_dias // 3600 #descobrir horas
resto_horas = resto_dias % 3600 #descobrir o restante dos horasXminutos

minutos = resto_horas // 60 #descobrir Minutos
resto_minutos = resto_horas % 60 #descobre segundos

print(dias,"Dias",horas,"Horas",minutos,"Minutos",resto_minutos,"Segundos")
