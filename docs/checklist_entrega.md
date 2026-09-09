# Checklist de conformidade — Aula 01

## Especificação formal recebida

O texto abaixo é preservado sem reescrita para permitir auditoria da entrega.

> Entrega referente à Aula 01 (18/08/2026): Ambiente, Datasets Abertos e Princípios FAIR.
>
> O que entregar:
> - Dataset escolhido (referencia somente)
> - Uso clínico potencial e ML: aplicação, pergunta de pesquisa, entradas, alvo/rótulo e métodos de ML já relatados para esse tipo de dado.
> - Ficha técnica legível, em Markdown, PDF ou outro formato de texto simples, cobrindo:
>   • Nome e fonte (nome oficial e URL de acesso)
>   • Licença (tipo e restrições de uso)
>   • Variáveis principais (tipos, formatos, faixas)
>   • Tamanho (nº de exemplos e tamanho em disco)
>   • Riscos de privacidade (potencial de reidentificação)
>   • Uso clínico e ML (aplicação, pergunta, entradas, alvo/rótulo, métodos já utilizados)
>   • Avaliação FAIR, com pontuação E JUSTIFICATIVA por princípio (Findable, Accessible, Interoperable, Reusable)
>   • Limitações conhecidas (viés de seleção, cobertura, período)
> - Ambiente reprodutível configurado: local (venv/conda) ou nuvem (Colab/Kaggle Kernels), com dependências fixadas e setup registrado (ex. requirements.txt) + README.
> - Notebook de exploração (EDA): visualizar sinais ou exemplos e examinar distribuição, cobertura e diversidade do dataset, executável do zero.
>
> Como enviar: repositório GitHub, link de notebook executável, pasta compactada ZIP ou formato equivalente — desde que contenha instruções claras, dependências, dados/amostras necessárias e caminho de execução reprodutível.
>
> Critérios de avaliação: reprodutibilidade, correção técnica, avaliação FAIR com justificativa e documentação.

## Matriz de atendimento

| Requisito | Evidência no repositório | Situação antes da execução dos dados |
|---|---|---|
| Dataset escolhido, somente referência | `DATASET.md`, `data/dataset_url.txt`, `data/README.md` | Atendido; nenhum CSV incluído |
| Aplicação clínica potencial | `README.md` e ficha técnica, seção 7 | Atendido com ressalva de não diagnóstico |
| Pergunta, entradas e alvo | `README.md` e ficha técnica, seção 7 | Atendido |
| Métodos já relatados | Ficha técnica, seção 7, com artigos de 2016 e 2017 | Atendido; resultados claramente atribuídos à literatura |
| Nome, fonte e URL | Ficha técnica, seção 1 | Atendido |
| Licença e restrições | Ficha técnica, seção 2 | Atendido |
| Variáveis, tipos, formatos e faixas | Ficha técnica, seção 4 | Atendido; faixas empíricas ficam para execução, sem invenção |
| Nº de exemplos e tamanho em disco | Ficha técnica, seção 3 | Atendido; distingue 80 participantes de 240 registros |
| Riscos de privacidade | Ficha técnica, seção 6 | Atendido; risco residual de associação/reidentificação |
| FAIR com nota e justificativa | Ficha técnica, seção 8 | Atendido: 18/20 |
| Viés, cobertura e período | Ficha técnica, seção 9 | Atendido; período não identificado é explicitado |
| Ambiente isolado | `.venv/` local, ignorado pelo Git | Configurado com Python 3.11.9 |
| Dependências fixadas | `requirements.txt` | Atendido |
| Setup registrado | `README.md`, seção Ambiente reproduzível | Atendido |
| EDA executável do zero | `notebooks/01_eda.ipynb` e `src/data_loader.py` | Preparado; execução depende de acesso autorizado à UCI ou CSV local |
| Distribuição, cobertura e diversidade | Seções de classes, sexo, participantes, réplicas e variáveis no notebook | Código preparado; sem resultados inventados |
| Caminho reprodutível | README, DATASET e parâmetros visíveis no notebook | Atendido |

## Gates antes do envio

- [x] fonte, DOI e licença verificados na UCI;
- [x] artigos metodológicos identificados por DOI;
- [x] dependência entre réplicas documentada;
- [x] dados brutos e ambiente excluídos pelo `.gitignore`;
- [x] notebook sem caminhos absolutos e com fontes online/local;
- [x] nenhum treinamento de modelo;
- [x] nenhum resultado de EDA inventado;
- [ ] executar o notebook com internet ou CSV local, por decisão do autor;
- [ ] revisar os resultados produzidos pela execução;
- [ ] publicar o repositório no GitHub e, se desejado, adicionar o link direto do Colab.
