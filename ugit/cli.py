import argparse
import os
import sys

from . import data
from . import base 

def main ():
    args = parse_args()
    args.function(args)

def parse_args():
    parser = argparse.ArgumentParser()

    # Add a subparser group
    commands = parser.add_subparsers(dest='command')# 'dest' specifies where the subcommand name is stored
    commands.required = True

    init_paraser = commands.add_parser('init')
    init_paraser.set_defaults(function=init)

    hash_object_parser = commands.add_parser('hash-object')
    hash_object_parser.set_defaults(function=hash_object)
    hash_object_parser.add_argument('file')

    cat_file_parser = commands.add_parser('cat-file')
    cat_file_parser.set_defaults(function=cat_file)
    cat_file_parser.add_argument('object')

    write_tree_parser = commands.add_parser('write-tree')
    write_tree_parser.set_defaults(function=write_tree)

    return parser.parse_args()

def init(args):
    data.init()
    print (f'Initialized empty ugit repository in {os.getcwd()}\{data.GIT_DIR}')

def hash_object(args):
    with open(args.file,'rb') as f:
        print(data.hash_object(f.read()))

def cat_file(args):
    # Flush stdout to ensure no buffered output remains
    sys.stdout.flush()
    # Write binary data of the specified object to stdout
    sys.stdout.buffer.write(data.get_object(args.object,expected=None))

def write_tree(args):
   print(base.write_tree())
