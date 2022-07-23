import os, sys
try:
    __import__("kille").login()
except Exception as e:
    exit(str(e))
