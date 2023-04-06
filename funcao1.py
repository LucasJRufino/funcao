def anoBi(ano):
    if ano % 4 != 0:
        return False
    elif ano % 100 != 0:
        return True
    elif ano % 400 != 0:
        return False
    else:
        return True
        
dadosTeste = [1900, 2000, 2016, 1987, 2023]

resultadosReais = [False, True, True, False, False]

for i in range(len(dadosTeste)):
    yr = dadosTeste[i]
    print(yr, " -> ", end="")
    result = anoBi(yr)
    if result == resultadosReais[i]:
        print("OK")
    else:
        print("Falha")