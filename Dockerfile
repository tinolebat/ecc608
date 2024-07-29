FROM ubuntu:focal

ENV PIP_CACHE_HOME="~/.pipcache"
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
  wget \
  python3 \
  python3-pip 
RUN cd /usr/local/bin && ln -s /usr/bin/python3 python
RUN apt-get install -y gcc cmake vim
RUN CRYPTOAUTHLIB_NOUSB=True pip3 install cryptoauthlib==20220320 cryptography

COPY ./info.py /info.py
CMD python info.py
