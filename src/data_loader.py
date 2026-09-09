"""Carregamento rastreável do dataset UCI 489, sem execução automática."""

from __future__ import annotations

from pathlib import Path
from typing import Literal

import pandas as pd


UCI_DATASET_ID = 489
DEFAULT_LOCAL_PATH = Path("data/raw/ReplicatedAcousticFeatures-ParkinsonDatabase.csv")
REQUIRED_COLUMNS = ("ID", "Recording", "Status", "Gender")


def _normalize_columns(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Remove espaços e BOM dos nomes, preservando os dados."""
    normalized = dataframe.copy()
    normalized.columns = [str(column).strip().lstrip("\ufeff") for column in normalized.columns]
    return normalized


def _check_required_columns(dataframe: pd.DataFrame) -> None:
    by_casefold = {column.casefold(): column for column in dataframe.columns}
    missing = [name for name in REQUIRED_COLUMNS if name.casefold() not in by_casefold]
    if missing:
        raise ValueError(
            "Colunas documentadas não encontradas: "
            f"{missing}. Colunas recebidas: {list(dataframe.columns)}"
        )


def _load_online() -> pd.DataFrame:
    """Obtém o dataset pela interface documentada da UCI."""
    from ucimlrepo import fetch_ucirepo

    dataset = fetch_ucirepo(id=UCI_DATASET_ID)
    original = getattr(dataset.data, "original", None)
    if isinstance(original, pd.DataFrame) and not original.empty:
        return original.copy()

    parts = [dataset.data.features, dataset.data.targets]
    valid_parts = [part for part in parts if isinstance(part, pd.DataFrame)]
    if not valid_parts:
        raise RuntimeError("A resposta da UCI não contém tabelas de features/targets.")
    return pd.concat(valid_parts, axis=1)


def load_parkinson_data(
    source: Literal["online", "local"] = "online",
    local_path: str | Path | None = None,
) -> pd.DataFrame:
    """Carrega e valida a estrutura mínima do dataset.

    Parameters
    ----------
    source:
        ``online`` chama ``fetch_ucirepo(id=489)``; ``local`` lê um CSV.
    local_path:
        Caminho do CSV quando ``source='local'``. Se omitido, usa o caminho
        relativo ``data/raw/ReplicatedAcousticFeatures-ParkinsonDatabase.csv``.
    """
    if source == "online":
        dataframe = _load_online()
    elif source == "local":
        csv_path = Path(local_path) if local_path is not None else DEFAULT_LOCAL_PATH
        if not csv_path.is_file():
            raise FileNotFoundError(
                f"CSV não encontrado em {csv_path.resolve()}. "
                "Consulte DATASET.md para obter o arquivo oficial."
            )
        dataframe = pd.read_csv(csv_path)
    else:
        raise ValueError("source deve ser 'online' ou 'local'.")

    dataframe = _normalize_columns(dataframe)
    _check_required_columns(dataframe)
    return dataframe
