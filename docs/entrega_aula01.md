# Entrega Aula 01 - Ambiente, Datasets Abertos e Princípios FAIR

## Identificação da entrega

- **Disciplina:** Engenharia de Dados e Inteligência Artificial Multimodal
- **Programa:** Pós-Graduação em Engenharia Biomédica
- **Projeto:** Biomarcadores acústicos de voz associados à doença de Parkinson
- **Repositório:** <https://github.com/B073LH0/detector-de-parkinson>

## Resumo

Esta entrega apresenta a definição e a preparação de um projeto acadêmico reproduzível para explorar características acústicas da voz potencialmente associadas à doença de Parkinson. O projeto utiliza o dataset aberto *Parkinson Dataset with replicated acoustic features*, identificado como UCI 489.

O trabalho não propõe diagnosticar a doença de Parkinson nem substituir avaliação médica. Seu uso clínico potencial é apoiar, em pesquisas futuras, estratégias de triagem não invasiva ou avaliação complementar baseada em biomarcadores vocais.

## Pergunta de pesquisa

> Características acústicas extraídas da voz apresentam diferenças mensuráveis entre indivíduos com doença de Parkinson e controles saudáveis e podem contribuir para diferenciar os dois grupos?

## Dataset selecionado

| Campo | Informação |
|---|---|
| Nome oficial | *Parkinson Dataset with replicated acoustic features* |
| Fonte | UCI Machine Learning Repository |
| Identificador | UCI 489 |
| DOI | <https://doi.org/10.24432/C5701F> |
| Licença | Creative Commons Attribution 4.0 International - CC BY 4.0 |
| Participantes | 80: 40 com Parkinson e 40 controles |
| Registros | 240 gravações, três por participante |
| Dados | 44 características acústicas extraídas da fonação sustentada da vogal `/a/` |
| Arquivo informado pela UCI | CSV com aproximadamente 120,7 KB |

O dataset bruto não foi incluído no Git. O notebook pode obtê-lo pela interface documentada `ucimlrepo.fetch_ucirepo(id=489)` ou utilizar uma cópia local fora do controle de versão.

## Conteúdo produzido

O repositório contém:

- README em português com objetivo, escopo, referências e instruções de execução;
- ficha técnica do dataset com fonte, licença, variáveis, tamanho, privacidade, uso clínico e limitações;
- avaliação FAIR com pontuação e justificativa para Findable, Accessible, Interoperable e Reusable;
- ambiente Python 3.11 isolado e dependências fixadas em `requirements.txt`;
- notebook de EDA executável do zero, preparado para inspeção estrutural, valores ausentes, classes, sexo, participantes e réplicas;
- análises preparadas em nível de participante: estatísticas descritivas, distribuições, correlações, associações exploratórias e PCA;
- módulo de carregamento com aquisição online e alternativa por CSV local;
- checklist que relaciona cada requisito do enunciado aos arquivos entregues.

## Decisão metodológica crítica

As 240 linhas não representam 240 indivíduos independentes. A base contém 80 participantes, cada um com três gravações. Por isso, análises principais são preparadas em nível de participante, por agregação das réplicas. Em qualquer Machine Learning futuro, treino e teste deverão ser separados por `ID`, utilizando estratégias como `GroupKFold`, `StratifiedGroupKFold` ou equivalentes. Um split aleatório por linha produziria vazamento de dados.

## Uso clínico e Machine Learning

- **Entradas:** características de jitter, shimmer, HNR, MFCC, delta-MFCC, RPDE, DFA, PPE e GNE.
- **Alvo:** `Status`, no qual 0 representa controle e 1 representa Parkinson.
- **Agrupamento:** `ID` do participante.
- **Métodos encontrados na literatura:** regressão binária Bayesiana em nível de sujeito, modelos probit com variáveis latentes, amostragem de Gibbs e abordagem em duas etapas para seleção de variáveis e classificação.
- **Possíveis baselines futuros:** regressão logística, SVM e Random Forest, sempre com validação agrupada por participante e pré-processamento dentro de cada dobra.

## Avaliação FAIR

| Princípio | Pontuação | Síntese da justificativa |
|---|---:|---|
| Findable | 5/5 | Página própria na UCI, metadados, identificador e DOI persistente. |
| Accessible | 5/5 | Acesso público por HTTPS, CSV e interface documentada. |
| Interoperable | 4/5 | Formato CSV e variáveis numéricas, mas sem ontologia biomédica formal. |
| Reusable | 4/5 | CC BY 4.0, DOI e documentação; reuso limitado pela amostra pequena, regional e replicada. |
| **Total** | **18/20** | Boa encontrabilidade e acessibilidade, com limitações semânticas e metodológicas registradas. |

## Privacidade e limitações

O CSV não apresenta identificadores pessoais diretos, mas inclui `ID` pseudonimizado, sexo e condição de saúde. Portanto, o risco de reidentificação é reduzido em relação ao áudio bruto, porém não é inexistente.

Entre as limitações estão a pequena amostra regional, o balanceamento artificial entre grupos, a dependência entre réplicas, a participação somente de pessoas com mais de 50 anos, a única tarefa de vogal sustentada, o protocolo específico de gravação, a ausência de áudio bruto e a falta de validação externa nesta entrega.

## Reprodutibilidade e estado da entrega

O projeto foi versionado em Git, publicado na branch `main` e configurado com Python 3.11.9. As dependências foram instaladas e verificadas sem conflitos. O notebook teve sua estrutura e sintaxe validadas e não contém caminhos absolutos nem resultados estatísticos inventados.

Por decisão metodológica, o dataset não foi baixado e a célula de aquisição não foi executada durante a preparação. Os resultados da EDA serão produzidos somente quando o notebook for executado pelo usuário com acesso à UCI ou com o CSV local.

## Acesso

Repositório completo e documentação:

**<https://github.com/B073LH0/detector-de-parkinson>**
