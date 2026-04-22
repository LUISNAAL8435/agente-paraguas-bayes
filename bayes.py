class Bayes:
    def __init__(self, probabilidades):
        self.prob = probabilidades

    def calcular_posterior(self):
        # Numerador
        numerador = self.prob.p_nublado_dado_lluvia * self.prob.p_lluvia

        # Denominador
        denominador = (
            (self.prob.p_nublado_dado_lluvia * self.prob.p_lluvia) +
            (self.prob.p_nublado_dado_no_lluvia * self.prob.p_no_lluvia)
        )

        # Resultado
        return numerador / denominador
    def calcularNonublado_posterior(self):
        # Numerador
        numerador = self.prob.p_no_nublado_dado_lluvia * self.prob.p_lluvia

        # Denominador
        denominador = (
            (self.prob.p_no_nublado_dado_lluvia * self.prob.p_lluvia) +
            (self.prob.p_no_nublado_dado_no_lluvia * self.prob.p_no_lluvia)
        )

        # Resultado
        return numerador / denominador