#!/usr/bin/python

"""Custom topology example

"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSSwitch, Controller, RemoteController
from time import sleep


class SingleSwitchTopo(Topo):
    "Single switch connected to 4 hosts."
    def build(self):
        s1 = self.addSwitch('s1')
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)
        self.addLink(h4, s1)


def start(controller_ip='127.0.0.1'):
    setLogLevel('info')
    topo = SingleSwitchTopo()
    c1 = RemoteController('c1', ip=controller_ip)
    net = Mininet(topo=topo, controller=c1)
    net.start()
    CLI(net)
    net.stop()
