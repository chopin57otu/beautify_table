# Table beautifier

## About
Beautify table is program for getting numerical data from ugly
data tables such as those parsed using [Tabula](https://github.com/tabulapdf/tabula)
or tables in MS Word DOCX documents.

It clean tables so there is rectangle of numbers in right bottom
and row and column labels are concatenated. Load tables from docx,
directory of csv files or directory of both.
```
Usage:
  beautify.py --from <input_file_or_dir> [--output-to-file] [--to <dir>]

Options:
  -h --help                   Show this screen.
  --from <input_file_or_dir>  Input files or directory of csv files or directory of input files.
  --output-to-file            Optional Whether to output result to file (.xlsx).
  --to <dir>                  Optional Output directory if --output-to-file is True.
```

## Build (wheel package)
```bash
pip install wheel
python setup.py bdist_wheel
```

## Install
* `pip install dist/*` or
* `pip install beautify_table` (from PyPi)

## Run
### From command line
```bash
python beautify_table/beautify.py \
    --from "<path-to-folder-with-csv-or-docx>" \
    --output-to-file \
    --to "<path-to-save-result-into>"
```

### As python package
```python
from beautify_table.beautify import main as get_beautiful_tables
btables = get_beautiful_tables(
    from_path=input_path, 
    output=True,
    to_path=output_path
) # returns list of Table objects
```

### In docker
```bash
docker run -it \
    -v /path/to/folder:/home/data beautify \
    --from /home/data \
    --output-to-file \
    --to .
```