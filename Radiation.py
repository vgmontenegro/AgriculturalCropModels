from math import sin, cos, radians, degrees, exp, acos, tan, pi, sqrt


def radsol_et(lat, nda):  # Fórmula da radiação solar extraterrestre
    jo = 118.11
    declsol_v = 23.45 * sin(radians((360 * (nda - 80)) / 365))  # Fórmula da declinação solar
    hn = degrees(acos(-tan(radians(lat)) * tan(radians(declsol_v))))  # Fórmula do ângulo horário do nascer do sol
    varrad_v = 1 + 0.033 * cos(radians(nda * 360 / 365))  # Fórmula da correção devido a elipse da terra entorno do sol (d/D)>02
    qo = (jo / pi) * varrad_v * ((pi / 180) * hn * sin(radians(lat)) * sin(radians(declsol_v)) + cos(radians(lat)) * cos(radians(declsol_v)) * sin(radians(hn)))
    return qo


def radsol_gb(qo, tmax, tmin, kt=0.16):
    qg = kt*qo*sqrt(tmax-tmin)
    return qg


def abspar(qg, k, iaf, r=0):  # Fórmula que calcula o aPAR a partir da PAR, K e IAF
    par = qg/2
    apar = par * (1 - r - exp(-k * iaf))
    return apar