FROM python:3.9.7
COPY requirements.txt /home
RUN pip install -r /home/requirements.txt
COPY . /home
WORKDIR /home
ENTRYPOINT ["python", "/home/beautify_table/beautify.py"]