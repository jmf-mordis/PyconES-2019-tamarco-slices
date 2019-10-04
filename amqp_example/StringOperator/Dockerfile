FROM python:3.7 AS builder

WORKDIR /install

ARG nexus_user
ARG nexus_password

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip \
 && pip3 install --install-option="--prefix=/install" -r requirements.txt

FROM python:3.7

WORKDIR /microservice

COPY --from=builder /install /usr/local

COPY microservice.py microservice.py

CMD ["python3", "microservice.py"]
