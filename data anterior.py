dia = input("Escreva o dia de hoje")
mes = input("Escreva o mês")
ano = input("Escreva o ano")
print(dia,mes,ano)

dia = int(dia)
ano = int(ano)
dia = dia - 1

if dia == 0 and mes == "janeiro":
   dia = 31
   mes = "dezembro"
   ano = ano -1

if dia == 0 and mes == "fevereiro":
   dia = 31
   mes = "janeiro"

if mes == "março" and dia == 0:
   mes = "fevereiro"
   dia = 28

if mes == "abril" and dia == 0:
   mes = "março"
   dia = 31

if mes == "maio" and dia == 0:
   mes = "abril"
   dia = 31

if mes == "junho" and dia == 0:
   mes = "maio"
   dia = 31

if mes == "julho" and dia == 0:
   mes = "junho"
   dia = 30

if mes == "agosto" and dia == 0:
   mes = "julho"
   dia = 31

if mes == "setembro" and dia == 0:
   mes = "agosto"
   dia = 31

if mes == "outubro" and dia == 0:
   mes = "setembro"
   dia = 30

if mes == "novembro" and dia == 0:
   mes = "outubro"
   dia = 31

if mes == "dezembro" and dia == 0:
   mes = "novembro"
   dia = 30

print("Ontem foi: ",dia, mes, ano)

