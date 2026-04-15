# FIAP - Faculdade de Informática e Administração Paulista  

<p align="center">
<a href="https://www.fiap.com.br/">
<img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width="40%">
</a>
</p>

<br>

# 2TIAOA

![Python](https://img.shields.io/badge/python-3.9-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-NLP-green)
![Healthcare](https://img.shields.io/badge/Healthcare-CardioIA-red)
![NLP](https://img.shields.io/badge/NLP-Diagnóstico-purple)
![Status](https://img.shields.io/badge/Status-Fase%202-orange)

## Fase 2 -- Capítulo 1

### Cap 1 - Desafio Integrador: IA entre Robôs, Sinapses e Medicina  
### Diagnóstico Automatizado – IA no Estetoscópio Digital

---

## 👨‍🎓 Integrante do Grupo 93

- **Deivisson Gonçalves Lima** -- RM565095  
- Email: deivisson.engtele@gmail.com  
- LinkedIn: https://www.linkedin.com/in/deivissonlima  

---

## 👩‍🏫 Professores

### Tutor
- Caique Nonato da Silva Bezerra  

### Coordenador
- André Godoi Chiovato  

---

## 📜 Descrição

Este projeto faz parte do programa de aprendizagem baseada em projetos (**PBL - Problem Based Learning**) do curso de Inteligência Artificial da FIAP e dá continuidade ao ecossistema **CardioIA**, iniciado na Fase 1.

Se na etapa anterior o foco esteve na organização e preparação de dados cardiológicos, nesta fase o objetivo evolui para a construção de uma solução de **diagnóstico automatizado assistido por Inteligência Artificial**, simulando o funcionamento de sistemas de apoio clínico utilizados em centros de diagnóstico modernos.

A proposta desta entrega é reproduzir, de forma prática e didática, como sistemas computacionais podem interpretar relatos textuais de pacientes, identificar sintomas relevantes, associá-los a possíveis doenças cardiovasculares e classificar o nível de risco clínico descrito em frases curtas.

---

## 🏥 Contexto Clínico e Justificativa

Na rotina médica, especialmente em triagens e atendimentos iniciais, grande parte da análise começa a partir do **relato textual do paciente**. Frases como:

> “Estou com dor no peito há dois dias e sinto falta de ar ao subir escadas.”

carregam sinais clínicos importantes, mas aparecem em formato **não estruturado**, exigindo interpretação e associação com conhecimento médico.

Nesta fase, o projeto CardioIA busca simular justamente essa primeira camada de inteligência, por meio de duas frentes:

1. **Extração de sintomas e sugestão diagnóstica baseada em regras**  
2. **Classificação automatizada do nível de risco com Machine Learning**

Os sintomas e associações utilizados foram escolhidos com base em exemplos comuns no contexto cardiovascular, como:

- **Dor no peito / aperto no tórax** → possível associação com **Infarto**
- **Cansaço constante / fadiga** → possível associação com **Insuficiência Cardíaca**
- **Falta de ar / dificuldade para respirar** → possível associação com **Angina**
- **Palpitações / coração acelerado** → possível associação com **Arritmia**

Essa estrutura não substitui avaliação médica real, mas demonstra como sistemas computacionais podem atuar como apoio à decisão em fluxos de triagem.

---

## 🎯 Objetivo Geral da Fase

Desenvolver uma solução prática capaz de:

- Ler frases médicas simuladas contendo sintomas relatados por pacientes
- Identificar expressões associadas a sinais clínicos
- Relacionar sintomas a possíveis diagnósticos com base em um mapa de conhecimento
- Classificar automaticamente frases em **alto risco** ou **baixo risco**
- Refletir sobre limitações, qualidade dos dados e viés em aplicações de IA na saúde

---

## 🧠 Arquitetura Conceitual da Solução

```text
Paciente → Relato textual de sintomas
                │
                ▼
        Pré-processamento de texto
                │
                ▼
     Extração de sintomas por regras
                │
                ▼
    Mapa de conhecimento (CSV)
                │
                ▼
     Sugestão de diagnóstico
                │
                ▼
   Vetorização textual com TF-IDF
                │
                ▼
 Modelo de Machine Learning
                │
                ▼
 Classificação do risco clínico
        (alto risco / baixo risco)
```

---

## 📁 Estrutura de Pastas

A estrutura do repositório foi organizada da seguinte forma:

```text
cardioia-fase2-diagnostico-automatizado
│
├── README.md
├── requirements.txt
│
├── assets
│   ├── logo-fiap.png
│   └── arquitetura_fase2_cardioia.png
│
├── data
│   ├── sintomas_pacientes.txt
│   ├── mapa_conhecimento_sintomas_doencas.csv
│   └── frases_risco_rotuladas.csv
│
├── notebooks
│   ├── parte1_extracao_sintomas.ipynb
│   ├── parte1_extracao_sintomas_ajustado.ipynb
│   ├── parte2_classificador_risco.ipynb
│   └── parte2_classificador_risco_ajustado.ipynb
│
├── scripts
│   ├── parte1_extracao_sintomas.py
│   └── parte2_classificador_risco.py


```

### Descrição das pastas

- **assets**  
  Contém arquivos visuais do projeto, como o logotipo institucional da FIAP e a arquitetura conceitual da solução.

- **data**  
  Armazena os dados textuais estruturados e não estruturados utilizados na Fase 2, incluindo frases de pacientes, mapa de conhecimento e dataset rotulado para classificação.

- **notebooks**  
  Contém os notebooks Jupyter desenvolvidos para execução e demonstração das duas partes da atividade, incluindo versões ajustadas para compatibilidade com Google Colab.

- **scripts**  
  Contém a implementação em Python das duas partes do projeto: extração de sintomas e classificação de risco.

- **README.md**  
  Documento principal com descrição, estrutura, execução e documentação geral da entrega.

---

## 🔍 Parte 1 -- Extração de Sintomas e Sugestão de Diagnóstico

Nesta etapa, foi desenvolvida uma solução baseada em regras simples de associação textual.

### Entregáveis desta parte

- Arquivo `.txt` com 10 frases simulando relatos de pacientes
- Arquivo `.csv` com mapa de conhecimento entre sintomas e doenças
- Código em Python / Notebook para leitura, identificação e sugestão diagnóstica

### Arquivos utilizados

- `data/sintomas_pacientes.txt`
- `data/mapa_conhecimento_sintomas_doencas.csv`
- `scripts/parte1_extracao_sintomas.py`
- `notebooks/parte1_extracao_sintomas.ipynb`

### Estratégia utilizada

A lógica aplicada consiste em:

1. Ler frases completas com sintomas relatados pelos pacientes
2. Comparar o conteúdo textual com um mapa de conhecimento previamente estruturado
3. Identificar sintomas presentes por correspondência textual
4. Sugerir um possível diagnóstico com base na doença associada aos sintomas encontrados

### Exemplo de funcionamento

**Frase de entrada:**  
`"Estou com dor no braço esquerdo junto com pressão no peito."`

**Sintomas identificados:**  
- dor no braço esquerdo  
- pressão no peito  

**Diagnóstico sugerido:**  
- Infarto

---

## 🤖 Parte 2 -- Classificador Básico de Texto

Nesta etapa, foi implementado um classificador supervisionado para analisar frases médicas e prever o nível de risco clínico.

### Entregáveis desta parte

- Arquivo `.csv` com frases rotuladas
- Notebook com TF-IDF, treinamento e avaliação
- Repositório GitHub público com documentação
- Vídeo demonstrativo da solução

### Arquivos utilizados

- `data/frases_risco_rotuladas.csv`
- `scripts/parte2_classificador_risco.py`
- `notebooks/parte2_classificador_risco.ipynb`

### Pipeline utilizado

1. Leitura do dataset rotulado
2. Transformação de texto em vetor numérico com **TF-IDF**
3. Separação entre treino e teste
4. Treinamento com **Logistic Regression**
5. Avaliação com:
   - Acurácia
   - Classification Report
   - Matriz de Confusão

---

## 📊 Resultados Obtidos

Na primeira execução, o modelo apresentou desempenho limitado, com acurácia aproximada de **40%**, além de dificuldade para identificar corretamente frases da classe **alto risco**.

### Interpretação crítica dos resultados

Esse comportamento é coerente com a configuração experimental do projeto, já que:

- o dataset é pequeno
- a diversidade linguística é reduzida
- há pouca variedade semântica entre as frases
- o volume de dados ainda não é suficiente para boa generalização

Esse ponto é relevante porque demonstra, de forma prática, uma limitação central da IA aplicada à saúde:

> Um modelo de aprendizado de máquina depende fortemente da qualidade, volume e equilíbrio dos dados disponíveis.

Assim, mesmo com código funcional e pipeline correto, o desempenho do classificador reforça a importância de bases mais robustas, bem balanceadas e representativas.

---

## ⚖️ Governança, Qualidade e Viés em Dados

A atividade também estimula uma reflexão importante sobre **IA responsável**, especialmente em contexto clínico.

Principais pontos observados:

- bases pequenas podem induzir viés
- modelos podem favorecer a classe mais frequente
- textos curtos e pouco variados reduzem a capacidade de generalização
- decisões automatizadas em saúde não devem ocorrer sem supervisão humana

Esse projeto, portanto, não busca apenas implementar uma solução técnica, mas também reforçar a importância da **governança de dados**, da explicabilidade e do uso ético da Inteligência Artificial.

---

## 💡 Continuidade em Relação à Fase 1

A Fase 2 foi construída respeitando a continuidade conceitual e estrutural do projeto iniciado anteriormente.

### Fase 1
Na primeira entrega, o foco foi a organização de dados cardiológicos em três dimensões:
- dados numéricos clínicos
- dados textuais médicos
- imagens ECG
```git da fase 1
https://github.com/limadeivisson/cardioia-fase1-dados-cardiologicos
```

### Fase 2
Nesta fase, os dados textuais deixam de ser apenas organizados e passam a ser utilizados de forma aplicada, com:
- interpretação semântica básica
- associação sintoma-doença
- classificação de risco clínico

Essa evolução mostra maturidade do projeto e alinhamento com a proposta integradora do CardioIA.

---

## 📦 Tecnologias Utilizadas

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Jupyter Notebook**
- **TF-IDF**
- **Logistic Regression**

---

## 🔧 Como Executar o Projeto

### Pré-requisitos

- Python 3.9 ou superior

### Instalação das dependências

```bash
pip install -r requirements.txt
```

### Executar Parte 1

```bash
python scripts/parte1_extracao_sintomas.py
```

### Executar Parte 2

```bash
python scripts/parte2_classificador_risco.py
```

### Executar no Google Colab

Caso deseje usar os notebooks no Google Colab, clone o repositório com:

```python
!git clone https://github.com/limadeivisson/cardioia-fase2-diagnostico-automatizado.git
```

---

## 🎥 Vídeo de Demonstração

O funcionamento completo da solução pode ser visualizado no vídeo:

👉 **[https://youtu.be/zaeCxzyVB8w]**

---

## 📊 Dados Utilizados

Um dos pontos de melhoria considerados a partir do feedback da Fase 1 foi reduzir a dependência de links externos.

Por isso, nesta entrega:

- os principais arquivos de dados utilizados estão incluídos diretamente no repositório
- o projeto pode ser executado sem depender de bases externas adicionais
- a estrutura está leve, organizada e reprodutível

### Arquivos principais

- `sintomas_pacientes.txt` → frases simuladas de pacientes
- `mapa_conhecimento_sintomas_doencas.csv` → associação entre sintomas e diagnósticos
- `frases_risco_rotuladas.csv` → dataset de frases médicas com rótulos de risco

---

## 📚 Conceitos Aplicados

Durante esta fase, foram aplicados conceitos das seguintes áreas:

- Processamento de Linguagem Natural (NLP)
- Extração de informação
- Classificação supervisionada
- Representação vetorial de texto
- Machine Learning clássico
- Governança e viés em IA
- Apoio automatizado à decisão clínica

---

## 📈 Potenciais Evoluções Futuras

Como continuidade do projeto CardioIA, futuras melhorias podem incluir:

- aumento do dataset textual
- refinamento do mapa de conhecimento
- uso de lematização e remoção de stopwords
- comparação entre múltiplos classificadores
- integração com interface web
- explicabilidade das previsões
- aplicação combinada com dados numéricos clínicos da Fase 1

---

## 🗃 Histórico de Lançamentos

- **0.2.0 - 2026**
  - Estrutura inicial da Fase 2
  - Implementação da extração de sintomas
  - Implementação do classificador de risco

- **0.2.1 - 2026**
  - Ajuste dos notebooks para execução local e no Google Colab
  - Melhoria da documentação
  - Revisão do README com base no feedback da Fase 1

---

## 📋 Licença

Projeto acadêmico desenvolvido para fins educacionais no curso de Inteligência Artificial da FIAP.

> Este sistema possui finalidade didática e demonstrativa.  
> Não substitui avaliação médica, triagem hospitalar real ou diagnóstico clínico profissional.
