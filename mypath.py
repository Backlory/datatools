import sys, os

path_this, name = os.path.split(os.path.abspath(__file__))
sys.path.append(path_this)

from _tools._mypath import *
