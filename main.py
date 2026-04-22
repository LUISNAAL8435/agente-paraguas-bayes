from probabilidades import Probabilidades
from bayes import Bayes
from agente import AgenteParaguas

def main():
    while True:
        print("\n" + "=" * 50)
        print("=== Sistema de Decisión para Llevar Paraguas ===")
        agente = AgenteParaguas(None)
        mes, nublado = agente.percibir()
        prob = Probabilidades(mes)
        modelo = Bayes(prob)
        agente.modelo = modelo

        probabilidad = agente.decidir(mes, nublado)
        agente.actuar(probabilidad)
        print(f"Probabilidad de lluvia: {probabilidad:.2f}")
        print("*" * 50)

        continuar = input("Desea continuar? (si/no): ").strip().lower()
        if continuar != "si":
            break

if __name__ == "__main__":
    main()