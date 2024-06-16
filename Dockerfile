FROM nikolaik/python-nodejs:python3.10-nodejs19

RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir -U -r requirements.txt

CMD bash start

ARG BASE_IMAGE
FROM ${BASE_IMAGE}

RUN ln -s /workspace /app

ARG pack_uid=1000
ARG pack_gid=1000

RUN groupadd koyeb --gid ${pack_gid} && \
  useradd koyeb -u ${pack_uid} -g ${pack_gid} -s /bin/bash -m

ARG STACK
LABEL io.buildpacks.stack.id="${STACK}"
USER koyeb
ENV HOME /app
