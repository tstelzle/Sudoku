FROM python:3

WORKDIR /usr
VOLUME /usr/src

RUN apt update
RUN apt install -y wkhtmltopdf

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r /usr/requirements.txt

CMD ["bash"]
