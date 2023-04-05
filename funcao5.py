def fahrenheitCelsius(tempF):
    tempC = (tempF - 32) * 5 / 9
    return tempC

tempF = 75
tempC = fahrenheitCelsius(tempF)

print(tempF, "Graus equivalem a ", tempC, " graus Celsius" )
print(tempF, "Graus equivalem a ", round(tempC, 1), " graus Celsius arrendondados" )