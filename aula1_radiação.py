from math import sin, cos, radians, degrees, exp, acos, tan, pi

# Variáveis de entrada
# IAF considerado fixo/médio para a cultura do milho; k e RUE são para a cultura do milho
lat = -28.0808
jo = 118.11
iaf = 3.48
k = 0.61
RUE = 3.85

sow_nda = 200 # data de semeadura
cicle_length = 120 # total de dias do ciclo da cultura

# Função que cria o ciclo com o NDA de cada dia
def nda_cicle(sow_nda, cicle_length):
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


# Fórmula da radiação solar extraterrestre
def RadSol_ET(lat, nda):
    declsol_v = 23.45 * sin(radians((360 * (nda - 80)) / 365)) # Fórmula da declinação solar
    hn = degrees(acos(-tan(radians(lat)) * tan(radians(declsol_v)))) # Fórmula do ângulo horário do nascer do sol
    varrad_v = 1 + 0.033 * cos(radians(nda * 360 / 365)) # Fórmula da correção devido a elipse da terra entorno do sol (d/D)>02
    qo = (jo / pi) * varrad_v * ((pi / 180) * hn * sin(radians(lat)) * sin(radians(declsol_v)) + cos(radians(lat)) * cos(radians(declsol_v)) * sin(radians(hn)))
    return qo

def absPAR(par, k, iaf, r=0):
    aPAR = (par) * (1 - r - exp(-k * iaf))
    return aPAR

TotalBiomass = 0
nda_cicle(sow_nda, cicle_length)

# Cálculo dos resultados
for dia in cicle:
    qo = RadSol_ET(lat, dia)                    # Calcular Qo
    par = qo/4                                  # Estimar par = qg/2 = qo/4
    aPAR = absPAR(par,k,iaf)                    # Estimar aPAR
    BiomassRate = aPAR * RUE                    # Estimar BR
    TotalBiomass = TotalBiomass + BiomassRate   # Biomassa total

# Resultados

print("Total Biomass    |  {:>07.2f} kg/ha".format(TotalBiomass*10))