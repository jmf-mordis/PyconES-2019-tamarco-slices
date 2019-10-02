FROM artifacts.s73cloud.com/python:3.7.0 AS builder

WORKDIR /install

ARG nexus_user
ARG nexus_password

COPY requirements.txt requirements.txt

# hadolint ignore=DL3013
RUN sed -ie "s/<USER>/${nexus_user}/g" /root/.pip/pip.conf \
 && sed -ie "s/<PASSWORD>/${nexus_password}/g" /root/.pip/pip.conf \
 && pip3 install --upgrade pip \
 && pip3 install --install-option="--prefix=/install" -r requirements.txt


FROM artifacts.s73cloud.com/python:3.7.0

WORKDIR /microservice

COPY --from=builder /install /usr/local

COPY microservice.py microservice.py

CMD ["python3", "microservice.py"]
