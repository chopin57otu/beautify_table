"""Beautify tables is program for getting numerical data from ugly
data tables such as those parsed using https://github.com/tabulapdf/tabula
or converted pdf documents.

It clean tables so there is rectangle of numbers in right bottom
and row and column labels are concatenated. Load tables from docx,
directory of csv files or directory of both.

Usage:
  beautify.py --from <input_file_or_dir> --to <dir> [<filename>]

Options:
  -h --help                   Show this screen.
  --version                   Show version.
  --from <input_file_or_dir>  Input files or directory of csv files or directory of input files.
  --to <dir>                  Output directory and name of output file id single file on input.
  --output_format <format>    Output format. '.xlsx' by default

"""
from pathlib import Path

import pandas as pd
from docopt import docopt

from beautify_table.libs.loaders import load_tables_from_csv_directory, load_documents, load_tables_from_docx
from beautify_table.processing import process_table


def beautify_doc(doc: Path):
    documents = []
    path_str = str(doc)
    if doc.is_dir():
        if any(p for p in doc.glob("*.csv")):
            documents.append(load_tables_from_csv_directory(path_str))
        else:
            documents = load_documents(path_str)
    elif doc.suffix == ".docx":
        documents.append((load_tables_from_docx(path_str), doc))
    else:
        ValueError(doc.suffix + " is not recognized suffix")

    processed_tables = []
    for d, path in documents:
        # if arguments["--output_format"] is None or arguments["--output_format"] == ".xlsx":
        #     writer = pd.ExcelWriter(str(path), engine='xlsxwriter')
        for table in d:
            processed_tables.append(process_table(table))

    return processed_tables


if __name__ == "__main__":
    print("start")
    arguments = docopt(__doc__, version='Beautify table 1.0')

    print(arguments)

    # from_path = Path(arguments["--from"])
