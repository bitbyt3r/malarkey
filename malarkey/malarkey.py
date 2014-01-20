# -*- coding: utf-8 -*-
import jsonDB as db
import socket
import os
import imp

client = socket.gethostname()


def loadFromFile(filepath):
    class_inst = None
    expected_class = 'Main'

    mod_name, file_ext = os.path.splitext(os.path.split(filepath)[-1])

    if file_ext.lower() == '.py':
        py_mod = imp.load_source(mod_name, filepath)

    elif file_ext.lower() == '.pyc':
        py_mod = imp.load_compiled(mod_name, filepath)

    if hasattr(py_mod, expected_class):
        class_inst = py_mod.MyClass()

    return class_inst

config = db.getConfig(client)
for adapter in config.adapters:
    adapter.inst = loadFromFile(adapter.path)
    adapter.inst.run(adapter.config)