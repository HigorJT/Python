import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.cursoemvideo.com.br')
except urllib.error.URLError:
    print('O site cursoemvídeo não está acessível no momento')
else:
    print('Consegui acessar o site cursoemvideo com sucesso!')
