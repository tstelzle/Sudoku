FROM python:3

WORKDIR /usr
VOLUME /usr/src

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r /usr/requirements.txt

CMD ["bash"]
