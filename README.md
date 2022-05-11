# Table beautifier

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