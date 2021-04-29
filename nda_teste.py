from datetime import date

# data de semeadura

dia = 12
mes = 10
ano = 2020
sow_nda = int(date(ano,mes,dia).strftime('%j'))
print(sow_nda)
