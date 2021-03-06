# Dockerfile, Image, Container

FROM python:3.8

ADD . .

RUN make install

CMD ["python", "store_manager.py"]

