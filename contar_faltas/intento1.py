
import urllib.parse
import urllib.request

url = 'https://seneca.juntadeandalucia.es/seneca/jsp/portal/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {'usuario': 'mcarceb395',
          'clave_p': 'hola',
          'language': 'Python' }
headers = {'User-Agent': user_agent}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data, headers)
with urllib.request.urlopen(req) as response:
   the_page = response.read()
   print(the_page)
