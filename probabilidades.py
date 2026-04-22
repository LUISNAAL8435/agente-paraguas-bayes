class Probabilidades:
    def __init__(self, mes):
        self.prob_lluvia_por_mes = {
            "enero": 0.1,
            "febrero": 0.1,
            "marzo": 0.2,
            "abril": 0.3,
            "mayo": 0.5,
            "junio": 0.7,
            "julio": 0.8,
            "agosto": 0.8,
            "septiembre": 0.7,
            "octubre": 0.5,
            "noviembre": 0.3,
            "diciembre": 0.2
        }
        # Probabilidades base
        self.p_lluvia = self.prob_lluvia_por_mes[mes]
        self.p_no_lluvia = 1 - self.p_lluvia

        # Probabilidades condicionales
        # P(nublado | lluvia) y P(nublado | no lluvia)
        self.p_nublado_dado_lluvia = 0.9
        self.p_nublado_dado_no_lluvia = 0.4

        # P(No nublado | lluvia) y P(No nublado | no lluvia)
        self.p_no_nublado_dado_lluvia = 1 - self.p_nublado_dado_lluvia # 0.1
        self.p_no_nublado_dado_no_lluvia = 1 - self.p_nublado_dado_no_lluvia # 0.6
        