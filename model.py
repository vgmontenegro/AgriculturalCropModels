from datetime import date
import Radiation
import Temperature

# Variáveis de entrada

# data de semeadura
(dia, mes, ano) = [30, 12, 2019]
sow_nda = int(date(ano, mes, dia).strftime('%j'))
lat = -22.7083  # Piracicaba/SP

# IAF considerado fixo/médio para a cultura do milho; k e RUE são para a cultura do milho
iaf = 3.48
k = 0.61
RUE = 3.85
IC = 0.5           # verificar
GD_mat = 900+1800  # Graus dia para a maturação / GD_florecimento + GD_florescimento_a_maturação
(Tb, To1, To2, TB) = [6, 26, 34, 40]

# Abrindo arquivo de dados, definindo variáveis para o inicio e iniciano cálculos
c_data = open('piracicaba_climate_data.csv')
(BR, GD, TotalBiomass, cicle) = [0, 0, 0, 0]

# cálculo do BR diário e somando ao TotalBiomass
for line in c_data:
    c = {}
    (c['ano'], c['nda'], c['tmin'], c['tmax'], c['tmed']) = line.split(sep=',')
    (nda, tmin, tmax, Tar) = (int(c['nda']), float(c['tmin']), float(c['tmax']), float(c['tmed']))
    if int(c['ano']) >= ano and nda >= sow_nda:
        sow_nda = 1
        GD = GD + Temperature.grausdia(Tar, Tb)
        if GD > GD_mat:  # para a contagem quando GD chega ao determinado para a maturação da cultura
            break
        else:
            qo = Radiation.radsol_et(lat, nda)
            qg = Radiation.radsol_gb(qo, tmax, tmin)
            apar = Radiation.abspar(qg, k, iaf)
            ftar = Temperature.ftar(Tar, Tb, To1, To2, TB)
            BR = apar * ftar * RUE * IC
            TotalBiomass = TotalBiomass + BR
            cicle = cicle + 1
    else:
        pass

print("Yield            |  {:>07.2f} kg/ha".format(TotalBiomass*10))
print("Cicle Lenght     |  {:>8d}   days".format(cicle))