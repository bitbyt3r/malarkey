# -*- coding: utf-8 -*-
import json


def __init__(self):
    self.conf = Config()
    with open("./malarkey.conf", "r") as confFile:
        self.conf.raw = json.load(confFile)


def getConfig(self, clientName):
    client = self.conf.resolveClient(clientName)
    return client


class Config(object):
    """A container for the stored config"""

    def __init__(self):
        self.adapters = []
        self.raw = {}

    def resolveClient(self, clientName):
        if clientName in self.raw:


class Adapter(object):
    """Adapters are helper modules and associated configuration"""

    def __init__(self):
        self.inst = None
        self.path = ""
        self.config = {}

class Client(object):
    """Clients hold a single system worth of configuration"""

    def __init__(self):
        self.name = ""
        self.adapters = []
        self.profiles = []
