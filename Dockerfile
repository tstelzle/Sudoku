FROM python:3

WORKDIR /usr/src
VOLUME /usr/src

RUN apt update
RUN apt install -y wkhtmltopdf

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r /usr/src/requirements.txt

CMD ["bash"]
