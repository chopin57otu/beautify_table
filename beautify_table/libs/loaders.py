import glob
import pathlib
from typing import Tuple, List, Any

import pandas as pd
from docx import Document


def load_documents(directory: str) -> list[tuple[list[pd.DataFrame], Any]]:
    document_tables = []
    for f in glob.glob(directory, recursive=False):
        p = pathlib.Path(f)
        if p.is_dir():
            tables = load_tables_from_csv_directory(f)
            document_tables.append((tables, f))
        if p.suffix == ".docx":
            tables = load_tables_from_docx(f)
            document_tables.append((tables, f))
    return document_tables


def load_tables_from_docx(path: str) -> List[pd.DataFrame]:
    document = Document(path)

    tables = []
    for i, t in enumerate(document.tables):
        table = []
        for col in t.rows:
            table.append([])
            for c in col.cells:
                table[-1].append(c.text if c.text != "" else float('nan'))
        tables.append(pd.DataFrame(table))

    return tables


def load_tables_from_csv_directory(path: str) -> List[pd.DataFrame]:
    tables = []
    for i, f in enumerate(glob.glob(path + "/*.csv", recursive=True)):
        print("parsing", i, f)
        f = pathlib.Path(f)
        table = pd.read_csv(f, sep=',', thousands=' ', header=None, dtype=object, encoding='UTF-8')
        tables.append(table)

    return tables

