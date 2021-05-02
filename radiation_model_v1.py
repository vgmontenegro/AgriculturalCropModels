from math import sin, cos, radians, degrees, exp, acos, tan, pi
from datetime import date

# Variáveis de entrada
# IAF considerado fixo/médio para a cultura do milho; k e RUE são para a cultura do milho
jo = 118.11
lat = -23.0808 # Piedade/SP
iaf = 3.48
k = 0.61
RUE = 3.85

# data de semeadura
dia = 12
mes = 10
ano = 2020

sow_nda = int(date(ano,mes,dia).strftime('%j'))
cicle_length = 150 # total de dias do ciclo da cultura

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

def RadSol_ET(lat, nda): # Fórmula da radiação solar extraterrestre
    declsol_v = 23.45 * sin(radians((360 * (nda - 80)) / 365)) # Fórmula da declinação solar
    hn = degrees(acos(-tan(radians(lat)) * tan(radians(declsol_v)))) # Fórmula do ângulo horário do nascer do sol
    varrad_v = 1 + 0.033 * cos(radians(nda * 360 / 365)) # Fórmula da correção devido a elipse da terra entorno do sol (d/D)>02
    qo = (jo / pi) * varrad_v * ((pi / 180) * hn * sin(radians(lat)) * sin(radians(declsol_v)) + cos(radians(lat)) * cos(radians(declsol_v)) * sin(radians(hn)))
    return qo

def absPAR(par, k, iaf, r=0): # Fórmula que calcula o aPAR a partir da PAR, K e IAF
    aPAR = (par) * (1 - r - exp(-k * iaf))
    return aPAR

TotalBiomass = 0
nda_cicle(sow_nda, cicle_length)# criando ciclo

# Cálculo dos resultados
for dia in cicle:
    qo = RadSol_ET(lat, dia)                    # Calcular Qo
    par = qo/4                                  # Estimar par = qg/2 = qo/4
    aPAR = absPAR(par,k,iaf)                    # Estimar aPAR
    BiomassRate = aPAR * RUE                    # Estimar BR
    TotalBiomass = TotalBiomass + BiomassRate   # Biomassa total

# Resultados

print("Total Biomass    |  {:>07.2f} kg/ha".format(TotalBiomass*10))