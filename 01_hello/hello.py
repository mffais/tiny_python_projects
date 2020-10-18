#!/usr/bin/env python3
# Purpose: Say Hello

import argparse
parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('-n','--name',metavar='name',default='World',help='Name to great')
args = parser.parse_args()
print('Hello, ' + args.name + '!')
