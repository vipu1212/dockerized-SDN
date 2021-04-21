#Author : Ajinkya Kadam
#Email : ajinkya.kadam@nyu.edu
#Program : To install RYU SDN controller and its required dependencies

apt-get update
apt-get -y install git python-pip python-dev
apt-get -y install python-eventlet python-routes python-webob python-paramiko
apt-get -y install openvswitch-switch
git clone https://github.com/osrg/ryu.git
cd ryu/;
pip install six --upgrade
pip install eventlet --upgrade
pip install oslo.config msgpack-python
pip install -r tools/pip-requires
python ./setup.py install

ryu-manager ryu.app.simple_switch_13