# Crie um código em Python que teste se o
# site do IEFP está acessível a partir do
# seu computador.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://iefponline.iefp.pt/IEFP/')
except:
    print('Site não está acessível')
else:
    print('O site está acessivel')

