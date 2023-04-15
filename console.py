#!/usr/bin/python3

""" module for entry point for command interpreter"""

import cmd
from models.base_model import Basemodel
from models import storage
import re
import json

class HBNBCommand(cmd.Cmd):
    prompt = 'hbnh'

    def default(self, line):
        """ default catches command if nothing else matches them"""
        print("DEF:::, line")

if __name__=='__main__':
    HBNBCommand().loop()