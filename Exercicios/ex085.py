from urlib import request

site = 'https://iefp.pt'
try:
    codigo = request.urlopen(site).getcode()
except:
    