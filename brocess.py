#!/usr/bin/env python3

# Imports
import os
from datetime import datetime

# Variables
p_proj_log = []

# Functions
def init():

    p_proj_log.append(os.path.abspath('.brocess_log'))
    if os.path.isfile(p_proj_log[0]):
        print('Brocess used here before... do  $ rm .brocess_log  before initializing again.')
        return

    with open(p_proj_log[0], 'w+') as f:
        timestamp = datetime.now().isoformat()
        _ = f.write('Initialized @ %s\n\n'%timestamp)
        print('Initialized project log: %s'%p_proj_log[0])

    return

def load(arg):

    if os.path.isfile(arg):
        if p_proj_log:
            tmp = p_proj_log.pop()
            print('Unloaded %s'%tmp)
        p_proj_log.append(os.path.abspath(arg))
        print('Loaded project log: %s'%p_proj_log[0])
    else:
        print('Not a file: %s'%arg)

    return

def run(func_name, **kwargs):

    if not p_proj_log:
        print('Missing project log.')
        return

    output = func_name(**kwargs)
    if isinstance(output, (list, tuple)):
        output_list = list(output)
    else:
        output_list = [output]

    with open(p_proj_log[0], 'a') as f:
        f.write('%s @ %s\n'%(func_name.__name__, datetime.now().isoformat()))
        for x in kwargs:
            _ = f.write('\t%s=%s\n'%(x,kwargs[x]))
        for x in list(output_list):
            _ = f.write('\t@RETURN=%s\n'%x)
        f.write('\n')

    return(output)
