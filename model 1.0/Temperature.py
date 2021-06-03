def ftar(Tar, Tb, To1, To2, TB):
    global FTar
    if Tar < Tb:
        FTar = float(0)
        return FTar
    else:
        if Tar < To1:
            FTar = float((Tar - Tb) / (To1 - Tb))
            return FTar
        else:
            if Tar <= To2:
                FTar = float(1)
                return FTar
            else:
                if Tar < TB:
                    FTar = float((TB - Tar) / (TB - To2))
                    return FTar
                else:
                    FTar = float(0)
                    return FTar


def grausdia(Tar, Tb, GD=0):
    GD = GD + (float(Tar) - Tb)
    return GD