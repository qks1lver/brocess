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
        _ = f.write('%s\n\tInitialized\n\n'%timestamp)
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

def run(func_name, *args, **kwargs):

    if not p_proj_log:
        print('Missing project log.')
        return

    output = func_name(**kwargs)
    if isinstance(output, (list, tuple)):
        output_list = list(output)
    else:
        output_list = [output]

    with open(p_proj_log[0], 'a') as f:
        f.write('%s\n\t%s('%(datetime.now().isoformat(), func_name.__name__))
        for x in args:
            if type(x) == str:
                _ = f.write("'%s',"%x)
            else:
                _ = f.write('%s,'%x)
        for x in kwargs:
            if type(kwargs[x]) == str:
                _ = f.write("%s='%s',"%(x,kwargs[x]))
            else:
                _ = f.write('%s=%s,'%(x,kwargs[x]))
        f.write(')\n')
        for x in list(output_list):
            _ = f.write('\t@RETURN=%s\n'%x)
        f.write('\n')

    return(output)
