import glob
import pathlib
from typing import Any, Tuple, List

import pandas as pd
from docx import Document

from .objects import Table


def load_tables(path: str) -> List[pd.DataFrame]:
    '''Returns list of pandas dataframes loaded from CSV directory or specified
    docx file
    '''
    result_tables = []
    path_object = pathlib.Path(path)
    
    if path_object.is_dir():
        return _load_tables_from_csv_directory(path)
    elif path_object.suffix == ".docx":
        return _load_tables_from_docx(path)
    else:
        raise ValueError(path + " is not recognized")
    
def _load_tables_from_csv_directory(path: str) -> List[pd.DataFrame]:
    result_tables = []

    for i, f in enumerate(glob.glob(path + "/*.csv", recursive=True)):
        print("parsing", i, f)
        f = pathlib.Path(f)
        df = pd.read_csv(f, sep=',', thousands=' ', header=None, dtype=object, encoding='UTF-8')
        table_object = Table(f, df)
        result_tables.append(table_object)

    return result_tables

def _load_tables_from_docx(path: str) -> List[pd.DataFrame]:
    document = Document(path)
    result_tables = []

    for table in document.tables:
        rows = []
        for row in table.rows:
            cells = []
            for cell in row.cells:
                cells.append(cell.text if cell.text != "" else float('nan'))
            rows.append(cells)
        
        df = pd.DataFrame(rows)
        table_object = Table(path, df)
        result_tables.append(table_object)

    return result_tables