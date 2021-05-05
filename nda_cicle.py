from datetime import date

# data de semeadura
dia = 12
mes = 10
ano = 2020

sow_nda = int(date(ano,mes,dia).strftime('%j'))
cicle_length = 150 # total de dias do ciclo da cultura

c_data = open('piedade_climate_data.csv')

def nda_cicle(sow_nda, cicle_length): # Função que cria o ciclo com o NDA de cada dia
    global cicle
    cicle = []
    while cicle_length != 0:
        cicle.append(sow_nda)
        sow_nda = sow_nda + 1
        cicle_length = cicle_length - 1
        if sow_nda > 365:
            sow_nda = 1
        else:
            pass
    return cicle