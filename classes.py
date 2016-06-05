#!/usr/bin/python
# -*- coding: UTF-8 -*-
class salario(object):
    """
    Classe com métodos para calcular salário liquido de acordo com os descontos vigentes CLT.
    """
    def __init__(self,salarioBruto, numDependentes):
        super(salario,self).__init__()
        self.salarioBruto = salarioBruto
        self.numDependentes = numDependentes

    def inss(self):
        """
        Método para calcular o desconto do inss.
        :param salarioBruto: Salário Bruto a ser calculado o desconto.
        :return: Valor a ser descontado de acordo com a faixa.
        """
        if self.salarioBruto<= 1556.94:
            aliquota = 8
        elif self.salarioBruto >= 1556.95 and self.salarioBruto <= 2594.92:
            aliquota = 9
        elif self.salarioBruto >= 2594.93 and self.salarioBruto <= 5189.82:
            aliquota = 11
        else:
            aliquota = 0
        return 570.88 if aliquota == 0 else round(((self.salarioBruto*aliquota)/100),2)

    def irrf(self):
        """
        Calcula o desconto do IRRF de acordo com o salário sem INSS e de acordo com o núemro de dependentes.
        :param salarioSemInss: Salário descontado com o INSS.
        :param numDependentes: Quantidade de dependentes.
        :return: Retorna o valor a ser descontado por mês.
        """
        descontoDependente = 189.59
        salarioSemInss = self.salarioBruto - self.inss()
        if salarioSemInss > 4664.68:
            desconto = 27.5
            deducao = 869.36
        elif salarioSemInss >= 3751.06 and salarioSemInss <= 4664.68:
            desconto = 22.5
            deducao = 636.13
        elif salarioSemInss >= 2826.66 and salarioSemInss <= 3751.05:
            desconto = 15
            deducao = 354.80
        elif salarioSemInss >= 1903.99 and salarioSemInss <= 2826.65:
            desconto = 7.5
            deducao = 142.80
        else:
            desconto = 0
            deducao = 0
        return 0 if desconto == 0 else round((((salarioSemInss - (self.numDependentes*descontoDependente))*desconto)/100)-deducao,2)

    def vt(self,diasTrabalhados,passagemDiaria):
        """
        Método para calcular o valor de desconto do VT.
        :param salarioBruto: Salário bruto mensal.
        :param diasTrabalhados: Quantidade de dias trabalhados no mês.
        :param passagemDiaria: valor gasto diáriamente com passagens.
        :return: retorna o valor a ser descontado.
        """
        valorMensal = passagemDiaria * diasTrabalhados
        descontoVt = (self.salarioBruto * 6)/100
        return round(valorMensal,2) if valorMensal < descontoVt else round(descontoVt,2)

