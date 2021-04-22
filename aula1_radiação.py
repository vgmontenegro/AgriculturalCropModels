from math import sin, cos, radians, degrees, exp, acos, tan, pi

# Variáveis de entrada
lat = -28.0808
jo = 118.11
iaf = 3
k = 0.61
RUE = 3.85
nda = 200

# Fórmula do ângulo horário do nascer do sol
def anghor(lat, declsol_v):
    anghor_v = degrees(acos(-tan(radians(lat))*tan(radians(declsol_v))))
    return anghor_v

# Fórmula da declinação solar
def declsol(nda):
    declsol_v = 23.45 * sin(radians((360 * (nda - 80)) / 365))
    return declsol_v

# Fórmula da correção devido a elipse da terra entorno do sol (d/D)^2
def varrad(nda):
    varrad_v = 1 + 0.033 * cos(radians(nda * 360 / 365))
    return varrad_v

# Fórmula da radiação solar extraterrestre
def RadSol_ET(hn, lat, declsol_v, nda):
    varrad_v = 1 + 0.033 * cos(radians(nda * 360 / 365))
    qo = (jo / pi) * varrad_v * ((pi / 180) * hn * sin(radians(lat)) * sin(radians(declsol_v)) + cos(radians(lat)) * cos(radians(declsol_v)) * sin(radians(hn)))
    return qo

def absPAR(par, k, iaf, r=0):
    aPAR = (par) * (1 - r - exp(-k * iaf))
    return aPAR

# Calcular declinação solar
declsol_v = declsol(nda)
print("Ds: ", round(declsol_v, 2), "º")
# Calcular angulo horario do nascer do sol (hn)
hn = anghor(lat, declsol_v)
print("hn: ", round(hn, 2), "º")

# Calcular Qo
qo = RadSol_ET(hn, lat, declsol_v, nda)
print("Qo:", round(qo, 2), "MJ/m2.dia")

# Estimar PAR
#    K, IAF;
# par = qg/2 = qo/4
par = qo/4
aPAR = absPAR(par,k,iaf)
print("aPAR: ", round(aPAR, 2), "MJ/m2.dia")

# Estimar BR
BiomassRate = aPAR * RUE
print("Biomass Rate: ", round(BiomassRate, 2), "g/m2.dia")
