from time import sleep
from random import uniform
import sys


with open('dosya.txt', 'r') as d:
    icerik = d.read()

#icerik = "Sanırım daktilo gibi yazabiliyoruz artık."

for x in icerik:
    print(x, end='', flush=True)
    sleep(0.5)
