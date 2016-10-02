from urllib3 import PoolManager

site = "http://raw.githubusercontent.com/PyLadiesCps/workshop_basico/master/README.md"
http = PoolManager()

requisicao = http.request('GET',site)
print requisicao.data

