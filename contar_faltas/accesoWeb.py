#encoding=utf-8
import urllib2
import urllib
import cookielib
def renrenBrower(url,user,password):
    # Página de inicio de sesión, se puede obtener a través del análisis de herramientas de captura de paquetes, como fiddler, wireshark
    login_page = "http://www.renren.com/PLogin.do"
    try:
                 #Obtener una instancia de cookieJar
        cj = cookielib.CookieJar()
                 #cookieJar como parámetro, obtenga una instancia del abridor
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
                 # Pretende ser un navegador normal para evitar el acceso denegado por algunos servidores web.
        opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
                 #Generar datos de publicación, incluidos nombre de usuario y contraseña de inicio de sesión.
        data = urllib.urlencode({"email":user,"password":password})
                 #Utilice el método de publicación para acceder a la página de destino, después de acceder a cookieJar guardará la cookie por sí misma
        opener.open(login_page,data)
                 #Visita la página con cookies
        op=opener.open(url)
                 # Leer el código fuente de la página
        data= op.read()
        return data
    except Exception as e:
        print str(e)
 #Acceso a la página de inicio personal de un usuario, de hecho, esto ha logrado la función de registro de Renren.
 print(renrenBrower ("http://www.renren.com/home", "nombre de usuario", "contraseña"))