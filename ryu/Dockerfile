FROM ubuntu:18.04

USER root
WORKDIR /root

ADD ./ryu ./

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    python-pip \
    python-dev \
    python-eventlet python-routes python-webob python-paramiko \
    openvswitch-switch \
    python-setuptools

RUN cd ryu/

RUN python -m pip install --upgrade pip  
RUN pip install setuptools --upgrade 
RUN pip install six --upgrade
RUN pip install eventlet --upgrade
RUN pip install oslo.config msgpack-python
RUN pip install -r tools/pip-requires
RUN python ./setup.py install

EXPOSE 6633 6653 6640

CMD ryu-manager ryu.app.simple_switch_13