# Proveniência e obtenção do dataset

## Identificação canônica

| Campo | Valor |
|---|---|
| Nome oficial | *Parkinson Dataset with replicated acoustic features* |
| Repositório | UCI Machine Learning Repository |
| Identificador UCI | 489 |
| Página oficial | <https://archive.ics.uci.edu/dataset/489/parkinson+dataset+with+replicated+acoustic+features> |
| DOI | <https://doi.org/10.24432/C5701F> |
| Licença | CC BY 4.0 |
| Arquivo | `ReplicatedAcousticFeatures-ParkinsonDatabase.csv` |
| Tamanho informado | 120,7 KB na tabela de arquivos da UCI (a interface também exibe 120,9 KB para o download total) |
| Consulta dos metadados | 8 de setembro de 2026 |

O registro Zenodo 16451705 (<https://zenodo.org/records/16451705>) foi usado na etapa anterior apenas como mapa para localizar e comparar datasets sobre Parkinson. Ele não é a fonte dos dados desta análise. A UCI e o DOI acima são as referências canônicas.

## Conteúdo documentado

A UCI descreve 240 registros correspondentes a três gravações consecutivas de cada um de 80 participantes (40 com doença de Parkinson e 40 controles). A tarefa é a fonação sustentada da vogal `/a/`. O estudo original descreve 44 características acústicas e quatro campos de identificação/contexto:

- `ID`: identificador pseudonimizado do participante;
- `Recording`: número da gravação;
- `Status`: 0 = controle saudável; 1 = Parkinson;
- `Gender`: 0 = homem; 1 = mulher;
- características de jitter: `Jitter_rel`, `Jitter_abs`, `Jitter_RAP`, `Jitter_PPQ`;
- características de shimmer: `Shim_loc`, `Shim_dB`, `Shim_APQ3`, `Shim_APQ5`, `Shim_APQ11`;
- HNR por bandas: `HNR05`, `HNR15`, `HNR25`, `HNR35`, `HNR38`;
- coeficientes `MFCC0` a `MFCC12` e derivadas `Delta0` a `Delta12`;
- medidas não lineares/ruído: `RPDE`, `DFA`, `PPE`, `GNE`.

A UCI reporta ausência de valores faltantes. Faixas empíricas, estatísticas e presença de duplicatas não são antecipadas neste documento: serão calculadas pelo notebook quando o dataset for obtido.

## Opção 1 — aquisição online recomendada

A página oficial documenta o pacote `ucimlrepo`:

```python
from ucimlrepo import fetch_ucirepo

dataset = fetch_ucirepo(id=489)
```

O módulo `src/data_loader.py` encapsula essa chamada e reúne preditores e alvo em uma tabela. A operação requer internet e somente ocorre quando o usuário executa a célula de carregamento com `DATA_SOURCE = "online"`.

## Opção 2 — CSV local

Baixe manualmente o arquivo pela página oficial e salve em:

```text
data/raw/ReplicatedAcousticFeatures-ParkinsonDatabase.csv
```

Em seguida, defina `DATA_SOURCE = "local"` no notebook. A pasta `data/raw/` é ignorada pelo Git.

## Política de versionamento

- o arquivo bruto não é incluído no repositório;
- `data/raw/` e `data/processed/` estão no `.gitignore`;
- derivados futuros devem registrar o código e os parâmetros que os produziram;
- a licença exige atribuição adequada à fonte;
- não se deve redistribuir uma cópia sem manter citação, licença e proveniência.

## Integridade e rastreabilidade futura

Após a primeira obtenção autorizada, recomenda-se registrar localmente o nome, o tamanho em bytes, a data/hora e um hash SHA-256 do arquivo em um relatório de execução. O hash não foi calculado agora porque, por decisão metodológica, o dataset não foi baixado nesta configuração.
