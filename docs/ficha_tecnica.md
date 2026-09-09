# Ficha técnica — Parkinson Dataset with replicated acoustic features

**Versão desta ficha:** 1.0

**Data de consulta das fontes:** 8 de setembro de 2026

**Escopo:** entrega acadêmica de documentação FAIR e preparação de EDA; nenhum resultado do notebook foi calculado nesta versão.

## 1. Nome e fonte

| Campo | Informação verificada |
|---|---|
| Nome oficial | *Parkinson Dataset with replicated acoustic features* |
| Fonte | UCI Machine Learning Repository |
| URL | <https://archive.ics.uci.edu/dataset/489/parkinson+dataset+with+replicated+acoustic+features> |
| Identificador | UCI 489 |
| DOI | <https://doi.org/10.24432/C5701F> |
| Criador indicado pela UCI | Carlos Perez |
| Ano indicado na citação UCI | 2016 |
| Data de doação indicada pela UCI | 9 de abril de 2019 |

O registro Zenodo 16451705 foi apenas um instrumento anterior de descoberta. A análise usa como fonte canônica a UCI.

## 2. Licença e restrições

A UCI declara a licença **Creative Commons Attribution 4.0 International (CC BY 4.0)**. Ela permite compartilhar e adaptar os dados, inclusive para qualquer finalidade, desde que seja atribuído crédito adequado, fornecido o link da licença e indicadas alterações.

Esta licença não elimina deveres éticos no tratamento de dados biomédicos. O repositório mantém apenas a referência e o código de aquisição; a cópia bruta fica fora do Git.

## 3. Composição, tamanho e unidade de análise

| Item | Valor/documentação |
|---|---|
| Participantes independentes | **80 indivíduos** |
| Grupos | 40 com doença de Parkinson e 40 controles saudáveis |
| Gravações por indivíduo | 3 gravações consecutivas |
| Registros no CSV | **240 linhas/gravações** |
| Tarefa vocal | Fonação sustentada da vogal `/a/`, em tom e intensidade confortáveis, por pelo menos 5 s e em uma respiração no protocolo original |
| Características acústicas | 44 variáveis derivadas |
| Campos adicionais | `ID`, `Recording`, `Status`, `Gender` |
| Arquivo | `ReplicatedAcousticFeatures-ParkinsonDatabase.csv` |
| Tamanho informado | 120,7 KB na tabela de arquivos da UCI; a interface exibe 120,9 KB para o download |
| Valores ausentes | A UCI reporta que não há |
| Período de coleta | Não identificado de forma clara nas fontes consultadas |

**Advertência metodológica:** os 240 registros não são 240 exemplos independentes. As três linhas do mesmo `ID` compartilham o participante. Análises inferenciais e validações de ML devem respeitar o agrupamento; um split aleatório por linha produz risco de vazamento entre treino e teste.

## 4. Variáveis principais, tipos, formatos e faixas

O arquivo é tabular, em CSV. A documentação da UCI e o artigo de geração descrevem:

| Grupo | Variáveis | Tipo/formato | Unidade ou faixa verificada |
|---|---|---|---|
| Identificação | `ID` | identificador/categórica | código pseudonimizado; faixa empírica será conferida na execução |
| Réplica | `Recording` | inteiro/categórica ordinal | número da gravação; codificação empírica será conferida na execução |
| Alvo clínico | `Status` | binária | 0 = controle saudável; 1 = Parkinson |
| Sexo | `Gender` | binária | 0 = homem; 1 = mulher |
| Perturbação de frequência | `Jitter_rel`, `Jitter_abs`, `Jitter_RAP`, `Jitter_PPQ` | numéricas contínuas | `Jitter_rel` em porcentagem; demais unidades conforme método de extração/artigo |
| Perturbação de amplitude | `Shim_loc`, `Shim_dB`, `Shim_APQ3`, `Shim_APQ5`, `Shim_APQ11` | numéricas contínuas | `Shim_dB` em dB; faixas empíricas não antecipadas |
| Harmônico-ruído | `HNR05`, `HNR15`, `HNR25`, `HNR35`, `HNR38` | numéricas contínuas | bandas 0–500, 0–1500, 0–2500, 0–3500 e 0–3800 Hz |
| Espectrais | `MFCC0`–`MFCC12` | numéricas contínuas | coeficientes de ordem 0 a 12 |
| Dinâmica espectral | `Delta0`–`Delta12` | numéricas contínuas | derivadas dos MFCC de ordem 0 a 12 |
| Não lineares/ruído | `RPDE`, `DFA`, `PPE`, `GNE` | numéricas contínuas | faixas empíricas não antecipadas |

Não foram incluídas mínimas e máximas empíricas porque o arquivo não foi baixado nem executado nesta etapa. O notebook calcula `min`, quartis e `max` de forma rastreável na primeira execução. A UCI documenta `Gender`, mas não lista idade entre as colunas distribuídas; as idades resumidas no artigo são características da coorte, não entradas desta análise.

## 5. Proveniência e protocolo de aquisição

O artigo original informa 80 participantes com mais de 50 anos. Os 40 participantes com Parkinson eram membros da Associação Regional de Parkinson de Extremadura, Espanha; o protocolo foi aprovado pelo comitê de bioética da Universidade de Extremadura e houve consentimento informado. A tarefa `/a/` foi repetida três vezes. O áudio foi registrado a 44,1 kHz e 16 bits/amostra, com interface TASCAM US322, microfone AKG 520 e Audacity 2.0.5.

Esses detalhes descrevem a origem das características. O arquivo público listado pela UCI contém o CSV de características derivadas, não os sinais de áudio bruto.

## 6. Privacidade e potencial de reidentificação

O CSV documentado não apresenta nomes, contatos ou outros identificadores pessoais diretos. `ID` funciona como identificador pseudonimizado. Ainda assim, há informação sensível:

- `Status` revela condição de saúde;
- `Gender` acrescenta um atributo demográfico;
- três registros podem ser ligados ao mesmo participante por `ID`;
- associação com fontes externas ou conhecimento local da pequena coorte pode elevar o risco de reidentificação.

O risco é provavelmente menor do que na distribuição de voz bruta, que pode carregar conteúdo e características biométricas mais ricas, mas não é nulo. Recomenda-se evitar tentativas de ligação de identidades, não publicar enriquecimentos identificáveis e manter apenas dados necessários à finalidade acadêmica.

## 7. Uso clínico potencial e ML

### Aplicação potencial

Apoio futuro a triagem não invasiva ou suporte complementar à avaliação da doença de Parkinson por biomarcadores vocais. Esta entrega não valida diagnóstico, prognóstico nem decisão terapêutica.

### Pergunta de pesquisa

> Características acústicas extraídas da voz apresentam diferenças mensuráveis entre indivíduos com doença de Parkinson e controles saudáveis e podem contribuir para diferenciar os dois grupos?

### Entradas e alvo

- **Entradas:** 44 características acústicas de jitter, shimmer, HNR, MFCC, delta-MFCC, RPDE, DFA, PPE e GNE. `Gender` pode ser descrito separadamente e somente incluído em modelos futuros mediante justificativa e análise de viés.
- **Alvo/rótulo:** `Status`, com 0 = controle e 1 = Parkinson.
- **Agrupamento obrigatório:** `ID`.
- **Identificador de réplica:** `Recording`, que não deve ser usado como biomarcador preditivo.

### Métodos já relatados

Naranjo et al. (2016) propuseram regressão binária Bayesiana em nível de sujeito, com variável latente/probit e amostragem de Gibbs, para modelar explicitamente as réplicas. O artigo relata validação cruzada desenhada em nível de participante e alerta que ignorar as réplicas pode produzir estimativas otimistas.

Naranjo et al. (2017) desenvolveram uma abordagem Bayesiana em duas etapas para seleção de variáveis e classificação, também adequada ao desenho replicado e resolvida por Gibbs sampling. No artigo, os autores reportam 86,2% de acurácia, 82,5% de sensibilidade e 90,0% de especificidade nessa base. Esses números são **resultados da literatura, não foram reproduzidos neste projeto**.

Modelos como regressão logística, SVM e Random Forest são opções comuns para baselines em dados tabulares, mas qualquer avaliação futura aqui deverá usar `GroupKFold`, `StratifiedGroupKFold`, `GroupShuffleSplit` ou estratégia equivalente por `ID`; seleção de atributos, padronização e ajuste devem ocorrer dentro de cada dobra.

## 8. Avaliação FAIR

Escala: 0 = não atende; 1 = atende muito pouco; 2 = atende parcialmente; 3 = atende razoavelmente; 4 = atende bem; 5 = atende de forma excelente. Total possível: 20.

| Princípio | Pontuação | Justificativa |
|---|---:|---|
| **Findable** | **5/5** | Há página própria em repositório reconhecido, título, criador, identificador UCI, metadados pesquisáveis e DOI persistente. O projeto registra a referência canônica em vários pontos e um arquivo de URL simples. |
| **Accessible** | **5/5** | A UCI oferece acesso público por HTTPS, download do CSV e interface documentada via `ucimlrepo`, sem autorização clínica individual ou login informado. O protocolo de acesso e uma alternativa local estão documentados. A nota se refere à base tabular publicada, não ao áudio bruto. |
| **Interoperable** | **4/5** | CSV e variáveis majoritariamente numéricas são amplamente legíveis por ferramentas abertas; nomes, papéis e algumas unidades são documentados. Perde um ponto porque não há, na página consultada, ontologia biomédica formal, vocabulário controlado ou esquema clínico interoperável, e várias unidades/faixas dependem do artigo. |
| **Reusable** | **4/5** | DOI, licença CC BY 4.0, citação recomendada, protocolo e artigos metodológicos sustentam reutilização. A pequena coorte regional, a dependência entre réplicas, a ausência de áudio bruto, o período de coleta não identificado e detalhes distribuídos entre repositório e artigo limitam reuso e generalização sem cautela. |
| **Total** | **18/20** | Boa encontrabilidade e acessibilidade, com limitações semânticas e metodológicas relevantes. |

As pontuações avaliam o dataset publicado e sua documentação atual; não equivalem a certificação FAIR formal.

## 9. Limitações conhecidas

- apenas 80 participantes e 40 por grupo;
- balanceamento artificial entre classes, incompatível com inferência de prevalência;
- três gravações dependentes por pessoa;
- seleção dos participantes com Parkinson por associação regional em Extremadura;
- somente participantes com mais de 50 anos;
- composição por sexo diferente entre os grupos no artigo, um potencial fator de confusão;
- fonação sustentada de uma única vogal, não fala espontânea ou múltiplas tarefas;
- equipamento, software e protocolo específicos de gravação;
- características pré-extraídas, sem áudio bruto para repetir a extração;
- período de coleta não identificado claramente;
- ausência de validação externa em outra população nesta entrega;
- cautela necessária para generalizar a idiomas, sotaques, microfones, ruídos e contextos clínicos diferentes;
- inadequação da base isolada para validar um instrumento clínico.

## 10. Plano analítico e controles contra vazamento

1. conferir esquema, tipos, ausências, duplicatas e cardinalidades;
2. verificar exatamente três gravações e consistência de rótulo por `ID`;
3. manter descrição por gravação apenas como visão da estrutura dependente;
4. agregar por participante (mediana das três gravações) para comparações principais;
5. explorar distribuições, correlações, efeito padronizado, correlação ponto-bisserial e PCA;
6. tratar testes múltiplos como exploratórios e aplicar Benjamini–Hochberg quando p-valores forem exibidos;
7. em ML futuro, dividir exclusivamente por participante e encapsular pré-processamento/seleção dentro da validação.

## 11. Referências

1. UCI Machine Learning Repository. *Parkinson Dataset with replicated acoustic features*. <https://archive.ics.uci.edu/dataset/489/parkinson+dataset+with+replicated+acoustic+features>.
2. Perez, C. (2016). *Parkinson Dataset with replicated acoustic features* [Dataset]. <https://doi.org/10.24432/C5701F>.
3. Naranjo, L., Pérez, C. J., Campos-Roca, Y., & Martín, J. (2016). *Expert Systems with Applications, 46*, 286–292. <https://doi.org/10.1016/j.eswa.2015.10.034>.
4. Naranjo, L., Pérez, C. J., Martín, J., & Campos-Roca, Y. (2017). *Computer Methods and Programs in Biomedicine, 142*, 147–156. <https://doi.org/10.1016/j.cmpb.2017.02.019>; resumo indexado em <https://pubmed.ncbi.nlm.nih.gov/28325442/>.
5. Creative Commons. *Attribution 4.0 International*. <https://creativecommons.org/licenses/by/4.0/>.
6. Wilkinson, M. D. et al. (2016). *The FAIR Guiding Principles for scientific data management and stewardship*. <https://doi.org/10.1038/sdata.2016.18>.
