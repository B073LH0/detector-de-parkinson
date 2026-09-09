# Biomarcadores acústicos de voz na doença de Parkinson

Projeto acadêmico da disciplina **Engenharia de Dados e Inteligência Artificial Multimodal**, do Programa de Pós-Graduação em Engenharia Biomédica. Esta primeira entrega documenta uma base aberta, organiza um ambiente reproduzível e prepara uma análise exploratória (EDA) rastreável segundo os princípios FAIR.

O projeto não propõe diagnosticar a doença de Parkinson nem substituir avaliação médica. Seu foco é investigar, de forma exploratória, características acústicas já extraídas de gravações de voz.

## Objetivo e pergunta de pesquisa

**Objetivo:** descrever a organização, a cobertura e a qualidade do dataset e explorar diferenças e associações entre características acústicas da voz e o grupo clínico, respeitando a dependência entre gravações do mesmo participante.

**Pergunta:** características acústicas extraídas da voz apresentam diferenças mensuráveis entre indivíduos com doença de Parkinson e controles saudáveis e podem contribuir para diferenciar os dois grupos?

**Uso clínico potencial:** apoio futuro a estratégias de triagem não invasiva ou suporte complementar à avaliação da doença de Parkinson com biomarcadores vocais. Qualquer aplicação clínica exigiria validação externa, prospectiva e regulatória; esta amostra isolada não sustenta um instrumento diagnóstico.

## Dataset

- **Nome oficial:** *Parkinson Dataset with replicated acoustic features*
- **Fonte:** [UCI Machine Learning Repository — dataset 489](https://archive.ics.uci.edu/dataset/489/parkinson+dataset+with+replicated+acoustic+features)
- **DOI persistente:** [10.24432/C5701F](https://doi.org/10.24432/C5701F)
- **Licença:** [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
- **Arquivo distribuído pela UCI:** `ReplicatedAcousticFeatures-ParkinsonDatabase.csv` (120,7 KB informados pela UCI)
- **Estrutura documentada:** 80 participantes — 40 com Parkinson e 40 controles —, três gravações consecutivas de fonação sustentada da vogal `/a/` por participante e 240 registros. O arquivo contém 44 características acústicas, além de identificador do participante, número da gravação, `Status` e `Gender`.

O dataset bruto **não faz parte deste repositório**. A proveniência, a obtenção online e o caminho local alternativo estão detalhados em [DATASET.md](DATASET.md).

> **Unidade experimental:** 240 linhas não equivalem a 240 pessoas. As três gravações de cada participante são dependentes. Nenhum modelo futuro deverá separar treino e teste aleatoriamente por linha; a divisão deve ser agrupada pelo identificador do participante.

## Escopo da EDA

O notebook prepara, nesta ordem:

1. aquisição explícita pela UCI ou leitura de CSV local;
2. inspeção de forma, colunas, tipos, duplicatas e ausências;
3. conferência de participantes, classes, sexo e três gravações por pessoa;
4. validação da consistência de `Status` e `Gender` dentro de cada participante;
5. estatísticas descritivas e representação agregada por mediana individual;
6. distribuições por grupo em características representativas;
7. correlações e pares potencialmente redundantes;
8. associação exploratória com `Status`, tamanho de efeito e ajuste de Benjamini–Hochberg;
9. PCA exploratória em nível de participante.

Não há treinamento de classificador nesta entrega. Resultados numéricos, gráficos e conclusões exploratórias serão produzidos somente quando o notebook for executado com os dados.

## Estrutura do repositório

```text
.
├── README.md
├── DATASET.md
├── requirements.txt
├── data/
│   ├── README.md
│   └── dataset_url.txt
├── docs/
│   ├── ficha_tecnica.md
│   └── checklist_entrega.md
├── notebooks/
│   └── 01_eda.ipynb
└── src/
    └── data_loader.py
```

`docs/checklist_entrega.md` preserva o enunciado formal da atividade e mapeia cada requisito para a evidência correspondente. É o único arquivo adicional à estrutura mínima e existe para tornar a auditoria da entrega rastreável.

## Ambiente reproduzível

Versão usada na preparação: **Python 3.11.9**. As versões diretas estão fixadas em `requirements.txt`.

No PowerShell, a partir da raiz do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m jupyter lab
```

No Prompt de Comando (`cmd`), a ativação é:

```bat
.venv\Scripts\activate.bat
```

No VS Code, selecione o interpretador `.venv\Scripts\python.exe`, abra `notebooks/01_eda.ipynb` e escolha esse kernel.

## Como executar do zero

1. Clone ou extraia o repositório.
2. Crie e ative o ambiente conforme acima.
3. Instale `requirements.txt`.
4. Abra `notebooks/01_eda.ipynb`.
5. Revise a variável `DATA_SOURCE` na célula de configuração:
   - `"online"` (padrão): chama a interface documentada `ucimlrepo.fetch_ucirepo(id=489)` e requer internet na primeira execução;
   - `"local"`: lê `data/raw/ReplicatedAcousticFeatures-ParkinsonDatabase.csv`.
6. Execute as células em ordem, a partir de um kernel novo.

A primeira execução online obterá os dados da UCI. Esse acesso é deliberadamente acionado somente pelo usuário no notebook; a configuração inicial deste repositório não executa o `fetch`.

### Uso opcional no Google Colab

Após publicar o repositório no GitHub, abra o notebook pelo menu **File > Open notebook > GitHub** do Colab. Para manter `src/` e `requirements.txt` disponíveis, clone o repositório no ambiente Colab e altere o diretório corrente para a raiz antes de executar. O fluxo local em VS Code/Jupyter é a referência desta entrega.

## Reprodutibilidade e FAIR

- fonte canônica, DOI, licença e data de consulta registrados;
- dependências diretas fixadas e ambiente isolado fora do Git;
- aquisição de dados explícita, com alternativa local e sem dados brutos versionados;
- notebook linear, parâmetros visíveis e caminhos relativos com `pathlib`;
- verificações de esquema, classes, número de participantes e réplicas;
- análise principal em nível de participante para não confundir réplicas com observações independentes;
- Git como trilha de mudanças e checklist que liga requisitos a arquivos.

A avaliação FAIR justificada (18/20) está em [docs/ficha_tecnica.md](docs/ficha_tecnica.md).

## Limitações principais

- amostra pequena e balanceada por desenho (80 participantes), não representativa de prevalência clínica;
- três registros por participante, com dependência intraindivíduo;
- participantes com Parkinson vinculados a uma associação regional de Extremadura, Espanha, o que limita generalização populacional e geográfica;
- somente pessoas com mais de 50 anos no estudo original;
- apenas fonação sustentada de `/a/`, com protocolo e equipamento específicos;
- disponibilização de características derivadas, não do áudio bruto, limitando novas extrações e auditoria do sinal;
- ausência de período de coleta claramente identificado na documentação consultada;
- generalização para outros idiomas, sotaques, microfones, ambientes e contextos clínicos não foi estabelecida por esta entrega.

## Referências

- Perez, C. (2016). *Parkinson Dataset with replicated acoustic features* [Dataset]. UCI Machine Learning Repository. [https://doi.org/10.24432/C5701F](https://doi.org/10.24432/C5701F).
- Naranjo, L., Pérez, C. J., Campos-Roca, Y., & Martín, J. (2016). Addressing voice recording replications for Parkinson's disease detection. *Expert Systems with Applications, 46*, 286–292. [https://doi.org/10.1016/j.eswa.2015.10.034](https://doi.org/10.1016/j.eswa.2015.10.034).
- Naranjo, L., Pérez, C. J., Martín, J., & Campos-Roca, Y. (2017). A two-stage variable selection and classification approach for Parkinson's disease detection by using voice recording replications. *Computer Methods and Programs in Biomedicine, 142*, 147–156. [https://doi.org/10.1016/j.cmpb.2017.02.019](https://doi.org/10.1016/j.cmpb.2017.02.019).
- Wilkinson, M. D. et al. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data, 3*, 160018. [https://doi.org/10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18).
