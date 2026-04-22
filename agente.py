class AgenteParaguas:
    def __init__(self, modelo_bayes):
        self.modelo = modelo_bayes

    def percibir(self):
            while True:
                mes = input("Introduce el mes: ").strip().lower()
                if mes in ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]:
                    break
                else:
                    print("Mes no válido. Intenta de nuevo.")
            while True:
                respuesta = input("¿El cielo está nublado? (si/no): ").strip().lower()
                if respuesta in ["si", "no"]:
                    nublado =  respuesta== "si"
                    return mes, nublado
                else:
                    print("Respuesta no válida. Intenta de nuevo.")

    def decidir(self, mes, nublado):
        if nublado:
            prob_lluvia = self.modelo.calcular_posterior()
            return prob_lluvia
        else:
            prob_lluvia = self.modelo.calcularNonublado_posterior()
            return prob_lluvia
            

    def actuar(self, probabilidad):
        if probabilidad > 0.5:
            print("Llevar paraguas")
        else:
            print("No llevar paraguas")