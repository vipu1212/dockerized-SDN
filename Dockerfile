FROM ubuntu:18.04

LABEL Author="Divyansh Singh <divyansh.1212@gmail.com>"

USER root
WORKDIR /root

ADD ./startup.sh .
ADD ./app ./app

RUN apt-get update && apt-get install -y --no-install-recommends \
    mininet \
    openvswitch-switch \
    python3-pip \
    net-tools \
    iproute2 \
    vim

RUN pip3 install mininet

EXPOSE 6633 6653 6640

CMD sh startup.sh