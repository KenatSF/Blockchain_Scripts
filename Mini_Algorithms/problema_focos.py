

class status_focos:
    def __init__(self, on, off):
        self.on = on
        self.off = off
        self.diccionario = {i: on for i in range(1, 101)}

    def getOn(self):
        return self.on
    
    def getOff(self):
        return self.off

    def getDiccionario(self):
        return self.diccionario

    def getStatus(self, indice):
        return self.diccionario[indice]

    def changeStaus(self, indice):
        if self.diccionario[indice] == self.on:
            self.diccionario[indice] = self.off
        else:
            self.diccionario[indice] = self.on


def main():

    focos = status_focos("encendido", "apagado")

    for i in range(1, 101):
        for j in range(1, 101):
            if j%i == 0:
                focos.changeStaus(j)



    focos_encendidos = [key for key, value in focos.getDiccionario().items() if value == "encendido"]
    print("Focos encendidos")
    print(focos_encendidos)

    focos_apagados = [key for key, value in focos.getDiccionario().items() if value == "apagado"]
    print("Focos apagados:")
    print(focos_apagados)

if __name__ == "__main__":
    main()




