import pandas as pd

def carregar_frases(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        return [linha.strip() for linha in f.readlines() if linha.strip()]

def identificar_sintomas(frase, mapa):
    frase = frase.lower()
    sintomas = []
    doencas = []

    for _, row in mapa.iterrows():
        s1 = str(row["sintoma_1"]).lower()
        s2 = str(row["sintoma_2"]).lower()
        doenca = row["doenca_associada"]

        if s1 in frase:
            sintomas.append(row["sintoma_1"])
            doencas.append(doenca)

        if s2 in frase:
            sintomas.append(row["sintoma_2"])
            doencas.append(doenca)

    if doencas:
        diagnostico = pd.Series(doencas).value_counts().idxmax()
    else:
        diagnostico = "Sem diagnóstico"

    return sintomas, diagnostico

def main():
    frases = carregar_frases("data/sintomas_pacientes.txt")
    mapa = pd.read_csv("data/mapa_conhecimento_sintomas_doencas.csv")

    for frase in frases:
        sintomas, diagnostico = identificar_sintomas(frase, mapa)
        print("\n" + "=" * 80)
        print("Frase:", frase)
        print("Sintomas:", sintomas if sintomas else "Nenhum identificado")
        print("Diagnóstico:", diagnostico)

if __name__ == "__main__":
    main()
