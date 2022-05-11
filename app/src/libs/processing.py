import pandas as pd
from .squeeze import merge_columns, squeeze_headers
from .string_manipulations import (is_empty, is_number,
                                                          is_string)
from .objects import Table
from typing import Tuple


def process_table(table:Table) -> pd.DataFrame:
    na = _identify_number_area(table.df)
    sc = squeeze_headers(table.df, na)
    merged = merge_columns(sc)
    cleaned = merged.replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=["",""], regex=True)
    final = Table(table.path, cleaned)
    
    return final

def _identify_number_area(df:pd.DataFrame) -> Tuple[int]:
    '''Identifies end corner of the table'''

    ic = _identification_mask(df)

    max_i, max_j = ic.shape
    index_sum = float('inf')
    for i in range(ic.shape[0]):
        for j in range(ic.shape[1]):
            if 0 == (ic.iloc[i:, j:] == "s").sum().sum() and i + j < index_sum:
                index_sum = i + j
                max_i, max_j = i, j

    return max_i, max_j

def _identification_mask(df:pd.DataFrame):
    '''Fills in entire table with None, n or s based on cell data type'''

    def substitute(e):
        if is_empty(e):
            return None
        if is_number(e):
            return "n"
        return "s"
    return df.applymap(substitute)




