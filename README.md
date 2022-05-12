# Table beautifier

## Build
`python setup.py sdist bdist_wheel`

## Install
`pip install dist/beautify_table-1.0-py3-none-any.whl`
`pip install beautify_table` (from PyPi)

## Run
### Locally
```bash
python beautify_table/beautify.py \
    --from "<path-to-folder-with-csv-or-docx>" \
    --to "<path-to-save-result-into>" \
    --output-to-file
```

### In docker
```bash
docker run -it \
    -v /path/to/folder:/home/data beautify \
    --from /home/data \
    --to . \
    --output-to-file
```