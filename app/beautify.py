"""Beautify tables is program for getting numerical data from ugly
data tables such as those parsed using https://github.com/tabulapdf/tabula
or converted pdf documents.

It clean tables so there is rectangle of numbers in right bottom
and row and column labels are concatenated. Load tables from docx,
directory of csv files or directory of both.

Usage:
  beautify.py --from <input_file_or_dir> --to <dir> --output-to-file

Options:
  -h --help                   Show this screen.
  --from <input_file_or_dir>  Input files or directory of csv files or directory of input files.
  --to <dir>                  Output directory.
  --output-to-file            Whether to output result to file (.xlsx).

"""
from pathlib import Path

import pandas as pd
from docopt import docopt
import openpyxl

from src.libs.loaders import load_tables
from src.libs.processing import process_table
from src.libs.objects import Table


def main(from_path:str, to_path:str, output:bool) -> list[Table]:
    tables = load_tables(path=from_path)
    processed_tables = beautify_docs(tables=tables)

    if output:
        output_table(processed_tables, f"{to_path}/result.xlsx")
    
    return processed_tables

def beautify_docs(tables: list[Table]) -> list[Table]:
    processed_tables = []

    for table in tables:
        processed_tables.append(process_table(table))

    return processed_tables

def output_table(tables: list[Table], path:str) -> None:
    writer = pd.ExcelWriter(path, engine = 'openpyxl')

    for i, table in enumerate(tables):
        table.df["path"] = table.path
        table.df.to_excel(writer, sheet_name = str(i))
    writer.save()
    writer.close()

if __name__ == "__main__":
    arguments = docopt(__doc__, version='Beautify table 1.0')

    from_path = arguments["--from"]
    to_path = arguments["--to"]
    if to_path[-1] == '/': to_path = to_path[:-1]
    output = arguments["--output-to-file"]

    main(from_path, to_path, output)