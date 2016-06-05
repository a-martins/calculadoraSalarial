#!/usr/bin/python
# -*- coding: UTF-8 -*-
from classes import salario

salarioBruto = input("Informe o salário Bruto: ")
numDependentes = input("Informe o número de dependentes: ")
salario1 = salario(salarioBruto,numDependentes)
calcVt = input("Descontar vale-transporte (S/N)? ")

vt = 0.00
if calcVt == 'S':
    dias = input("Quantidade de dias trabalhados: ")
    valDiario = input("Valor diário de passagem: ")
    vt = salario1.vt(dias,valDiario)

outrosValores = 0.00
while True:
    continua = input("Descontar oustros valores (S/N)? ")
    if continua == "S":
        outrosValores += input("Informe outros descontos: ")
    else:
        break

inss = salario1.inss()
irrf = salario1.irrf()

print("Salário bruto: R$"+str(salarioBruto))
print("Desconto INSS: R$"+str(inss))
print("Desconto IRRF: R$"+str(irrf))
if calcVt == "S":
    print("Desconto VT: R$"+str(vt))
print("Outros descontos: R$"+str(outrosValores))
print("Salário líquido: R$"+str(salarioBruto-inss-irrf-vt-outrosValores))