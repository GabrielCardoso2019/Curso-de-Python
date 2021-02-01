# from subprocess import check_output
# try:
#    url = 'www.saltstack.com.br'
#    check_output(f"ping {url}", shell=True)
#    print(f'Acesso ao site {url} efetuado com sucesso')
# except Exception as err:
#    print(f'ERR: Acesso ao site {url} falhou.', err.__class__)

# ==============================================================
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://www.saltstack.com.br')
except urllib.error.URLError:
    print('O site não está acessível no momento')
else:
    print('O site foi acessado com sucesso')
    print(site.read())  # Conteúdo HTML do site
