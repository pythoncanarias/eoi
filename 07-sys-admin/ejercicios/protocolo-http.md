# Ejercicio 1: Peticiones HTTP usando Sockets

Aquí un ejemplo de petición via sockets


```python
import ssl
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('google.com', 443))
s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_SSLv23)
s.sendall(b"GET / HTTP/1.1\r\nHost:www.google.com\r\n\r\n")
data = s.recv(1024)
print(data)
```

    b'HTTP/1.1 200 OK\r\nDate: Sat, 24 Apr 2021 16:03:52 GMT\r\nExpires: -1\r\nCache-Control: private, max-age=0\r\nContent-Type: text/html; charset=ISO-8859-1\r\nP3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."\r\nServer: gws\r\nX-XSS-Protection: 0\r\nX-Frame-Options: SAMEORIGIN\r\nSet-Cookie: CONSENT=PENDING+183; expires=Fri, 01-Jan-2038 00:00:00 GMT; path=/; domain=.google.com\r\nAlt-Svc: h3-29=":443"; ma=2592000,h3-T051=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"\r\nAccept-Ranges: none\r\nVary: Accept-Encoding\r\nTransfer-Encoding: chunked\r\n\r\n5223\r\n<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="es"><head><meta content="Google.es permite acceder a la informaci\xf3n mundial en castellano, catal\xe1n, gallego, euskara e ingl\xe9s." name="description"><meta content="noodp" name="robots"><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_'


Crear un socket que haga una petición a la web [ifconfig.io](http://ifconfig.io) para obtener nuestra IP pública
> Punto extra! formatea la salida para mostrar SOLO LA IP, sin el resto del texto


```python
import socket

with socket.socket() as s:
    s.connect(('ifconfig.io', 80))
    s.sendall(b'GET / HTTP/1.1\r\nHost: ifconfig.io\r\nUser-Agent: curl\r\n\r\n')
    data = s.recv(1024)
    data_str = data.decode('ascii')
    ip = data_str.split('\r\n\r\n')[1].rstrip()
    print(ip)
```

    83.50.235.155


# Ejercicio 2: HTTP protocol client con Python

Establecemos una conexión con la web `www.python.org`


```python
import http.client

conn = http.client.HTTPSConnection("www.python.org")
print(conn)
```

    <http.client.HTTPSConnection object at 0x7fa3d836fca0>


## Peticiones GET

Lanzamos una petición GET para obtener la información de esa página


```python
conn.request("GET", "/")
```

A continuación vamos a guardar la respuesta en un objeto e inspeccionar el resultado


```python
r1 = conn.getresponse()
print(r1)
```

    <http.client.HTTPResponse object at 0x7fa3d836fe80>


Los campos disponibles en el objeto `HTTPResponse` puedes encontrarlos en la [documentación oficial de Python](https://docs.python.org/3/library/http.client.html#httpresponse-objects).

Vamos a inspeccionar los principales:


```python
print(r1.status, r1.reason)
```

    200 OK



```python
data1 = r1.read()  # This will return entire content.
print(data1)
```

    b'<!doctype html>\n<!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->\n<!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]-->\n<!--[if IE 8]>      <html class="no-js ie8 lt-ie9">                 <![endif]-->\n<!--[if gt IE 8]><!--><html class="no-js" lang="en" dir="ltr">  <!--<![endif]-->\n\n<head>\n    <meta charset="utf-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n\n    <link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">\n    <link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js">\n\n    <meta name="application-name" content="Python.org">\n    <meta name="msapplication-tooltip" content="The official home of the Python Programming Language">\n    <meta name="apple-mobile-web-app-title" content="Python.org">\n    <meta name="apple-mobile-web-app-capable" content="yes">\n    <meta name="apple-mobile-web-app-status-bar-style" content="black">\n\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <meta name="HandheldFriendly" content="True">\n    <meta name="format-detection" content="telephone=no">\n    <meta http-equiv="cleartype" content="on">\n    <meta http-equiv="imagetoolbar" content="false">\n\n    <script src="/static/js/libs/modernizr.js"></script>\n\n    <link href="/static/stylesheets/style.5cd40467dffc.css" rel="stylesheet" type="text/css" title="default" />\n    <link href="/static/stylesheets/mq.e887b902092b.css" rel="stylesheet" type="text/css" media="not print, braille, embossed, speech, tty" />\n    \n\n    <!--[if (lte IE 8)&(!IEMobile)]>\n    <link href="/static/stylesheets/no-mq.bf0c425cdb73.css" rel="stylesheet" type="text/css" media="screen" />\n    \n    \n    <![endif]-->\n    <link rel="stylesheet" href="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css">\n\n    \n    <link rel="icon" type="image/x-icon" href="/static/favicon.ico">\n    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/static/apple-touch-icon-144x144-precomposed.png">\n    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/static/apple-touch-icon-114x114-precomposed.png">\n    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="/static/apple-touch-icon-72x72-precomposed.png">\n    <link rel="apple-touch-icon-precomposed" href="/static/apple-touch-icon-precomposed.png">\n    <link rel="apple-touch-icon" href="/static/apple-touch-icon-precomposed.png">\n\n    \n    <meta name="msapplication-TileImage" content="/static/metro-icon-144x144-precomposed.png"><!-- white shape -->\n    <meta name="msapplication-TileColor" content="#3673a5"><!-- python blue -->\n    <meta name="msapplication-navbutton-color" content="#3673a5">\n\n    <title>Welcome to Python.org</title>\n\n    <meta name="description" content="The official home of the Python Programming Language">\n    <meta name="keywords" content="Python programming language object oriented web free open source software license documentation download community">\n\n    \n    <meta property="og:type" content="website">\n    <meta property="og:site_name" content="Python.org">\n    <meta property="og:title" content="Welcome to Python.org">\n    <meta property="og:description" content="The official home of the Python Programming Language">\n    \n    <meta property="og:image" content="https://www.python.org/static/opengraph-icon-200x200.png">\n    <meta property="og:image:secure_url" content="https://www.python.org/static/opengraph-icon-200x200.png">\n    \n    <meta property="og:url" content="https://www.python.org/">\n\n    <link rel="author" href="/static/humans.txt">\n\n    <link rel="alternate" type="application/rss+xml" title="Python Enhancement Proposals"\n          href="https://www.python.org/dev/peps/peps.rss/">\n    <link rel="alternate" type="application/rss+xml" title="Python Job Opportunities"\n          href="https://www.python.org/jobs/feed/rss/">\n    <link rel="alternate" type="application/rss+xml" title="Python Software Foundation News"\n          href="https://feeds.feedburner.com/PythonSoftwareFoundationNews">\n    <link rel="alternate" type="application/rss+xml" title="Python Insider"\n          href="https://feeds.feedburner.com/PythonInsider">\n\n    \n\n    \n    <script type="application/ld+json">\n     {\n       "@context": "https://schema.org",\n       "@type": "WebSite",\n       "url": "https://www.python.org/",\n       "potentialAction": {\n         "@type": "SearchAction",\n         "target": "https://www.python.org/search/?q={search_term_string}",\n         "query-input": "required name=search_term_string"\n       }\n     }\n    </script>\n\n    \n    <script type="text/javascript">\n    var _gaq = _gaq || [];\n    _gaq.push([\'_setAccount\', \'UA-39055973-1\']);\n    _gaq.push([\'_trackPageview\']);\n\n    (function() {\n        var ga = document.createElement(\'script\'); ga.type = \'text/javascript\'; ga.async = true;\n        ga.src = (\'https:\' == document.location.protocol ? \'https://ssl\' : \'http://www\') + \'.google-analytics.com/ga.js\';\n        var s = document.getElementsByTagName(\'script\')[0]; s.parentNode.insertBefore(ga, s);\n    })();\n    </script>\n    \n</head>\n\n<body class="python home" id="homepage">\n\n    <div id="touchnav-wrapper">\n\n        <div id="nojs" class="do-not-print">\n            <p><strong>Notice:</strong> While Javascript is not essential for this website, your interaction with the content will be limited. Please turn Javascript on for the full experience. </p>\n        </div>\n\n        <!--[if lte IE 8]>\n        <div id="oldie-warning" class="do-not-print">\n            <p>\n                <strong>Notice:</strong> Your browser is <em>ancient</em>. Please\n                <a href="http://browsehappy.com/">upgrade to a different browser</a> to experience a better web.\n            </p>\n        </div>\n        <![endif]-->\n\n        <!-- Sister Site Links -->\n        <div id="top" class="top-bar do-not-print">\n\n            <nav class="meta-navigation container" role="navigation">\n\n                \n                <div class="skip-link screen-reader-text">\n                    <a href="#content" title="Skip to content">Skip to content</a>\n                </div>\n\n                \n                <a id="close-python-network" class="jump-link" href="#python-network" aria-hidden="true">\n                    <span aria-hidden="true" class="icon-arrow-down"><span>&#9660;</span></span> Close\n                </a>\n\n                \n\n<ul class="menu" role="tree">\n    \n    <li class="python-meta current_item selectedcurrent_branch selected">\n        <a href="/" title="The Python Programming Language" class="current_item selectedcurrent_branch selected">Python</a>\n    </li>\n    \n    <li class="psf-meta ">\n        <a href="/psf-landing/" title="The Python Software Foundation" >PSF</a>\n    </li>\n    \n    <li class="docs-meta ">\n        <a href="https://docs.python.org" title="Python Documentation" >Docs</a>\n    </li>\n    \n    <li class="pypi-meta ">\n        <a href="https://pypi.org/" title="Python Package Index" >PyPI</a>\n    </li>\n    \n    <li class="jobs-meta ">\n        <a href="/jobs/" title="Python Job Board" >Jobs</a>\n    </li>\n    \n    <li class="shop-meta ">\n        <a href="/community-landing/"  >Community</a>\n    </li>\n    \n</ul>\n\n\n                <a id="python-network" class="jump-link" href="#top" aria-hidden="true">\n                    <span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> The Python Network\n                </a>\n\n            </nav>\n\n        </div>\n\n        <!-- Header elements -->\n        <header class="main-header" role="banner">\n            <div class="container">\n\n                <h1 class="site-headline">\n                    <a href="/"><img class="python-logo" src="/static/img/python-logo.png" alt="python&trade;"></a>\n                </h1>\n\n                <div class="options-bar-container do-not-print">\n                    <a href="https://psfmember.org/civicrm/contribute/transact?reset=1&id=2" class="donate-button">Donate</a>\n                    <div class="options-bar">\n                        \n                        <a id="site-map-link" class="jump-to-menu" href="#site-map"><span class="menu-icon">&equiv;</span> Menu</a><form class="search-the-site" action="/search/" method="get">\n                            <fieldset title="Search Python.org">\n\n                                <span aria-hidden="true" class="icon-search"></span>\n\n                                <label class="screen-reader-text" for="id-search-field">Search This Site</label>\n                                <input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" tabindex="1">\n\n                                <button type="submit" name="submit" id="submit" class="search-button" title="Submit this Search" tabindex="3">\n                                    GO\n                                </button>\n\n                                \n                                <!--[if IE]><input type="text" style="display: none;" disabled="disabled" size="1" tabindex="4"><![endif]-->\n\n                            </fieldset>\n                        </form><span class="breaker"></span><div class="adjust-font-size" aria-hidden="true">\n                            <ul class="navigation menu" aria-label="Adjust Text Size on Page">\n                                <li class="tier-1 last" aria-haspopup="true">\n                                    <a href="#" class="action-trigger"><strong><small>A</small> A</strong></a>\n                                    <ul class="subnav menu">\n                                        <li class="tier-2 element-1" role="treeitem"><a class="text-shrink" title="Make Text Smaller" href="javascript:;">Smaller</a></li>\n                                        <li class="tier-2 element-2" role="treeitem"><a class="text-grow" title="Make Text Larger" href="javascript:;">Larger</a></li>\n                                        <li class="tier-2 element-3" role="treeitem"><a class="text-reset" title="Reset any font size changes I have made" href="javascript:;">Reset</a></li>\n                                    </ul>\n                                </li>\n                            </ul>\n                        </div><div class="winkwink-nudgenudge">\n                            <ul class="navigation menu" aria-label="Social Media Navigation">\n                                <li class="tier-1 last" aria-haspopup="true">\n                                    <a href="#" class="action-trigger">Socialize</a>\n                                    <ul class="subnav menu">\n                                        <li class="tier-2 element-1" role="treeitem"><a href="https://www.facebook.com/pythonlang?fref=ts"><span aria-hidden="true" class="icon-facebook"></span>Facebook</a></li>\n                                        <li class="tier-2 element-2" role="treeitem"><a href="https://twitter.com/ThePSF"><span aria-hidden="true" class="icon-twitter"></span>Twitter</a></li>\n                                        <li class="tier-2 element-3" role="treeitem"><a href="/community/irc/"><span aria-hidden="true" class="icon-freenode"></span>Chat on IRC</a></li>\n                                    </ul>\n                                </li>\n                            </ul>\n                        </div>\n                        <span data-html-include="/authenticated"></span>\n                    </div><!-- end options-bar -->\n                </div>\n\n                <nav id="mainnav" class="python-navigation main-navigation do-not-print" role="navigation">\n                    \n                        \n<ul class="navigation menu" role="menubar" aria-label="Main Navigation">\n  \n    \n    \n    <li id="about" class="tier-1 element-1  " aria-haspopup="true">\n        <a href="/about/" title="" class="">About</a>\n        \n            \n\n<ul class="subnav menu" role="menu" aria-hidden="true">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    \n    \n    <li id="downloads" class="tier-1 element-2  " aria-haspopup="true">\n        <a href="/downloads/" title="" class="">Downloads</a>\n        \n            \n\n<ul class="subnav menu" role="menu" aria-hidden="true">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/downloads/mac-osx/" title="">Mac OS X</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    \n    \n    <li id="documentation" class="tier-1 element-3  " aria-haspopup="true">\n        <a href="/doc/" title="" class="">Documentation</a>\n        \n            \n\n<ul class="subnav menu" role="menu" aria-hidden="true">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner&#39;s Guide</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="https://devguide.python.org/" title="">Developer&#39;s Guide</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="http://python.org/dev/peps/" title="">PEP Index</a></li>\n    \n        <li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>\n    \n        <li class="tier-2 element-9" role="treeitem"><a href="/doc/essays/" title="">Python Essays</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    \n    \n    <li id="community" class="tier-1 element-4  " aria-haspopup="true">\n        <a href="/community/" title="" class="">Community</a>\n        \n            \n\n<ul class="subnav menu" role="menu" aria-hidden="true">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/community/survey" title="">Community Survey</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="/community/forums/" title="">Forums</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="/psf/annual-report/2020/" title="">PSF Annual Impact Report</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>\n    \n        <li class="tier-2 element-8" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>\n    \n        <li class="tier-2 element-9" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>\n    \n        <li class="tier-2 element-10" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>\n    \n        <li class="tier-2 element-11" role="treeitem"><a href="/community/merchandise/" title="">Merchandise</a></li>\n    \n        <li class="tier-2 element-12" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>\n    \n        <li class="tier-2 element-13" role="treeitem"><a href="/psf/conduct/" title="">Code of Conduct</a></li>\n    \n        <li class="tier-2 element-14" role="treeitem"><a href="/psf/get-involved/" title="">Get Involved</a></li>\n    \n        <li class="tier-2 element-15" role="treeitem"><a href="/psf/community-stories/" title="">Shared Stories</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    \n    \n    <li id="success-stories" class="tier-1 element-5  " aria-haspopup="true">\n        <a href="/success-stories/" title="success-stories" class="">Success Stories</a>\n        \n            \n\n<ul class="subnav menu" role="menu" aria-hidden="true">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/success-stories/category/arts/" title="">Arts</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/success-stories/category/business/" title="">Business</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/success-stories/category/education/" title="">Education</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/success-stories/category/engineering/" title="">Engineering</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="/success-stories/category/government/" title="">Government</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="/success-stories/category/scientific/" title="">Scientific</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="/success-stories/category/software-development/" title="">Software Development</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    \n    \n    <li id="news" class="tier-1 element-6  " aria-haspopup="true">\n        <a href="/blogs/" title="News from around the Python world" class="">News</a>\n        \n            \n\n<ul class="subnav menu" role="menu" aria-hidden="true">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/psf/newsletter/" title="Python Software Foundation Newsletter">PSF Newsletter</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">Community News</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon News</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    \n    \n    <li id="events" class="tier-1 element-7  " aria-haspopup="true">\n        <a href="/events/" title="" class="">Events</a>\n        \n            \n\n<ul class="subnav menu" role="menu" aria-hidden="true">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/events/python-events" title="">Python Events</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    \n    \n    \n  \n</ul>\n\n                    \n                </nav>\n\n                <div class="header-banner "> <!-- for optional "do-not-print" class -->\n                    \n        <div id="dive-into-python" class="flex-slideshow slideshow">\n\n            <ul class="launch-shell menu" id="launch-shell">\n                <li>\n                    <a class="button prompt" id="start-shell" data-shell-container="#dive-into-python" href="/shell/">&gt;_\n                        <span class="message">Launch Interactive Shell</span>\n                    </a>\n                </li>\n            </ul>\n\n            <ul class="slides menu">\n                \n                <li>\n                    <div class="slide-code"><pre><code><span class="comment"># Python 3: Fibonacci series up to n</span>\r\n>>> def fib(n):\r\n>>>     a, b = 0, 1\r\n>>>     while a &lt; n:\r\n>>>         print(a, end=\' \')\r\n>>>         a, b = b, a+b\r\n>>>     print()\r\n>>> fib(1000)\r\n<span class="output">0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987</span></code></pre></div>\n                    <div class="slide-copy"><h1>Functions Defined</h1>\r\n<p>The core of extensible programming is defining functions. Python allows mandatory and optional arguments, keyword arguments, and even arbitrary argument lists. <a href="//docs.python.org/3/tutorial/controlflow.html#defining-functions">More about defining functions in Python&nbsp;3</a></p></div>\n                </li>\n                \n                <li>\n                    <div class="slide-code"><pre><code><span class="comment"># Python 3: List comprehensions</span>\r\n>>> fruits = [\'Banana\', \'Apple\', \'Lime\']\r\n>>> loud_fruits = [fruit.upper() for fruit in fruits]\r\n>>> print(loud_fruits)\r\n<span class="output">[\'BANANA\', \'APPLE\', \'LIME\']</span>\r\n\r\n<span class="comment"># List and the enumerate function</span>\r\n>>> list(enumerate(fruits))\r\n<span class="output">[(0, \'Banana\'), (1, \'Apple\'), (2, \'Lime\')]</span></code></pre></div>\n                    <div class="slide-copy"><h1>Compound Data Types</h1>\r\n<p>Lists (known as arrays in other languages) are one of the compound data types that Python understands. Lists can be indexed, sliced and manipulated with other built-in functions. <a href="//docs.python.org/3/tutorial/introduction.html#lists">More about lists in Python&nbsp;3</a></p></div>\n                </li>\n                \n                <li>\n                    <div class="slide-code"><pre><code><span class="comment"># Python 3: Simple arithmetic</span>\r\n>>> 1 / 2\r\n<span class="output">0.5</span>\r\n>>> 2 ** 3\r\n<span class="output">8</span>\r\n>>> 17 / 3  <span class="comment"># classic division returns a float</span>\r\n<span class="output">5.666666666666667</span>\r\n>>> 17 // 3  <span class="comment"># floor division</span>\r\n<span class="output">5</span></code></pre></div>\n                    <div class="slide-copy"><h1>Intuitive Interpretation</h1>\r\n<p>Calculations are simple with Python, and expression syntax is straightforward: the operators <code>+</code>, <code>-</code>, <code>*</code> and <code>/</code> work as expected; parentheses <code>()</code> can be used for grouping. <a href="http://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator">More about simple math functions in Python&nbsp;3</a>.</p></div>\n                </li>\n                \n                <li>\n                    <div class="slide-code"><pre><code><span class="comment"># Python 3: Simple output (with Unicode)</span>\r\n>>> print("Hello, I\'m Python!")\r\n<span class="output">Hello, I\'m Python!</span>\r\n\r\n<span class="comment"># Input, assignment</span>\r\n>>> name = input(\'What is your name?\\n\')\r\n>>> print(\'Hi, %s.\' % name)\r\n<span class="output">What is your name?\r\nPython\r\nHi, Python.</span></code></pre></div>\n                    <div class="slide-copy"><h1>Quick &amp; Easy to Learn</h1>\r\n<p>Experienced programmers in any other language can pick up Python very quickly, and beginners find the clean syntax and indentation structure easy to learn. <a href="//docs.python.org/3/tutorial/">Whet your appetite</a> with our Python&nbsp;3 overview.</p>\r\n                   </div>\n                </li>\n                \n                <li>\n                    <div class="slide-code"><pre><code><span class="comment"># For loop on a list</span>\r\n>>> numbers = [2, 4, 6, 8]\r\n>>> product = 1\r\n>>> for number in numbers:\r\n...    product = product * number\r\n... \r\n>>> print(\'The product is:\', product)\r\n<span class="output">The product is: 384</span></code></pre></div>\n                    <div class="slide-copy"><h1>All the Flow You&rsquo;d Expect</h1>\r\n<p>Python knows the usual control flow statements that other languages speak &mdash; <code>if</code>, <code>for</code>, <code>while</code> and <code>range</code> &mdash; with some of its own twists, of course. <a href="//docs.python.org/3/tutorial/controlflow.html">More control flow tools in Python&nbsp;3</a></p></div>\n                </li>\n                \n            </ul>\n        </div>\n\n\n                </div>\n\n                \n        <div class="introduction">\n            <p>Python is a programming language that lets you work quickly <span class="breaker"></span>and integrate systems more effectively. <a class="readmore" href="/doc/">Learn More</a></p>\n        </div>\n\n\n             </div><!-- end .container -->\n        </header>\n\n        <div id="content" class="content-wrapper">\n            <!-- Main Content Column -->\n            <div class="container">\n\n                <section class="main-content " role="main">\n\n                    \n                    \n\n                    \n\n                    \n\n                \n\n                <div class="row">\n\n                    <div class="small-widget get-started-widget">\n                        <h2 class="widget-title"><span aria-hidden="true" class="icon-get-started"></span>Get Started</h2>\r\n<p>Whether you\'re new to programming or an experienced developer, it\'s easy to learn and use Python.</p>\r\n<p><a href="/about/gettingstarted/">Start with our Beginner&rsquo;s Guide</a></p>\n                    </div>\n\n                    <div class="small-widget download-widget">\n                        <h2 class="widget-title"><span aria-hidden="true" class="icon-download"></span>Download</h2>\n<p>Python source code and installers are available for download for all versions!</p>\n<p>Latest: <a href="/downloads/release/python-394/">Python 3.9.4</a></p>\n                    </div>\n\n                    <div class="small-widget documentation-widget">\n                        <h2 class="widget-title"><span aria-hidden="true" class="icon-documentation"></span>Docs</h2>\r\n<p>Documentation for Python\'s standard library, along with tutorials and guides, are available online.</p>\r\n<p><a href="https://docs.python.org">docs.python.org</a></p>\n                    </div>\n\n                    <div class="small-widget jobs-widget last">\n                        <h2 class="widget-title"><span aria-hidden="true" class="icon-jobs"></span>Jobs</h2>\r\n<p>Looking for work or have a Python related position that you\'re trying to hire for? Our <strong>relaunched community-run job board</strong> is the place to go.</p>\r\n<p><a href="//jobs.python.org">jobs.python.org</a></p>\n                    </div>\n\n                </div>\n\n                <div class="list-widgets row">\n\n                    <div class="medium-widget blog-widget">\n                        \n                        <div class="shrubbery">\n                        \n                            <h2 class="widget-title"><span aria-hidden="true" class="icon-news"></span>Latest News</h2>\n                            <p class="give-me-more"><a href="https://blog.python.org" title="More News">More</a></p>\n                            \n                            <ul class="menu">\n                                \n                                \n                                <li>\n<time datetime="2021-04-23T18:23:00.000004+00:00"><span class="say-no-more">2021-</span>04-23</time>\n <a href="http://feedproxy.google.com/~r/PythonSoftwareFoundationNews/~3/-01rNDGeJjI/python-software-foundation-fellow.html">Python Software Foundation Fellow Members for Q1 2021</a></li>\n                                \n                                <li>\n<time datetime="2021-04-13T15:00:00.000001+00:00"><span class="say-no-more">2021-</span>04-13</time>\n <a href="http://feedproxy.google.com/~r/PythonSoftwareFoundationNews/~3/BWmRSi2H2PE/the-psf-is-hiring-python-packaging.html">The PSF is hiring a Python Packaging Project Manager!</a></li>\n                                \n                                <li>\n<time datetime="2021-04-06T15:15:00.000001+00:00"><span class="say-no-more">2021-</span>04-06</time>\n <a href="http://feedproxy.google.com/~r/PythonSoftwareFoundationNews/~3/wXMXO2mnbPQ/the-psf-is-hiring-developer-in.html">The PSF is hiring a Developer-in-Residence to support CPython!</a></li>\n                                \n                                <li>\n<time datetime="2021-04-06T11:30:00.000001+00:00"><span class="say-no-more">2021-</span>04-06</time>\n <a href="http://feedproxy.google.com/~r/PythonInsider/~3/J8arUjJC_XY/python-3100a7-is-now-available-for.html">Python 3.10.0a7 is now available for testing</a></li>\n                                \n                                <li>\n<time datetime="2021-04-06T11:30:00.000001+00:00"><span class="say-no-more">2021-</span>04-06</time>\n <a href="http://feedproxy.google.com/~r/PythonInsider/~3/HVZUgOL8qJA/python-3100a7-is-now-available-for.html">Python 3.10.0a7 is now available for testing</a></li>\n                                \n                            </ul>\n                        </div><!-- end .shrubbery -->\n\n                    </div>\n\n                    <div class="medium-widget event-widget last">\n                        \n                        <div class="shrubbery">\n                        \n                            <h2 class="widget-title"><span aria-hidden="true" class="icon-calendar"></span>Upcoming Events</h2>\n                            <p class="give-me-more"><a href="/events/calendars/" title="More Events">More</a></p>\n                            \n                            <ul class="menu">\n                                \n                                \n                                \n                                <li>\n<time datetime="2021-05-12T00:00:00+00:00"><span class="say-no-more">2021-</span>05-12</time>\n <a href="/events/python-events/893/">PyCon US 2021</a></li>\n                                \n                                \n                                \n                                <li>\n<time datetime="2021-05-26T16:30:00+00:00"><span class="say-no-more">2021-</span>05-26</time>\n <a href="/events/python-user-group/1090/">An introduction to Web Scraping with Python and Azure Functions - PyLadies Amsterdam</a></li>\n                                \n                                \n                                \n                                <li>\n<time datetime="2021-05-27T00:00:00+00:00"><span class="say-no-more">2021-</span>05-27</time>\n <a href="/events/python-events/1088/">Conf42 Python 2021</a></li>\n                                \n                                \n                                \n                                <li>\n<time datetime="2021-06-02T00:00:00+00:00"><span class="say-no-more">2021-</span>06-02</time>\n <a href="/events/python-events/1048/"> DjangoCon Europe 2021</a></li>\n                                \n                                \n                                \n                                <li>\n<time datetime="2021-06-18T00:00:00+00:00"><span class="say-no-more">2021-</span>06-18</time>\n <a href="/events/python-events/1036/">PyCon Namibia 2021</a></li>\n                                \n                                \n                            </ul>\n                        </div>\n\n                    </div>\n\n                </div>\n\n                <div class="row">\n\n                    <div class="medium-widget success-stories-widget">\n                        \n\n\n\n                        <div class="shrubbery">\n                            \n\n                            <h2 class="widget-title"><span aria-hidden="true" class="icon-success-stories"></span>Success Stories</h2>\n                            <p class="give-me-more"><a href="/success-stories/" title="More Success Stories">More</a></p>\n\n                            \n                            <div class="success-story-item" id="success-story-932">\n\n                            <blockquote>\n                                <a href="/success-stories/abridging-clinical-conversations-using-python/">Python powers major aspects of Abridge\xe2\x80\x99s ML lifecycle, including data annotation,  research and experimentation, and ML model deployment to production.</a>\n                            </blockquote>\n\n                            <table cellpadding="0" cellspacing="0" border="0" width="100%" class="quote-from">\n                                <tbody>\n                                    <tr>\n                                        \n                                        <td><p><a href="/success-stories/abridging-clinical-conversations-using-python/">Abridging clinical conversations using Python</a> <em>by Nimshi Venkat and Sandeep Konam</em></p></td>\n                                    </tr>\n                                </tbody>\n                            </table>\n                            </div>\n                            \n\n                        </div><!-- end .shrubbery -->\n\n                    </div>\n\n                    <div class="medium-widget applications-widget last">\n                        <div class="shrubbery">\n                            <h2 class="widget-title"><span aria-hidden="true" class="icon-python"></span>Use Python for&hellip;</h2>\r\n<p class="give-me-more"><a href="/about/apps" title="More Applications">More</a></p>\r\n\r\n<ul class="menu">\r\n    <li><b>Web Development</b>:\r\n        <span class="tag-wrapper"><a class="tag" href="http://www.djangoproject.com/">Django</a>, <a class="tag" href="http://www.pylonsproject.org/">Pyramid</a>, <a class="tag" href="http://bottlepy.org">Bottle</a>, <a class="tag" href="http://tornadoweb.org">Tornado</a>, <a href="http://flask.pocoo.org/" class="tag">Flask</a>, <a class="tag" href="http://www.web2py.com/">web2py</a></span></li>\r\n    <li><b>GUI Development</b>:\r\n        <span class="tag-wrapper"><a class="tag" href="http://wiki.python.org/moin/TkInter">tkInter</a>, <a class="tag" href="https://wiki.gnome.org/Projects/PyGObject">PyGObject</a>, <a class="tag" href="http://www.riverbankcomputing.co.uk/software/pyqt/intro">PyQt</a>, <a class="tag" href="https://wiki.qt.io/PySide">PySide</a>, <a class="tag" href="https://kivy.org/">Kivy</a>, <a class="tag" href="http://www.wxpython.org/">wxPython</a></span></li>\r\n    <li><b>Scientific and Numeric</b>:\r\n        <span class="tag-wrapper">\r\n<a class="tag" href="http://www.scipy.org">SciPy</a>, <a class="tag" href="http://pandas.pydata.org/">Pandas</a>, <a href="http://ipython.org" class="tag">IPython</a></span></li>\r\n    <li><b>Software Development</b>:\r\n        <span class="tag-wrapper"><a class="tag" href="http://buildbot.net/">Buildbot</a>, <a class="tag" href="http://trac.edgewall.org/">Trac</a>, <a class="tag" href="http://roundup.sourceforge.net/">Roundup</a></span></li>\r\n    <li><b>System Administration</b>:\r\n        <span class="tag-wrapper"><a class="tag" href="http://www.ansible.com">Ansible</a>, <a class="tag" href="http://www.saltstack.com">Salt</a>, <a class="tag" href="https://www.openstack.org">OpenStack</a></span></li>\r\n</ul>\r\n\n                        </div><!-- end .shrubbery -->\n                    </div>\n\n                </div>\n\n                \n                <div class="pep-widget">\n\n                    <h2 class="widget-title">\n                        <span class="prompt">&gt;&gt;&gt;</span> <a href="/dev/peps/">Python Enhancement Proposals<span class="say-no-more"> (PEPs)</span></a>: The future of Python<span class="say-no-more"> is discussed here.</span>\n                        <a aria-hidden="true" class="rss-link" href="/dev/peps/peps.rss"><span class="icon-feed"></span> RSS</a>\n                    </h2>\n\n\n                    \n                    \n                </div>\n\n                                <div class="psf-widget">\n\n                    <div class="python-logo"></div>\n                    \n                    <h2 class="widget-title">\r\n    <span class="prompt">&gt;&gt;&gt;</span> <a href="/psf/">Python Software Foundation</a>\r\n</h2>\r\n<p>The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers. <a class="readmore" href="/psf/">Learn more</a> </p>\r\n<p class="click-these">\r\n    <a class="button" href="/users/membership/">Become a Member</a>\r\n    <a class="button" href="/psf/donations/">Donate to the PSF</a>\r\n</p>\n                </div>\n\n\n\n\n                </section>\n\n                \n                \n\n                \n                \n\n\n            </div><!-- end .container -->\n        </div><!-- end #content .content-wrapper -->\n\n        <!-- Footer and social media list -->\n        \n        <footer id="site-map" class="main-footer" role="contentinfo">\n            <div class="main-footer-links">\n                <div class="container">\n\n                    \n                    <a id="back-to-top-1" class="jump-link" href="#python-network"><span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> Back to Top</a>\n\n                    \n\n<ul class="sitemap navigation menu do-not-print" role="tree" id="container">\n    \n    <li class="tier-1 element-1">\n        <a href="/about/" >About</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    <li class="tier-1 element-2">\n        <a href="/downloads/" >Downloads</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/downloads/mac-osx/" title="">Mac OS X</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    <li class="tier-1 element-3">\n        <a href="/doc/" >Documentation</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner&#39;s Guide</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="https://devguide.python.org/" title="">Developer&#39;s Guide</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="http://python.org/dev/peps/" title="">PEP Index</a></li>\n    \n        <li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>\n    \n        <li class="tier-2 element-9" role="treeitem"><a href="/doc/essays/" title="">Python Essays</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    <li class="tier-1 element-4">\n        <a href="/community/" >Community</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/community/survey" title="">Community Survey</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="/community/forums/" title="">Forums</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="/psf/annual-report/2020/" title="">PSF Annual Impact Report</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>\n    \n        <li class="tier-2 element-8" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>\n    \n        <li class="tier-2 element-9" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>\n    \n        <li class="tier-2 element-10" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>\n    \n        <li class="tier-2 element-11" role="treeitem"><a href="/community/merchandise/" title="">Merchandise</a></li>\n    \n        <li class="tier-2 element-12" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>\n    \n        <li class="tier-2 element-13" role="treeitem"><a href="/psf/conduct/" title="">Code of Conduct</a></li>\n    \n        <li class="tier-2 element-14" role="treeitem"><a href="/psf/get-involved/" title="">Get Involved</a></li>\n    \n        <li class="tier-2 element-15" role="treeitem"><a href="/psf/community-stories/" title="">Shared Stories</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    <li class="tier-1 element-5">\n        <a href="/success-stories/" title="success-stories">Success Stories</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/success-stories/category/arts/" title="">Arts</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/success-stories/category/business/" title="">Business</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/success-stories/category/education/" title="">Education</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/success-stories/category/engineering/" title="">Engineering</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="/success-stories/category/government/" title="">Government</a></li>\n    \n        <li class="tier-2 element-6" role="treeitem"><a href="/success-stories/category/scientific/" title="">Scientific</a></li>\n    \n        <li class="tier-2 element-7" role="treeitem"><a href="/success-stories/category/software-development/" title="">Software Development</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    <li class="tier-1 element-6">\n        <a href="/blogs/" title="News from around the Python world">News</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/psf/newsletter/" title="Python Software Foundation Newsletter">PSF Newsletter</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">Community News</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon News</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    <li class="tier-1 element-7">\n        <a href="/events/" >Events</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="/events/python-events" title="">Python Events</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n    <li class="tier-1 element-8">\n        <a href="/dev/" >Contributing</a>\n        \n            \n\n<ul class="subnav menu">\n    \n        <li class="tier-2 element-1" role="treeitem"><a href="https://devguide.python.org/" title="">Developer&#39;s Guide</a></li>\n    \n        <li class="tier-2 element-2" role="treeitem"><a href="https://bugs.python.org/" title="">Issue Tracker</a></li>\n    \n        <li class="tier-2 element-3" role="treeitem"><a href="https://mail.python.org/mailman/listinfo/python-dev" title="">python-dev list</a></li>\n    \n        <li class="tier-2 element-4" role="treeitem"><a href="/dev/core-mentorship/" title="">Core Mentorship</a></li>\n    \n        <li class="tier-2 element-5" role="treeitem"><a href="/dev/security/" title="">Report a Security Issue</a></li>\n    \n</ul>\n\n        \n    </li>\n    \n</ul>\n\n\n                    <a id="back-to-top-2" class="jump-link" href="#python-network"><span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> Back to Top</a>\n                    \n\n                </div><!-- end .container -->\n            </div> <!-- end .main-footer-links -->\n\n            <div class="site-base">\n                <div class="container">\n                    \n                    <ul class="footer-links navigation menu do-not-print" role="tree">\n                        <li class="tier-1 element-1"><a href="/about/help/">Help &amp; <span class="say-no-more">General</span> Contact</a></li>\n                        <li class="tier-1 element-2"><a href="/community/diversity/">Diversity <span class="say-no-more">Initiatives</span></a></li>\n                        <li class="tier-1 element-3"><a href="https://github.com/python/pythondotorg/issues">Submit Website Bug</a></li>\n                        <li class="tier-1 element-4">\n                            <a href="https://status.python.org/">Status <span class="python-status-indicator-default" id="python-status-indicator"></span></a>\n                        </li>\n                    </ul>\n\n                    <div class="copyright">\n                        <p><small>\n                            <span class="pre">Copyright &copy;2001-2021.</span>\n                            &nbsp;<span class="pre"><a href="/psf-landing/">Python Software Foundation</a></span>\n                            &nbsp;<span class="pre"><a href="/about/legal/">Legal Statements</a></span>\n                            &nbsp;<span class="pre"><a href="/privacy/">Privacy Policy</a></span>\n                            &nbsp;<span class="pre"><a href="/psf/sponsorship/sponsors/#heroku">Powered by Heroku</a></span>\n                        </small></p>\n                    </div>\n\n                </div><!-- end .container -->\n            </div><!-- end .site-base -->\n\n        </footer>\n        \n\n    </div><!-- end #touchnav-wrapper -->\n\n    \n    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>\n    <script>window.jQuery || document.write(\'<script src="/static/js/libs/jquery-1.8.2.min.js"><\\/script>\')</script>\n    <script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js"></script>\n    <script>window.jQuery || document.write(\'<script src="/static/js/libs/jquery-ui-1.12.1.min.js"><\\/script>\')</script>\n\n    <script src="/static/js/libs/masonry.pkgd.min.js"></script>\n    <script src="/static/js/libs/html-includes.js"></script>\n\n    <script type="text/javascript" src="/static/js/main-min.b10cab6b401c.js" charset="utf-8"></script>\n    \n\n    <!--[if lte IE 7]>\n    <script type="text/javascript" src="/static/js/plugins/IE8-min.8af6e26c7a3b.js" charset="utf-8"></script>\n    \n    \n    <![endif]-->\n\n    <!--[if lte IE 8]>\n    <script type="text/javascript" src="/static/js/plugins/getComputedStyle-min.d41d8cd98f00.js" charset="utf-8"></script>\n    \n    \n    <![endif]-->\n\n    \n\n    \n    \n\n</body>\n</html>\n'


Ahora vamos a hacer lo mismo con una respuesta inválida, por ejemplo, `docs.python.org/parrot.spam`


```python
conn = http.client.HTTPSConnection("docs.python.org")
conn.request("GET", "/parrot.spam")
r2 = conn.getresponse()
print(r2.status, r2.reason)
```

    404 Not Found



```python
data2 = r2.read()
print(data2)
conn.close()
```

    b''


## Peticiones `POST`

En la web de [http://bugs.python.org/](http://bugs.python.org/) tienen un issue abierto (el [12524](http://bugs.python.org/issue12524)) para que los desarrolladores python puedan hacer pruebas de peticiones POST sobre una web. Vamos a hacer una prueba nosotros.

En este caso tenemos que configurar más parámetros que con el get, ya que no vamos a obtener información sino que vamos a modificar un servicio externo. Por ello, vamos a importar la librería `urllib`, para gestionar mejor la construcción de la URL


```python
import http.client, urllib.parse
```

A continuación vamos a construir la url y las headers de nuestra petición:


```python
params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}
```

Construimos la conexión y lanzamos la petición:


```python
conn = http.client.HTTPConnection("bugs.python.org")
conn.request("POST", "", params, headers)
response = conn.getresponse()
print(response.status, response.reason)
```

    301 Moved Permanently


Parece que algo no ha ido bien... prueba ahora con una conexión https:


```python
conn = http.client.HTTPSConnection("bugs.python.org")
conn.request("POST", "", params, headers)
response = conn.getresponse()
print(response.status, response.reason)
```

    302 Found


Muestra el contenido de la respuesta:


```python
data = response.read()
data
```




    b''



Y por último, cierra la conexión:


```python
conn.close()
```

# Ejercicio 3: Librería `requests`

La librería más usada por los desarrolladores Python para hacer requests a una API es **[requests: http para humanos](https://docs.python-requests.org/es/latest/)**
    


```python
! pip install requests
```

    Collecting requests
      Downloading requests-2.25.1-py2.py3-none-any.whl (61 kB)
    Collecting chardet<5,>=3.0.2
      Downloading chardet-4.0.0-py2.py3-none-any.whl (178 kB)
    Collecting urllib3<1.27,>=1.21.1
      Downloading urllib3-1.26.4-py2.py3-none-any.whl (153 kB)
    Collecting certifi>=2017.4.17
      Downloading certifi-2020.12.5-py2.py3-none-any.whl (147 kB)
    Collecting idna<3,>=2.5
      Downloading idna-2.10-py2.py3-none-any.whl (58 kB)
    Installing collected packages: urllib3, idna, chardet, certifi, requests
    Successfully installed certifi-2020.12.5 chardet-4.0.0 idna-2.10 requests-2.25.1 urllib3-1.26.4



```python
import requests
```

Uno de los métodos HTTP más comunes es GET. El método GET indica que está intentando obtener o recuperar datos de un recurso específico.


```python
requests.get('https://api.github.com')
```




    <Response [200]>



Una respuesta (response) es un objeto poderoso para inspeccionar los resultados de la petición. Haz la misma petición nuevamente, pero esta vez almacena el valor de retorno en una variable para que puedas ver más de cerca sus atributos y comportamientos:


```python
response = requests.get('https://api.github.com')
```


```python
response.status_code
```




    200



A veces, puedes usar el campo `status_code` para tomar decisiones en el código


```python
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')
```

    Success!


Prueba ahora con una URL inválida


```python
response = requests.get('https://api.github.com/invalid')
```


```python
response.status_code
```




    404



La respuesta de un GET a menudo tiene información valiosa, conocida como carga útil, en el cuerpo del mensaje. Usando los atributos y métodos de `response`, puede ver la carga útil en una variedad de formatos diferentes.


```python
response = requests.get('https://api.github.com')
response.content
```




    b'{"current_user_url":"https://api.github.com/user","current_user_authorizations_html_url":"https://github.com/settings/connections/applications{/client_id}","authorizations_url":"https://api.github.com/authorizations","code_search_url":"https://api.github.com/search/code?q={query}{&page,per_page,sort,order}","commit_search_url":"https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}","emails_url":"https://api.github.com/user/emails","emojis_url":"https://api.github.com/emojis","events_url":"https://api.github.com/events","feeds_url":"https://api.github.com/feeds","followers_url":"https://api.github.com/user/followers","following_url":"https://api.github.com/user/following{/target}","gists_url":"https://api.github.com/gists{/gist_id}","hub_url":"https://api.github.com/hub","issue_search_url":"https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}","issues_url":"https://api.github.com/issues","keys_url":"https://api.github.com/user/keys","label_search_url":"https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}","notifications_url":"https://api.github.com/notifications","organization_url":"https://api.github.com/orgs/{org}","organization_repositories_url":"https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}","organization_teams_url":"https://api.github.com/orgs/{org}/teams","public_gists_url":"https://api.github.com/gists/public","rate_limit_url":"https://api.github.com/rate_limit","repository_url":"https://api.github.com/repos/{owner}/{repo}","repository_search_url":"https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}","current_user_repositories_url":"https://api.github.com/user/repos{?type,page,per_page,sort}","starred_url":"https://api.github.com/user/starred{/owner}{/repo}","starred_gists_url":"https://api.github.com/gists/starred","user_url":"https://api.github.com/users/{user}","user_organizations_url":"https://api.github.com/user/orgs","user_repositories_url":"https://api.github.com/users/{user}/repos{?type,page,per_page,sort}","user_search_url":"https://api.github.com/search/users?q={query}{&page,per_page,sort,order}"}'




```python
response.text
```




    '{"current_user_url":"https://api.github.com/user","current_user_authorizations_html_url":"https://github.com/settings/connections/applications{/client_id}","authorizations_url":"https://api.github.com/authorizations","code_search_url":"https://api.github.com/search/code?q={query}{&page,per_page,sort,order}","commit_search_url":"https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}","emails_url":"https://api.github.com/user/emails","emojis_url":"https://api.github.com/emojis","events_url":"https://api.github.com/events","feeds_url":"https://api.github.com/feeds","followers_url":"https://api.github.com/user/followers","following_url":"https://api.github.com/user/following{/target}","gists_url":"https://api.github.com/gists{/gist_id}","hub_url":"https://api.github.com/hub","issue_search_url":"https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}","issues_url":"https://api.github.com/issues","keys_url":"https://api.github.com/user/keys","label_search_url":"https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}","notifications_url":"https://api.github.com/notifications","organization_url":"https://api.github.com/orgs/{org}","organization_repositories_url":"https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}","organization_teams_url":"https://api.github.com/orgs/{org}/teams","public_gists_url":"https://api.github.com/gists/public","rate_limit_url":"https://api.github.com/rate_limit","repository_url":"https://api.github.com/repos/{owner}/{repo}","repository_search_url":"https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}","current_user_repositories_url":"https://api.github.com/user/repos{?type,page,per_page,sort}","starred_url":"https://api.github.com/user/starred{/owner}{/repo}","starred_gists_url":"https://api.github.com/gists/starred","user_url":"https://api.github.com/users/{user}","user_organizations_url":"https://api.github.com/user/orgs","user_repositories_url":"https://api.github.com/users/{user}/repos{?type,page,per_page,sort}","user_search_url":"https://api.github.com/search/users?q={query}{&page,per_page,sort,order}"}'




```python
response.json()
```




    {'current_user_url': 'https://api.github.com/user',
     'current_user_authorizations_html_url': 'https://github.com/settings/connections/applications{/client_id}',
     'authorizations_url': 'https://api.github.com/authorizations',
     'code_search_url': 'https://api.github.com/search/code?q={query}{&page,per_page,sort,order}',
     'commit_search_url': 'https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}',
     'emails_url': 'https://api.github.com/user/emails',
     'emojis_url': 'https://api.github.com/emojis',
     'events_url': 'https://api.github.com/events',
     'feeds_url': 'https://api.github.com/feeds',
     'followers_url': 'https://api.github.com/user/followers',
     'following_url': 'https://api.github.com/user/following{/target}',
     'gists_url': 'https://api.github.com/gists{/gist_id}',
     'hub_url': 'https://api.github.com/hub',
     'issue_search_url': 'https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}',
     'issues_url': 'https://api.github.com/issues',
     'keys_url': 'https://api.github.com/user/keys',
     'label_search_url': 'https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}',
     'notifications_url': 'https://api.github.com/notifications',
     'organization_url': 'https://api.github.com/orgs/{org}',
     'organization_repositories_url': 'https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}',
     'organization_teams_url': 'https://api.github.com/orgs/{org}/teams',
     'public_gists_url': 'https://api.github.com/gists/public',
     'rate_limit_url': 'https://api.github.com/rate_limit',
     'repository_url': 'https://api.github.com/repos/{owner}/{repo}',
     'repository_search_url': 'https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}',
     'current_user_repositories_url': 'https://api.github.com/user/repos{?type,page,per_page,sort}',
     'starred_url': 'https://api.github.com/user/starred{/owner}{/repo}',
     'starred_gists_url': 'https://api.github.com/gists/starred',
     'user_url': 'https://api.github.com/users/{user}',
     'user_organizations_url': 'https://api.github.com/user/orgs',
     'user_repositories_url': 'https://api.github.com/users/{user}/repos{?type,page,per_page,sort}',
     'user_search_url': 'https://api.github.com/search/users?q={query}{&page,per_page,sort,order}'}



## Headers

Los encabezados de respuesta pueden darte información útil, como el tipo de contenido de la carga útil de respuesta y un límite de tiempo sobre cuánto tiempo almacenar en caché la respuesta. Para ver estos encabezados, accede al campo `headers`:


```python
response.headers
```




    {'Server': 'GitHub.com', 'Date': 'Sun, 09 May 2021 00:05:57 GMT', 'Cache-Control': 'public, max-age=60, s-maxage=60', 'Vary': 'Accept, Accept-Encoding, Accept, X-Requested-With', 'ETag': '"27278c3efffccc4a7be1bf315653b901b14f2989b2c2600d7cc2e90a97ffbf60"', 'Access-Control-Expose-Headers': 'ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Resource, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, Deprecation, Sunset', 'Access-Control-Allow-Origin': '*', 'Strict-Transport-Security': 'max-age=31536000; includeSubdomains; preload', 'X-Frame-Options': 'deny', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '0', 'Referrer-Policy': 'origin-when-cross-origin, strict-origin-when-cross-origin', 'Content-Security-Policy': "default-src 'none'", 'Content-Type': 'application/json; charset=utf-8', 'X-GitHub-Media-Type': 'github.v3; format=json', 'Content-Encoding': 'gzip', 'X-RateLimit-Limit': '60', 'X-RateLimit-Remaining': '56', 'X-RateLimit-Reset': '1620520057', 'X-RateLimit-Resource': 'core', 'X-RateLimit-Used': '4', 'Accept-Ranges': 'bytes', 'Content-Length': '496', 'X-GitHub-Request-Id': 'D036:F036:31891B4:328BB91:6097276E'}



Una forma común de personalizar una solicitud GET es pasar valores a través de parámetros de cadena de consulta en la URL. Para hacer usa la función get utilizando el parámetro `params`. 

Por ejemplo, puede usar la API de búsqueda de GitHub para buscar la biblioteca de solicitudes:


```python
import requests

# Search GitHub's repositories for requests
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)

# Inspect some attributes of the `requests` repository
json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')  # Python 3.6+
```

    Repository name: grequests
    Repository description: Requests + Gevent = <3


## Otros métodos HTTP


```python
response = requests.post('https://httpbin.org/post', data={'key':'value'})
response.json()
```




    {'args': {},
     'data': '',
     'files': {},
     'form': {'key': 'value'},
     'headers': {'Accept': '*/*',
      'Accept-Encoding': 'gzip, deflate',
      'Content-Length': '9',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Host': 'httpbin.org',
      'User-Agent': 'python-requests/2.25.1',
      'X-Amzn-Trace-Id': 'Root=1-607f5990-1c6427264bce135544fba0d0'},
     'json': None,
     'origin': '83.50.235.155',
     'url': 'https://httpbin.org/post'}




```python
requests.post('https://httpbin.org/post', data={'key':'value'})
requests.put('https://httpbin.org/put', data={'key':'value'})
requests.delete('https://httpbin.org/delete')
requests.head('https://httpbin.org/get')
requests.patch('https://httpbin.org/patch', data={'key':'value'})
requests.options('https://httpbin.org/get')
```




    <Response [200]>



## Ejercicio 4: Explora otras librerías


```python
response = requests.get(
    'https://cat-fact.herokuapp.com/facts',
    params={'animal_type': 'horse'},
)
response.json()
```




    [{'status': {'verified': True, 'sentCount': 1},
      'type': 'cat',
      'deleted': False,
      '_id': '58e008800aac31001185ed07',
      'user': '58e007480aac31001185ecef',
      'text': 'Wikipedia has a recording of a cat meowing, because why not?',
      '__v': 0,
      'source': 'user',
      'updatedAt': '2020-08-23T20:20:01.611Z',
      'createdAt': '2018-03-06T21:20:03.505Z',
      'used': False},
     {'status': {'verified': True, 'sentCount': 1},
      'type': 'cat',
      'deleted': False,
      '_id': '58e008630aac31001185ed01',
      'user': '58e007480aac31001185ecef',
      'text': 'When cats grimace, they are usually "taste-scenting." They have an extra organ that, with some breathing control, allows the cats to taste-sense the air.',
      '__v': 0,
      'source': 'user',
      'updatedAt': '2020-08-23T20:20:01.611Z',
      'createdAt': '2018-02-07T21:20:02.903Z',
      'used': False},
     {'status': {'verified': True, 'sentCount': 1},
      'type': 'cat',
      'deleted': False,
      '_id': '58e00a090aac31001185ed16',
      'user': '58e007480aac31001185ecef',
      'text': 'Cats make more than 100 different sounds whereas dogs make around 10.',
      '__v': 0,
      'source': 'user',
      'updatedAt': '2020-08-23T20:20:01.611Z',
      'createdAt': '2018-02-11T21:20:03.745Z',
      'used': False},
     {'status': {'verified': True, 'sentCount': 1},
      'type': 'cat',
      'deleted': False,
      '_id': '58e009390aac31001185ed10',
      'user': '58e007480aac31001185ecef',
      'text': "Most cats are lactose intolerant, and milk can cause painful stomach cramps and diarrhea. It's best to forego the milk and just give your cat the standard: clean, cool drinking water.",
      '__v': 0,
      'source': 'user',
      'updatedAt': '2020-08-23T20:20:01.611Z',
      'createdAt': '2018-03-04T21:20:02.979Z',
      'used': False},
     {'status': {'verified': True, 'sentCount': 1},
      'type': 'cat',
      'deleted': False,
      '_id': '58e008780aac31001185ed05',
      'user': '58e007480aac31001185ecef',
      'text': 'Owning a cat can reduce the risk of stroke and heart attack by a third.',
      '__v': 0,
      'source': 'user',
      'updatedAt': '2020-08-23T20:20:01.611Z',
      'createdAt': '2018-03-29T20:20:03.844Z',
      'used': False}]




```python
response = requests.get('https://api.fbi.gov/wanted/v1/list')
data = response.json()
print(data['total'])
print(data['items'][:10])
```

    990
    [{'files': [{'url': 'https://www.fbi.gov/wanted/seeking-info/manassas-mall-shooting/download.pdf', 'name': 'English'}], 'age_range': None, 'uid': '902d88d5245d401d8b36e61b646e46df', 'weight': None, 'occupations': None, 'field_offices': ['washingtondc'], 'locations': None, 'reward_text': 'The FBI is offering a reward of up to $5,000 for information leading to the identification, arrest, and conviction of the individual(s) responsible for the murder of Jahmar Latravern Graves.', 'hair': None, 'ncic': None, 'dates_of_birth_used': None, 'caution': None, 'nationality': None, 'age_min': None, 'age_max': None, 'scars_and_marks': None, 'subjects': ['Seeking Information'], 'aliases': None, 'race_raw': None, 'suspects': None, 'publication': '2021-04-20T12:51:00', 'title': 'MANASSAS MALL SHOOTING', 'coordinates': [], 'hair_raw': None, 'languages': None, 'complexion': None, 'build': None, 'details': '<p>The FBI\'s Northern Virginia Safe Streets Violent Crimes Task Force is assisting the Prince William Police Department in Virginia with its investigation into the murder of Jahmar Latravern Graves.\xa0 Graves, 34, from Baltimore, Maryland, was killed, and a 22-year-old victim was wounded, in a shooting that occurred at approximately 11:15 p.m. on April 2, 2021, during an altercation in the parking lot outside the Manassas Mall in Manassas, Virginia.\xa0\xa0</p>\r\n<p>\xa0<br />Investigators are asking for the public’s assistance in identifying two male suspects and one female suspect, as well as anyone else involved in the shooting. Surveillance video can be found at <a data-urltype="/view" data-val="https://www.youtube.com/watch?v=85pgWyULEmE" href="https://www.youtube.com/watch?v=85pgWyULEmE" data-linktype="external">https://youtu.be/85pgWyULEmE</a>.</p>\r\n<p>\xa0</p>', 'status': 'na', 'legat_names': None, 'eyes': None, 'person_classification': 'Main', 'description': 'Manassas, Virginia\r\nApril 2, 2021', 'images': [{'large': 'https://www.fbi.gov/wanted/seeking-info/manassas-mall-shooting/@@images/image/large', 'caption': None, 'thumb': 'https://www.fbi.gov/wanted/seeking-info/manassas-mall-shooting/@@images/image/thumb', 'original': 'https://www.fbi.gov/wanted/seeking-info/manassas-mall-shooting/@@images/image'}, {'large': 'https://www.fbi.gov/wanted/seeking-info/manassas-mall-shooting/wfomallshooting2.jpg/@@images/image/large', 'caption': '', 'thumb': 'https://www.fbi.gov/wanted/seeking-info/manassas-mall-shooting/wfomallshooting2.jpg/@@images/image/thumb', 'original': 'https://www.fbi.gov/wanted/seeking-info/manassas-mall-shooting/wfomallshooting2.jpg'}, {'large': 'https://www.fbi.gov/wanted/seeking-info/manassas-mall-shooting/wfomallshooting3.jpg/@@images/image/large', 'caption': '', 'thumb': 'https://www.fbi.gov/wanted/seeking-info/manassas-mall-shooting/wfomallshooting3.jpg/@@images/image/thumb', 'original': 'https://www.fbi.gov/wanted/seeking-info/manassas-mall-shooting/wfomallshooting3.jpg'}, {'large': 'https://www.fbi.gov/wanted/seeking-info/manassas-mall-shooting/wfomallshooting4.jpg/@@images/image/large', 'caption': '', 'thumb': 'https://www.fbi.gov/wanted/seeking-info/manassas-mall-shooting/wfomallshooting4.jpg/@@images/image/thumb', 'original': 'https://www.fbi.gov/wanted/seeking-info/manassas-mall-shooting/wfomallshooting4.jpg'}], 'possible_countries': None, 'weight_min': None, 'additional_information': None, 'remarks': None, 'path': '/wanted/seeking-info/manassas-mall-shooting', 'sex': None, 'eyes_raw': None, 'weight_max': None, 'reward_min': 0, 'url': 'https://www.fbi.gov/wanted/seeking-info/manassas-mall-shooting', 'possible_states': None, 'modified': '2021-04-20T19:32:38+00:00', 'reward_max': 0, 'race': None, 'height_max': None, 'place_of_birth': None, 'height_min': None, 'warning_message': None, '@id': 'https://api.fbi.gov/@wanted-person/902d88d5245d401d8b36e61b646e46df'}, {'files': [{'url': 'https://www.fbi.gov/wanted/law-enforcement-assistance/justin-smith/download.pdf', 'name': 'English'}], 'age_range': None, 'uid': 'c8dd3e4221784278ae34ba01f8069665', 'weight': '160 to 180 pounds', 'occupations': None, 'field_offices': ['philadelphia'], 'locations': None, 'reward_text': 'The FBI is offering a monetary reward for information leading directly to the arrest of Justin Smith.', 'hair': 'black', 'ncic': None, 'dates_of_birth_used': ['December 1, 1997'], 'caution': "<p>The FBI's Philadelphia Violent Crimes Task Force is assisting the Philadelphia Police Department in Pennsylvania with the search for Justin Smith.\xa0 Smith is wanted for murder in the death of his pregnant 21-year-old girlfriend, who disappeared on March 30, 2021, and whose body was found on April 5, 2021.\xa0 Smith is alleged to have shot the woman in the head multiple times, causing her death and the death of her unborn child.</p>\r\n<p>\xa0</p>\r\n<p>On April 9, 2021, Smith was charged with murder and related offenses in the 1st\xa0Judicial District in Philadelphia County, Pennsylvania, and a state warrant was issued for his arrest.</p>\r\n<p>\xa0</p>", 'nationality': 'American', 'age_min': None, 'age_max': None, 'scars_and_marks': None, 'subjects': ['Law Enforcement Assistance'], 'aliases': None, 'race_raw': 'Black', 'suspects': None, 'publication': '2021-04-19T13:17:00', 'title': 'JUSTIN SMITH', 'coordinates': [], 'hair_raw': 'Black', 'languages': None, 'complexion': None, 'build': None, 'details': None, 'status': 'na', 'legat_names': None, 'eyes': 'brown', 'person_classification': 'Main', 'description': 'Murder; First Degree Murder - Unborn Child; Arson; Firearms Violations; Abuse of Corpse; Tamper with Evidence; Criminal Conspiracy', 'images': [{'large': 'https://www.fbi.gov/wanted/law-enforcement-assistance/justin-smith/@@images/image/large', 'caption': 'Photograph taken in 2019', 'thumb': 'https://www.fbi.gov/wanted/law-enforcement-assistance/justin-smith/@@images/image/thumb', 'original': 'https://www.fbi.gov/wanted/law-enforcement-assistance/justin-smith/@@images/image'}], 'possible_countries': None, 'weight_min': 160, 'additional_information': None, 'remarks': '<p>Smith is known to have connections to Greensboro, North Carolina, and New Castle, Delaware.\xa0\xa0He has also been seen in the Little Haiti neighborhood of Miami, Florida, and in Atlanta, Georgia.\xa0</p>', 'path': '/wanted/law-enforcement-assistance/justin-smith', 'sex': 'Male', 'eyes_raw': 'Brown', 'weight_max': 180, 'reward_min': 0, 'url': 'https://www.fbi.gov/wanted/law-enforcement-assistance/justin-smith', 'possible_states': None, 'modified': '2021-04-19T18:45:58+00:00', 'reward_max': 0, 'race': 'black', 'height_max': 68, 'place_of_birth': 'Greensboro, North Carolina', 'height_min': 68, 'warning_message': 'SHOULD BE CONSIDERED ARMED AND DANGEROUS', '@id': 'https://api.fbi.gov/@wanted-person/c8dd3e4221784278ae34ba01f8069665'}, {'files': [{'url': 'https://www.fbi.gov/wanted/seeking-info/medardo-gutierrez-lopez/download.pdf', 'name': 'English'}, {'url': 'https://www.fbi.gov/wanted/seeking-info/medardo-gutierrez-lopez/gutierrez-lopez_spanish_4-19-2021-1.pdf/@@download/file/Gutierrez-Lopez_Spanish_4-19-2021-1.pdf', 'name': 'EN ESPAÑOL'}], 'age_range': None, 'uid': '9459a4a1ae564f75a6747866f02bf118', 'weight': None, 'occupations': None, 'field_offices': ['albuquerque'], 'locations': None, 'reward_text': None, 'hair': None, 'ncic': None, 'dates_of_birth_used': ['June 8, 1989'], 'caution': None, 'nationality': 'Mexican', 'age_min': None, 'age_max': None, 'scars_and_marks': None, 'subjects': ['Seeking Information'], 'aliases': None, 'race_raw': 'White (Hispanic)', 'suspects': None, 'publication': '2021-04-14T12:24:00', 'title': 'MEDARDO GUTIERREZ-LOPEZ', 'coordinates': [], 'hair_raw': None, 'languages': None, 'complexion': None, 'build': None, 'details': "<p>The Federal Bureau of Investigation's Albuquerque Field Office is asking for the public's assistance in identifying the circumstances surrounding the death of Medardo Gutierrez-Lopez, a citizen of Mexico.\xa0<br />\xa0<br />On July 6, 2020, Gutierrez-Lopez was found deceased near the frontage road north of Interstate 40 and east of Exit 33 in Fort Wingate, New Mexico, on the Navajo Nation. The cause of death is undetermined.</p>", 'status': 'na', 'legat_names': None, 'eyes': None, 'person_classification': 'Main', 'description': 'Unknown Cause of Death\r\nFort Wingate, New Mexico\r\nJuly 6, 2020', 'images': [{'large': 'https://www.fbi.gov/wanted/seeking-info/medardo-gutierrez-lopez/@@images/image/large', 'caption': 'Photograph taken in 2019', 'thumb': 'https://www.fbi.gov/wanted/seeking-info/medardo-gutierrez-lopez/@@images/image/thumb', 'original': 'https://www.fbi.gov/wanted/seeking-info/medardo-gutierrez-lopez/@@images/image'}, {'large': 'https://www.fbi.gov/wanted/seeking-info/medardo-gutierrez-lopez/lopez-2.png/@@images/image/large', 'caption': 'Photograph taken in 2018', 'thumb': 'https://www.fbi.gov/wanted/seeking-info/medardo-gutierrez-lopez/lopez-2.png/@@images/image/thumb', 'original': 'https://www.fbi.gov/wanted/seeking-info/medardo-gutierrez-lopez/lopez-2.png'}, {'large': 'https://www.fbi.gov/wanted/seeking-info/medardo-gutierrez-lopez/lopez-3.png/@@images/image/large', 'caption': 'Photograph taken in 2019', 'thumb': 'https://www.fbi.gov/wanted/seeking-info/medardo-gutierrez-lopez/lopez-3.png/@@images/image/thumb', 'original': 'https://www.fbi.gov/wanted/seeking-info/medardo-gutierrez-lopez/lopez-3.png'}, {'large': 'https://www.fbi.gov/wanted/seeking-info/medardo-gutierrez-lopez/lopez-4.png/@@images/image/large', 'caption': '', 'thumb': 'https://www.fbi.gov/wanted/seeking-info/medardo-gutierrez-lopez/lopez-4.png/@@images/image/thumb', 'original': 'https://www.fbi.gov/wanted/seeking-info/medardo-gutierrez-lopez/lopez-4.png'}], 'possible_countries': None, 'weight_min': None, 'additional_information': None, 'remarks': None, 'path': '/wanted/seeking-info/medardo-gutierrez-lopez', 'sex': 'Male', 'eyes_raw': None, 'weight_max': None, 'reward_min': 0, 'url': 'https://www.fbi.gov/wanted/seeking-info/medardo-gutierrez-lopez', 'possible_states': None, 'modified': '2021-04-19T18:07:53+00:00', 'reward_max': 0, 'race': 'hispanic', 'height_max': None, 'place_of_birth': 'Oaxaca, Mexico', 'height_min': None, 'warning_message': None, '@id': 'https://api.fbi.gov/@wanted-person/9459a4a1ae564f75a6747866f02bf118'}, {'files': [{'url': 'https://www.fbi.gov/wanted/seeking-info/sabotage-of-communications-towers/download.pdf', 'name': 'English'}], 'age_range': None, 'uid': '7f4b72a03eae4e298578f87a0651913d', 'weight': None, 'occupations': None, 'field_offices': ['dallas'], 'locations': None, 'reward_text': 'The FBI is offering a reward of up to $5,000 for information leading to the identification, arrest and conviction of the individual(s) responsible for this crime.', 'hair': None, 'ncic': None, 'dates_of_birth_used': None, 'caution': None, 'nationality': None, 'age_min': None, 'age_max': None, 'scars_and_marks': None, 'subjects': ['Seeking Information'], 'aliases': None, 'race_raw': None, 'suspects': None, 'publication': '2021-03-16T14:36:00', 'title': 'SABOTAGE OF COMMUNICATIONS TOWERS', 'coordinates': [], 'hair_raw': None, 'languages': None, 'complexion': None, 'build': None, 'details': '<p>In the pre-dawn hours of Friday, December 18, 2020, an unknown person or persons seriously damaged two communication towers in Wichita Falls, Texas, by cutting several of the wires that support the structures. One 500-foot-tall tower collapsed to the ground at its location in the 3700 block of Arena Road. The second tower at Seymour Highway did not collapse, but the damage required evacuation of a nearby business. Investigators believe that if the 1,200-foot-tall tower had collapsed on the business or highway, serious bodily injuries and fatalities could have resulted.</p>', 'status': 'na', 'legat_names': None, 'eyes': None, 'person_classification': 'Main', 'description': 'Wichita Falls, Texas\r\nDecember 18, 2020', 'images': [{'large': 'https://www.fbi.gov/wanted/seeking-info/sabotage-of-communications-towers/@@images/image/large', 'caption': None, 'thumb': 'https://www.fbi.gov/wanted/seeking-info/sabotage-of-communications-towers/@@images/image/thumb', 'original': 'https://www.fbi.gov/wanted/seeking-info/sabotage-of-communications-towers/@@images/image'}], 'possible_countries': None, 'weight_min': None, 'additional_information': None, 'remarks': None, 'path': '/wanted/seeking-info/sabotage-of-communications-towers', 'sex': None, 'eyes_raw': None, 'weight_max': None, 'reward_min': 0, 'url': 'https://www.fbi.gov/wanted/seeking-info/sabotage-of-communications-towers', 'possible_states': None, 'modified': '2021-04-19T15:35:50+00:00', 'reward_max': 0, 'race': None, 'height_max': None, 'place_of_birth': None, 'height_min': None, 'warning_message': None, '@id': 'https://api.fbi.gov/@wanted-person/7f4b72a03eae4e298578f87a0651913d'}, {'files': [{'url': 'https://www.fbi.gov/wanted/seeking-info/isiah-terrell-billy/download.pdf', 'name': 'English'}, {'url': 'https://www.fbi.gov/wanted/seeking-info/isiah-terrell-billy/billy-navajo-4-19-21.pdf/@@download/file/Billy Navajo 4-19-21.pdf', 'name': 'DINÉ BIZAAD K’EHGO'}], 'age_range': None, 'uid': '950e62ff80cf4fe1b476db427d2711a3', 'weight': '144 pounds', 'occupations': None, 'field_offices': ['albuquerque'], 'locations': None, 'reward_text': 'The FBI is offering a reward of up to $5,000 for information leading to the identification, arrest, and conviction of the individual(s) responsible for the death of Isiah Terrell Billy.', 'hair': 'black', 'ncic': None, 'dates_of_birth_used': ['October 4, 1990'], 'caution': None, 'nationality': None, 'age_min': None, 'age_max': None, 'scars_and_marks': None, 'subjects': ['Seeking Information'], 'aliases': None, 'race_raw': 'Native American', 'suspects': None, 'publication': '2021-03-03T13:33:00', 'title': 'ISIAH TERRELL BILLY', 'coordinates': [], 'hair_raw': 'Black', 'languages': None, 'complexion': None, 'build': None, 'details': "<p>The FBI's Albuquerque Field Office, Farmington Resident Agency in New Mexico is seeking the public's assistance in finding the person(s) responsible for the death of Isiah Terrell Billy, who lived in Shiprock, New Mexico, on the Navajo Nation.</p>\r\n<p>\xa0</p>\r\n<p>On October 5, 2020, Billy was found deceased in a wash east of the Sinclair gas station near mile marker 23 on U.S. Highway 64, in Shiprock, New Mexico.</p>\r\n<p>\xa0</p>\r\n<p>The cause of death is pending, but considered suspicious.</p>", 'status': 'na', 'legat_names': None, 'eyes': 'brown', 'person_classification': 'Victim', 'description': 'Homicide Victim\r\nShiprock, New Mexico\r\nOctober 5, 2020', 'images': [{'large': 'https://www.fbi.gov/wanted/seeking-info/isiah-terrell-billy/@@images/image/large', 'caption': 'Photograph taken in 2015', 'thumb': 'https://www.fbi.gov/wanted/seeking-info/isiah-terrell-billy/@@images/image/thumb', 'original': 'https://www.fbi.gov/wanted/seeking-info/isiah-terrell-billy/@@images/image'}], 'possible_countries': None, 'weight_min': 144, 'additional_information': None, 'remarks': None, 'path': '/wanted/seeking-info/isiah-terrell-billy', 'sex': 'Male', 'eyes_raw': 'Brown', 'weight_max': 144, 'reward_min': 0, 'url': 'https://www.fbi.gov/wanted/seeking-info/isiah-terrell-billy', 'possible_states': None, 'modified': '2021-04-19T14:55:22+00:00', 'reward_max': 0, 'race': 'native', 'height_max': 64, 'place_of_birth': None, 'height_min': 64, 'warning_message': None, '@id': 'https://api.fbi.gov/@wanted-person/950e62ff80cf4fe1b476db427d2711a3'}, {'files': [{'url': 'https://www.fbi.gov/wanted/kidnap/luis-davila/download.pdf', 'name': 'English'}, {'url': 'https://www.fbi.gov/wanted/kidnap/luis-davila/davilaspanish.pdf/@@download/file/DavilaSpanish.pdf', 'name': 'EN ESPAÑOL'}], 'age_range': None, 'uid': '641ac2b3505c4525ab52381af7265eff', 'weight': 'Approximately 190 pounds', 'occupations': None, 'field_offices': ['littlerock'], 'locations': None, 'reward_text': None, 'hair': 'black', 'ncic': None, 'dates_of_birth_used': None, 'caution': None, 'nationality': 'United States', 'age_min': None, 'age_max': None, 'scars_and_marks': None, 'subjects': ['Exploited Children', 'Kidnappings and Missing Persons'], 'aliases': None, 'race_raw': 'White (Hispanic)', 'suspects': None, 'publication': '2021-04-11T13:26:00', 'title': 'LUIS DAVILA', 'coordinates': [], 'hair_raw': 'Black', 'languages': ['English', 'Spanish'], 'complexion': None, 'build': None, 'details': '<p>The FBI’s Little Rock Field Office is seeking information from the public about an Arkansas resident who went to Mexico to visit his girlfriend and has not been seen since March 29, 2021. Luis Davila (31 years old at the time of his disappearance), is from Bentonville, Arkansas, and was in Mexico visiting his girlfriend near Monterrey. Luis was last seen near Monterrey, Mexico, on March 29, 2021, wearing a white shirt and jeans. He was driving a silver 2016 Nissan Maxima (Arkansas License Plate 936-VET). Although the whereabouts of Luis are unknown at this time, it is believed he may still be in Mexico, possibly near Nuevo Laredo, Tamaulipas. Luis may be the victim of a kidnapping.</p>\r\n<p>\xa0</p>', 'status': 'na', 'legat_names': None, 'eyes': 'brown', 'person_classification': 'Main', 'description': 'Monterrey or Nuevo Laredo, Tamaulipas, Mexico\r\nMarch 29, 2021', 'images': [{'large': 'https://www.fbi.gov/wanted/kidnap/luis-davila/@@images/image/large', 'caption': None, 'thumb': 'https://www.fbi.gov/wanted/kidnap/luis-davila/@@images/image/thumb', 'original': 'https://www.fbi.gov/wanted/kidnap/luis-davila/@@images/image'}, {'large': 'https://www.fbi.gov/wanted/kidnap/luis-davila/thumbnail_luis-davila-2.jpg/@@images/image/large', 'caption': '', 'thumb': 'https://www.fbi.gov/wanted/kidnap/luis-davila/thumbnail_luis-davila-2.jpg/@@images/image/thumb', 'original': 'https://www.fbi.gov/wanted/kidnap/luis-davila/thumbnail_luis-davila-2.jpg'}, {'large': 'https://www.fbi.gov/wanted/kidnap/luis-davila/thumbnail_luis-davila-3.jpg/@@images/image/large', 'caption': '', 'thumb': 'https://www.fbi.gov/wanted/kidnap/luis-davila/thumbnail_luis-davila-3.jpg/@@images/image/thumb', 'original': 'https://www.fbi.gov/wanted/kidnap/luis-davila/thumbnail_luis-davila-3.jpg'}], 'possible_countries': None, 'weight_min': 190, 'additional_information': None, 'remarks': '<p>Luis Davila is associated with the following locations: Bentonville, Arkansas; Monterrey, Mexico; and Nuevo Laredo, Tamaulipas, Mexico.</p>', 'path': '/wanted/kidnap/luis-davila', 'sex': 'Male', 'eyes_raw': 'Brown', 'weight_max': 190, 'reward_min': 0, 'url': 'https://www.fbi.gov/wanted/kidnap/luis-davila', 'possible_states': None, 'modified': '2021-04-19T12:12:52+00:00', 'reward_max': 0, 'race': 'hispanic', 'height_max': 70, 'place_of_birth': None, 'height_min': 70, 'warning_message': None, '@id': 'https://api.fbi.gov/@wanted-person/641ac2b3505c4525ab52381af7265eff'}, {'files': [{'url': 'https://www.fbi.gov/wanted/seeking-info/bank-burglary---minneapolis/download.pdf', 'name': 'English'}], 'age_range': None, 'uid': 'd82c238e8e2947cf86ae01e95a8d6a85', 'weight': None, 'occupations': None, 'field_offices': ['minneapolis'], 'locations': None, 'reward_text': 'Reward money may be available.', 'hair': None, 'ncic': None, 'dates_of_birth_used': None, 'caution': None, 'nationality': None, 'age_min': None, 'age_max': None, 'scars_and_marks': None, 'subjects': ['Seeking Information'], 'aliases': None, 'race_raw': None, 'suspects': None, 'publication': '2021-04-16T10:29:00', 'title': 'BANK BURGLARY - MINNEAPOLIS', 'coordinates': [], 'hair_raw': None, 'languages': None, 'complexion': None, 'build': None, 'details': "<p>The Federal Bureau of Investigation's Minneapolis Field Office is seeking the public's assistance in identifying the individuals responsible for a bank burglary that occurred the night of Sunday, April 11, 2021, at the Wells Fargo Bank located at 8460 Zane Avenue in Brooklyn Park, Minnesota.</p>", 'status': 'na', 'legat_names': None, 'eyes': None, 'person_classification': 'Main', 'description': 'Brooklyn Park, Minnesota\r\nApril 11, 2021', 'images': [{'large': 'https://www.fbi.gov/wanted/seeking-info/bank-burglary---minneapolis/@@images/image/large', 'caption': None, 'thumb': 'https://www.fbi.gov/wanted/seeking-info/bank-burglary---minneapolis/@@images/image/thumb', 'original': 'https://www.fbi.gov/wanted/seeking-info/bank-burglary---minneapolis/@@images/image'}, {'large': 'https://www.fbi.gov/wanted/seeking-info/bank-burglary---minneapolis/mp-br-2.png/@@images/image/large', 'caption': '', 'thumb': 'https://www.fbi.gov/wanted/seeking-info/bank-burglary---minneapolis/mp-br-2.png/@@images/image/thumb', 'original': 'https://www.fbi.gov/wanted/seeking-info/bank-burglary---minneapolis/mp-br-2.png'}], 'possible_countries': None, 'weight_min': None, 'additional_information': None, 'remarks': None, 'path': '/wanted/seeking-info/bank-burglary---minneapolis', 'sex': None, 'eyes_raw': None, 'weight_max': None, 'reward_min': 0, 'url': 'https://www.fbi.gov/wanted/seeking-info/bank-burglary---minneapolis', 'possible_states': None, 'modified': '2021-04-16T16:55:13+00:00', 'reward_max': 0, 'race': None, 'height_max': None, 'place_of_birth': None, 'height_min': None, 'warning_message': None, '@id': 'https://api.fbi.gov/@wanted-person/d82c238e8e2947cf86ae01e95a8d6a85'}, {'files': [{'url': 'https://www.fbi.gov/wanted/vicap/homicides-and-sexual-assaults/unknown-suspect---long-beach-california/vicap-alert-2021-04-09.pdf', 'name': 'English'}], 'age_range': 'Late 40s to early 50s', 'uid': '4ce12b102fc4485da75a95b1e1de2f47', 'weight': '170 to 180 pounds', 'occupations': None, 'field_offices': None, 'locations': None, 'reward_text': None, 'hair': None, 'ncic': None, 'dates_of_birth_used': None, 'caution': None, 'nationality': None, 'age_min': 40, 'age_max': 50, 'scars_and_marks': None, 'subjects': ['ViCAP Homicides and Sexual Assaults'], 'aliases': None, 'race_raw': 'White or White (Hispanic)', 'suspects': None, 'publication': '2021-04-16T10:55:00', 'title': 'UNKNOWN SUSPECT - LONG BEACH, CALIFORNIA', 'coordinates': [], 'hair_raw': None, 'languages': None, 'complexion': None, 'build': 'Medium', 'details': "<p>On Saturday, July 21, 2018, at approximately 4:20 p.m., the body of Frederick Taft, a 57-year-old Black male, was discovered inside the men's restroom on the west side of the Pan American Park in Long Beach, California. Taft had been attending a family picnic at the park. He had been shot multiple times in the torso, back, and head.</p>\r\n<p>The suspect was described as a White or White (Hispanic) male in his late 40s to early 50s. Multiple witnesses observed the unknown suspect fleeing the men's restroom immediately after the gunshots were heard, concealing what appeared to be a rifle-type firearm.</p>\r\n<p>Taft's homicide is still unsolved. Anyone with information is urged to contact the Long Beach Police Department.</p>", 'status': 'na', 'legat_names': None, 'eyes': None, 'person_classification': 'Main', 'description': 'Homicide\r\nJuly 21, 2018\r\nLong Beach, California', 'images': [{'large': 'https://www.fbi.gov/wanted/vicap/homicides-and-sexual-assaults/unknown-suspect---long-beach-california/@@images/image/large', 'caption': None, 'thumb': 'https://www.fbi.gov/wanted/vicap/homicides-and-sexual-assaults/unknown-suspect---long-beach-california/@@images/image/thumb', 'original': 'https://www.fbi.gov/wanted/vicap/homicides-and-sexual-assaults/unknown-suspect---long-beach-california/@@images/image'}], 'possible_countries': None, 'weight_min': 170, 'additional_information': None, 'remarks': '<p>The unknown suspect wore a long-sleeved, button-down, white linen shirt, khaki-colored cargo shots, and a soft, cotton-style fishing hat. He had a round chin and face.</p>', 'path': '/wanted/vicap/homicides-and-sexual-assaults/unknown-suspect---long-beach-california', 'sex': 'Male', 'eyes_raw': None, 'weight_max': 180, 'reward_min': 0, 'url': 'https://www.fbi.gov/wanted/vicap/homicides-and-sexual-assaults/unknown-suspect---long-beach-california', 'possible_states': None, 'modified': '2021-04-16T16:07:47+00:00', 'reward_max': 0, 'race': 'hispanic', 'height_max': 70, 'place_of_birth': None, 'height_min': 67, 'warning_message': None, '@id': 'https://api.fbi.gov/@wanted-person/4ce12b102fc4485da75a95b1e1de2f47'}, {'files': [{'url': 'https://www.fbi.gov/wanted/seeking-info/zachariah-juwaun-shorty/download.pdf', 'name': 'English'}, {'url': 'https://www.fbi.gov/wanted/seeking-info/zachariah-juwaun-shorty/shorty-navajo-3-2-2021.pdf/@@download/file/Shorty Navajo 3-2-2021.pdf', 'name': 'DINÉ BIZAAD K’EHGO'}], 'age_range': None, 'uid': 'f042ad53ce1c4b68ab820440a9529c67', 'weight': '130 pounds', 'occupations': None, 'field_offices': ['albuquerque'], 'locations': None, 'reward_text': 'The FBI is offering a reward of up to $5,000 for information leading to the identification, arrest, and conviction of the individual(s) responsible for the death of Zachariah Juwaun Shorty.', 'hair': 'black', 'ncic': None, 'dates_of_birth_used': ['May 5, 1997'], 'caution': None, 'nationality': None, 'age_min': None, 'age_max': None, 'scars_and_marks': 'Shorty has the following tattoos: the words "Indian Outlaw" on his left arm, the word "Numb" on his left hand, and the word "Blessed" on his right arm.', 'subjects': ['Seeking Information', 'Indian Country', 'Navajo'], 'aliases': None, 'race_raw': 'Native American', 'suspects': None, 'publication': '2021-02-05T08:51:00', 'title': 'ZACHARIAH JUWAUN SHORTY', 'coordinates': [], 'hair_raw': 'Black', 'languages': None, 'complexion': None, 'build': None, 'details': "<p>The Federal Bureau of Investigation's Albuquerque Field Office is asking for the public's assistance in identifying the person(s) responsible for the homicide of Zachariah Juwaun Shorty.</p>\r\n<p>\xa0</p>\r\n<p>On July 25, 2020, Shorty was found deceased on a dirt pathway in a field in Nenahnezad, New Mexico, on the Navajo Nation. The cause of death was gunshot wounds.</p>\r\n<p>\xa0</p>\r\n<p>He was last seen on July 21, 2020, in the area of the Journey Inn in Farmington, New Mexico.</p>", 'status': 'na', 'legat_names': None, 'eyes': 'brown', 'person_classification': 'Main', 'description': 'Homicide Victim\r\nNenahnezad, New Mexico\r\nJuly 25, 2020', 'images': [{'large': 'https://www.fbi.gov/wanted/seeking-info/zachariah-juwaun-shorty/@@images/image/large', 'caption': 'Photograph taken in 2019', 'thumb': 'https://www.fbi.gov/wanted/seeking-info/zachariah-juwaun-shorty/@@images/image/thumb', 'original': 'https://www.fbi.gov/wanted/seeking-info/zachariah-juwaun-shorty/@@images/image'}, {'large': 'https://www.fbi.gov/wanted/seeking-info/zachariah-juwaun-shorty/3.png/@@images/image/large', 'caption': '', 'thumb': 'https://www.fbi.gov/wanted/seeking-info/zachariah-juwaun-shorty/3.png/@@images/image/thumb', 'original': 'https://www.fbi.gov/wanted/seeking-info/zachariah-juwaun-shorty/3.png'}, {'large': 'https://www.fbi.gov/wanted/seeking-info/zachariah-juwaun-shorty/4.jpg/@@images/image/large', 'caption': '', 'thumb': 'https://www.fbi.gov/wanted/seeking-info/zachariah-juwaun-shorty/4.jpg/@@images/image/thumb', 'original': 'https://www.fbi.gov/wanted/seeking-info/zachariah-juwaun-shorty/4.jpg'}, {'large': 'https://www.fbi.gov/wanted/seeking-info/zachariah-juwaun-shorty/1.jpg/@@images/image/large', 'caption': '', 'thumb': 'https://www.fbi.gov/wanted/seeking-info/zachariah-juwaun-shorty/1.jpg/@@images/image/thumb', 'original': 'https://www.fbi.gov/wanted/seeking-info/zachariah-juwaun-shorty/1.jpg'}], 'possible_countries': None, 'weight_min': 130, 'additional_information': None, 'remarks': '<p>Shorty lived in Kirtland, New Mexico.</p>', 'path': '/wanted/seeking-info/zachariah-juwaun-shorty', 'sex': 'Male', 'eyes_raw': 'Brown', 'weight_max': 130, 'reward_min': 0, 'url': 'https://www.fbi.gov/wanted/seeking-info/zachariah-juwaun-shorty', 'possible_states': None, 'modified': '2021-04-16T13:38:09+00:00', 'reward_max': 0, 'race': 'native', 'height_max': 65, 'place_of_birth': None, 'height_min': 65, 'warning_message': None, '@id': 'https://api.fbi.gov/@wanted-person/f042ad53ce1c4b68ab820440a9529c67'}, {'files': [{'url': 'https://www.fbi.gov/wanted/seeking-info/donnie-wade-barney/download.pdf', 'name': 'English'}, {'url': 'https://www.fbi.gov/wanted/seeking-info/donnie-wade-barney/barney-navajo-12-4-2020.pdf/@@download/file/Barney Navajo 12-4-2020.pdf', 'name': 'DINÉ BIZAAD K’EHGO'}], 'age_range': None, 'uid': '464b182870d54a15999b68117bda9912', 'weight': '180 pounds', 'occupations': None, 'field_offices': ['albuquerque'], 'locations': None, 'reward_text': 'The FBI is offering a reward of up to $1,000 for information leading to the arrest and conviction of the person or persons responsible for the death of Donnie Wade Barney.', 'hair': 'black', 'ncic': None, 'dates_of_birth_used': ['October 25, 1984'], 'caution': None, 'nationality': None, 'age_min': None, 'age_max': None, 'scars_and_marks': None, 'subjects': ['Seeking Information', 'Indian Country', 'Navajo'], 'aliases': None, 'race_raw': 'Native American', 'suspects': None, 'publication': '2018-08-01T13:12:00', 'title': 'DONNIE WADE BARNEY', 'coordinates': [], 'hair_raw': 'Black', 'languages': None, 'complexion': None, 'build': None, 'details': "<p>The Federal Bureau of Investigation's Albuquerque Field Office is asking for the public's assistance in identifying the person(s) responsible for the homicide of Donnie Wade Barney.</p>\r\n<p>\xa0</p>\r\n<p>On August 19, 2017, Barney's body was discovered inside a hogan - a traditional Navajo hut of logs and earth - on Shadow Farm Road in Rehoboth, New Mexico. An autopsy indicated Barney died from stab wounds to his torso.</p>", 'status': 'na', 'legat_names': None, 'eyes': 'brown', 'person_classification': 'Victim', 'description': 'Homicide Victim\r\nRehoboth, New Mexico\r\nAugust 19, 2017', 'images': [{'large': 'https://www.fbi.gov/wanted/seeking-info/donnie-wade-barney/@@images/image/large', 'caption': 'Photograph taken in 2016', 'thumb': 'https://www.fbi.gov/wanted/seeking-info/donnie-wade-barney/@@images/image/thumb', 'original': 'https://www.fbi.gov/wanted/seeking-info/donnie-wade-barney/@@images/image'}], 'possible_countries': None, 'weight_min': 180, 'additional_information': None, 'remarks': None, 'path': '/wanted/seeking-info/donnie-wade-barney', 'sex': 'Male', 'eyes_raw': 'Brown', 'weight_max': 180, 'reward_min': 0, 'url': 'https://www.fbi.gov/wanted/seeking-info/donnie-wade-barney', 'possible_states': None, 'modified': '2021-04-16T13:05:41+00:00', 'reward_max': 0, 'race': 'native', 'height_max': 70, 'place_of_birth': None, 'height_min': 70, 'warning_message': None, '@id': 'https://api.fbi.gov/@wanted-person/464b182870d54a15999b68117bda9912'}]



```python
response = requests.get('https://www.fruityvice.com/api/fruit/carbohydrates/', params={"min": "0"})
response.json()
```




    [{'genus': 'Fragaria',
      'name': 'Strawberry',
      'id': 3,
      'family': 'Rosaceae',
      'order': 'Rosales',
      'nutritions': {'carbohydrates': 5.5,
       'protein': 0.8,
       'fat': 0.4,
       'calories': 29,
       'sugar': 5.4}},
     {'genus': 'Musa',
      'name': 'Banana',
      'id': 1,
      'family': 'Musaceae',
      'order': 'Zingiberales',
      'nutritions': {'carbohydrates': 22,
       'protein': 1,
       'fat': 0.2,
       'calories': 96,
       'sugar': 17.2}},
     {'genus': 'Solanum',
      'name': 'Tomato',
      'id': 5,
      'family': 'Solanaceae',
      'order': 'Solanales',
      'nutritions': {'carbohydrates': 3.9,
       'protein': 0.9,
       'fat': 0.2,
       'calories': 74,
       'sugar': 2.6}},
     {'genus': 'Pyrus',
      'name': 'Pear',
      'id': 4,
      'family': 'Rosaceae',
      'order': 'Rosales',
      'nutritions': {'carbohydrates': 15,
       'protein': 0.4,
       'fat': 0.1,
       'calories': 57,
       'sugar': 10}},
     {'genus': 'Prunus',
      'name': 'Cherry',
      'id': 9,
      'family': 'Rosaceae',
      'order': 'None',
      'nutritions': {'carbohydrates': 12,
       'protein': 1,
       'fat': 0.3,
       'calories': 50,
       'sugar': 8}},
     {'genus': 'Ananas',
      'name': 'Pineapple',
      'id': 10,
      'family': 'Bromeliaceae',
      'order': 'Poales',
      'nutritions': {'carbohydrates': 13.12,
       'protein': 0.54,
       'fat': 0.12,
       'calories': 50,
       'sugar': 9.85}},
     {'genus': 'Citrus',
      'name': 'Orange',
      'id': 2,
      'family': 'Rutaceae',
      'order': 'Sapindales',
      'nutritions': {'carbohydrates': 8.3,
       'protein': 1,
       'fat': 0.2,
       'calories': 43,
       'sugar': 8.2}},
     {'genus': 'Rubus',
      'name': 'Raspberry',
      'id': 23,
      'family': 'Rosaceae',
      'order': 'Rosales',
      'nutritions': {'carbohydrates': 12,
       'protein': 1.2,
       'fat': 0.7,
       'calories': 53,
       'sugar': 4.4}},
     {'genus': 'Citrullus',
      'name': 'Watermelon',
      'id': 25,
      'family': 'Cucurbitaceae',
      'order': 'Cucurbitales',
      'nutritions': {'carbohydrates': 8,
       'protein': 0.6,
       'fat': 0.2,
       'calories': 30,
       'sugar': 6}},
     {'genus': 'Citrus',
      'name': 'Lemon',
      'id': 26,
      'family': 'Rutaceae',
      'order': 'Sapindales',
      'nutritions': {'carbohydrates': 9,
       'protein': 1.1,
       'fat': 0.3,
       'calories': 29,
       'sugar': 2.5}},
     {'genus': 'Mangifera',
      'name': 'Mango',
      'id': 27,
      'family': 'Anacardiaceae',
      'order': 'Sapindales',
      'nutritions': {'carbohydrates': 15,
       'protein': 0.82,
       'fat': 0.38,
       'calories': 60,
       'sugar': 13.7}},
     {'genus': 'Fragaria',
      'name': 'Blueberry',
      'id': 33,
      'family': 'Rosaceae',
      'order': 'Rosales',
      'nutritions': {'carbohydrates': 5.5,
       'protein': 0,
       'fat': 0.4,
       'calories': 29,
       'sugar': 5.4}},
     {'genus': 'Malus',
      'name': 'Apple',
      'id': 6,
      'family': 'Rosaceae',
      'order': 'Rosales',
      'nutritions': {'carbohydrates': 11.4,
       'protein': 0.3,
       'fat': 0.4,
       'calories': 52,
       'sugar': 10.3}},
     {'genus': 'Psidium',
      'name': 'Guava',
      'id': 37,
      'family': 'Myrtaceae',
      'order': 'Myrtales',
      'nutritions': {'carbohydrates': 14,
       'protein': 2.6,
       'fat': 1,
       'calories': 68,
       'sugar': 9}},
     {'genus': 'Prunus',
      'name': 'Apricot',
      'id': 35,
      'family': 'Rosaceae',
      'order': 'Rosales',
      'nutritions': {'carbohydrates': 3.9,
       'protein': 0.5,
       'fat': 0.1,
       'calories': 15,
       'sugar': 3.2}}]




```python
response = requests.get('https://api.imgflip.com/get_memes')
response.json()
```




    {'success': True,
     'data': {'memes': [{'id': '181913649',
        'name': 'Drake Hotline Bling',
        'url': 'https://i.imgflip.com/30b1gx.jpg',
        'width': 1200,
        'height': 1200,
        'box_count': 2},
       {'id': '112126428',
        'name': 'Distracted Boyfriend',
        'url': 'https://i.imgflip.com/1ur9b0.jpg',
        'width': 1200,
        'height': 800,
        'box_count': 3},
       {'id': '87743020',
        'name': 'Two Buttons',
        'url': 'https://i.imgflip.com/1g8my4.jpg',
        'width': 600,
        'height': 908,
        'box_count': 2},
       {'id': '129242436',
        'name': 'Change My Mind',
        'url': 'https://i.imgflip.com/24y43o.jpg',
        'width': 482,
        'height': 361,
        'box_count': 2},
       {'id': '131087935',
        'name': 'Running Away Balloon',
        'url': 'https://i.imgflip.com/261o3j.jpg',
        'width': 761,
        'height': 1024,
        'box_count': 5},
       {'id': '247375501',
        'name': 'Buff Doge vs. Cheems',
        'url': 'https://i.imgflip.com/43a45p.png',
        'width': 937,
        'height': 720,
        'box_count': 4},
       {'id': '124822590',
        'name': 'Left Exit 12 Off Ramp',
        'url': 'https://i.imgflip.com/22bdq6.jpg',
        'width': 804,
        'height': 767,
        'box_count': 3},
       {'id': '217743513',
        'name': 'UNO Draw 25 Cards',
        'url': 'https://i.imgflip.com/3lmzyx.jpg',
        'width': 500,
        'height': 494,
        'box_count': 2},
       {'id': '222403160',
        'name': 'Bernie I Am Once Again Asking For Your Support',
        'url': 'https://i.imgflip.com/3oevdk.jpg',
        'width': 750,
        'height': 750,
        'box_count': 2},
       {'id': '102156234',
        'name': 'Mocking Spongebob',
        'url': 'https://i.imgflip.com/1otk96.jpg',
        'width': 502,
        'height': 353,
        'box_count': 2},
       {'id': '438680',
        'name': 'Batman Slapping Robin',
        'url': 'https://i.imgflip.com/9ehk.jpg',
        'width': 400,
        'height': 387,
        'box_count': 2},
       {'id': '131940431',
        'name': "Gru's Plan",
        'url': 'https://i.imgflip.com/26jxvz.jpg',
        'width': 700,
        'height': 449,
        'box_count': 4},
       {'id': '93895088',
        'name': 'Expanding Brain',
        'url': 'https://i.imgflip.com/1jwhww.jpg',
        'width': 857,
        'height': 1202,
        'box_count': 4},
       {'id': '188390779',
        'name': 'Woman Yelling At Cat',
        'url': 'https://i.imgflip.com/345v97.jpg',
        'width': 680,
        'height': 438,
        'box_count': 2},
       {'id': '1035805',
        'name': 'Boardroom Meeting Suggestion',
        'url': 'https://i.imgflip.com/m78d.jpg',
        'width': 500,
        'height': 649,
        'box_count': 4},
       {'id': '252600902',
        'name': 'Always Has Been',
        'url': 'https://i.imgflip.com/46e43q.png',
        'width': 960,
        'height': 540,
        'box_count': 2},
       {'id': '4087833',
        'name': 'Waiting Skeleton',
        'url': 'https://i.imgflip.com/2fm6x.jpg',
        'width': 298,
        'height': 403,
        'box_count': 2},
       {'id': '226297822',
        'name': 'Panik Kalm Panik',
        'url': 'https://i.imgflip.com/3qqcim.png',
        'width': 640,
        'height': 881,
        'box_count': 3},
       {'id': '178591752',
        'name': 'Tuxedo Winnie The Pooh',
        'url': 'https://i.imgflip.com/2ybua0.png',
        'width': 800,
        'height': 582,
        'box_count': 2},
       {'id': '135256802',
        'name': 'Epic Handshake',
        'url': 'https://i.imgflip.com/28j0te.jpg',
        'width': 900,
        'height': 645,
        'box_count': 3},
       {'id': '97984',
        'name': 'Disaster Girl',
        'url': 'https://i.imgflip.com/23ls.jpg',
        'width': 500,
        'height': 375,
        'box_count': 2},
       {'id': '119139145',
        'name': 'Blank Nut Button',
        'url': 'https://i.imgflip.com/1yxkcp.jpg',
        'width': 600,
        'height': 446,
        'box_count': 2},
       {'id': '148909805',
        'name': 'Monkey Puppet',
        'url': 'https://i.imgflip.com/2gnnjh.jpg',
        'width': 923,
        'height': 768,
        'box_count': 2},
       {'id': '80707627',
        'name': 'Sad Pablo Escobar',
        'url': 'https://i.imgflip.com/1c1uej.jpg',
        'width': 720,
        'height': 709,
        'box_count': 3},
       {'id': '114585149',
        'name': 'Inhaling Seagull',
        'url': 'https://i.imgflip.com/1w7ygt.jpg',
        'width': 1269,
        'height': 2825,
        'box_count': 4},
       {'id': '100777631',
        'name': 'Is This A Pigeon',
        'url': 'https://i.imgflip.com/1o00in.jpg',
        'width': 1587,
        'height': 1425,
        'box_count': 3},
       {'id': '110163934',
        'name': "I Bet He's Thinking About Other Women",
        'url': 'https://i.imgflip.com/1tl71a.jpg',
        'width': 1654,
        'height': 930,
        'box_count': 2},
       {'id': '91538330',
        'name': 'X, X Everywhere',
        'url': 'https://i.imgflip.com/1ihzfe.jpg',
        'width': 2118,
        'height': 1440,
        'box_count': 2},
       {'id': '61579',
        'name': 'One Does Not Simply',
        'url': 'https://i.imgflip.com/1bij.jpg',
        'width': 568,
        'height': 335,
        'box_count': 2},
       {'id': '180190441',
        'name': "They're The Same Picture",
        'url': 'https://i.imgflip.com/2za3u1.jpg',
        'width': 1363,
        'height': 1524,
        'box_count': 3},
       {'id': '27813981',
        'name': 'Hide the Pain Harold',
        'url': 'https://i.imgflip.com/gk5el.jpg',
        'width': 480,
        'height': 601,
        'box_count': 2},
       {'id': '123999232',
        'name': 'The Scroll Of Truth',
        'url': 'https://i.imgflip.com/21tqf4.jpg',
        'width': 1280,
        'height': 1236,
        'box_count': 2},
       {'id': '195515965',
        'name': 'Clown Applying Makeup',
        'url': 'https://i.imgflip.com/38el31.jpg',
        'width': 750,
        'height': 798,
        'box_count': 4},
       {'id': '101470',
        'name': 'Ancient Aliens',
        'url': 'https://i.imgflip.com/26am.jpg',
        'width': 500,
        'height': 437,
        'box_count': 2},
       {'id': '216951317',
        'name': 'Guy Holding Cardboard Sign',
        'url': 'https://i.imgflip.com/3l60ph.jpg',
        'width': 700,
        'height': 702,
        'box_count': 2},
       {'id': '89370399',
        'name': 'Roll Safe Think About It',
        'url': 'https://i.imgflip.com/1h7in3.jpg',
        'width': 702,
        'height': 395,
        'box_count': 2},
       {'id': '155067746',
        'name': 'Surprised Pikachu',
        'url': 'https://i.imgflip.com/2kbn1e.jpg',
        'width': 1893,
        'height': 1893,
        'box_count': 3},
       {'id': '134797956',
        'name': 'American Chopper Argument',
        'url': 'https://i.imgflip.com/2896ro.jpg',
        'width': 640,
        'height': 1800,
        'box_count': 5},
       {'id': '79132341',
        'name': 'Bike Fall',
        'url': 'https://i.imgflip.com/1b42wl.jpg',
        'width': 500,
        'height': 680,
        'box_count': 3},
       {'id': '21735',
        'name': 'The Rock Driving',
        'url': 'https://i.imgflip.com/grr.jpg',
        'width': 568,
        'height': 700,
        'box_count': 2},
       {'id': '135678846',
        'name': 'Who Killed Hannibal',
        'url': 'https://i.imgflip.com/28s2gu.jpg',
        'width': 1280,
        'height': 1440,
        'box_count': 3},
       {'id': '124055727',
        'name': "Y'all Got Any More Of That",
        'url': 'https://i.imgflip.com/21uy0f.jpg',
        'width': 600,
        'height': 471,
        'box_count': 2},
       {'id': '259237855',
        'name': 'Laughing Leo',
        'url': 'https://i.imgflip.com/4acd7j.png',
        'width': 470,
        'height': 470,
        'box_count': 2},
       {'id': '55311130',
        'name': 'This Is Fine',
        'url': 'https://i.imgflip.com/wxica.jpg',
        'width': 580,
        'height': 282,
        'box_count': 2},
       {'id': '175540452',
        'name': 'Unsettled Tom',
        'url': 'https://i.imgflip.com/2wifvo.jpg',
        'width': 680,
        'height': 550,
        'box_count': 2},
       {'id': '28251713',
        'name': 'Oprah You Get A',
        'url': 'https://i.imgflip.com/gtj5t.jpg',
        'width': 620,
        'height': 465,
        'box_count': 2},
       {'id': '17699',
        'name': 'Buddy Christ',
        'url': 'https://i.imgflip.com/dnn.jpg',
        'width': 400,
        'height': 400,
        'box_count': 2},
       {'id': '6235864',
        'name': 'Finding Neverland',
        'url': 'https://i.imgflip.com/3pnmg.jpg',
        'width': 423,
        'height': 600,
        'box_count': 3},
       {'id': '8072285',
        'name': 'Doge',
        'url': 'https://i.imgflip.com/4t0m5.jpg',
        'width': 620,
        'height': 620,
        'box_count': 5},
       {'id': '61520',
        'name': 'Futurama Fry',
        'url': 'https://i.imgflip.com/1bgw.jpg',
        'width': 552,
        'height': 414,
        'box_count': 2},
       {'id': '3218037',
        'name': "This Is Where I'd Put My Trophy If I Had One",
        'url': 'https://i.imgflip.com/1wz1x.jpg',
        'width': 300,
        'height': 418,
        'box_count': 2},
       {'id': '196652226',
        'name': 'Spongebob Ight Imma Head Out',
        'url': 'https://i.imgflip.com/392xtu.jpg',
        'width': 822,
        'height': 960,
        'box_count': 2},
       {'id': '61556',
        'name': 'Grandma Finds The Internet',
        'url': 'https://i.imgflip.com/1bhw.jpg',
        'width': 640,
        'height': 480,
        'box_count': 2},
       {'id': '132769734',
        'name': 'Hard To Swallow Pills',
        'url': 'https://i.imgflip.com/271ps6.jpg',
        'width': 680,
        'height': 979,
        'box_count': 2},
       {'id': '84341851',
        'name': 'Evil Kermit',
        'url': 'https://i.imgflip.com/1e7ql7.jpg',
        'width': 700,
        'height': 325,
        'box_count': 2},
       {'id': '14371066',
        'name': 'Star Wars Yoda',
        'url': 'https://i.imgflip.com/8k0sa.jpg',
        'width': 620,
        'height': 714,
        'box_count': 2},
       {'id': '101288',
        'name': 'Third World Skeptical Kid',
        'url': 'https://i.imgflip.com/265k.jpg',
        'width': 426,
        'height': 426,
        'box_count': 2},
       {'id': '101287',
        'name': 'Third World Success Kid',
        'url': 'https://i.imgflip.com/265j.jpg',
        'width': 500,
        'height': 500,
        'box_count': 2},
       {'id': '5496396',
        'name': 'Leonardo Dicaprio Cheers',
        'url': 'https://i.imgflip.com/39t1o.jpg',
        'width': 600,
        'height': 400,
        'box_count': 2},
       {'id': '91545132',
        'name': 'Trump Bill Signing',
        'url': 'https://i.imgflip.com/1ii4oc.jpg',
        'width': 1866,
        'height': 1529,
        'box_count': 2},
       {'id': '161865971',
        'name': 'Marked Safe From',
        'url': 'https://i.imgflip.com/2odckz.jpg',
        'width': 618,
        'height': 499,
        'box_count': 2},
       {'id': '61532',
        'name': 'The Most Interesting Man In The World',
        'url': 'https://i.imgflip.com/1bh8.jpg',
        'width': 550,
        'height': 690,
        'box_count': 2},
       {'id': '99683372',
        'name': 'Sleeping Shaq',
        'url': 'https://i.imgflip.com/1nck6k.jpg',
        'width': 640,
        'height': 631,
        'box_count': 2},
       {'id': '61533',
        'name': 'X All The Y',
        'url': 'https://i.imgflip.com/1bh9.jpg',
        'width': 500,
        'height': 355,
        'box_count': 2},
       {'id': '563423',
        'name': 'That Would Be Great',
        'url': 'https://i.imgflip.com/c2qn.jpg',
        'width': 526,
        'height': 440,
        'box_count': 2},
       {'id': '61544',
        'name': 'Success Kid',
        'url': 'https://i.imgflip.com/1bhk.jpg',
        'width': 500,
        'height': 500,
        'box_count': 2},
       {'id': '4173692',
        'name': 'Scared Cat',
        'url': 'https://i.imgflip.com/2hgfw.jpg',
        'width': 620,
        'height': 464,
        'box_count': 2},
       {'id': '183518946',
        'name': 'Blank Transparent Square',
        'url': 'https://i.imgflip.com/319g4i.png',
        'width': 1000,
        'height': 1000,
        'box_count': 2},
       {'id': '61546',
        'name': 'Brace Yourselves X is Coming',
        'url': 'https://i.imgflip.com/1bhm.jpg',
        'width': 622,
        'height': 477,
        'box_count': 2},
       {'id': '29617627',
        'name': 'Look At Me',
        'url': 'https://i.imgflip.com/hmt3v.jpg',
        'width': 300,
        'height': 300,
        'box_count': 2},
       {'id': '101511',
        'name': "Don't You Squidward",
        'url': 'https://i.imgflip.com/26br.jpg',
        'width': 500,
        'height': 333,
        'box_count': 2},
       {'id': '157978092',
        'name': 'Presidential Alert',
        'url': 'https://i.imgflip.com/2m20oc.jpg',
        'width': 920,
        'height': 534,
        'box_count': 2},
       {'id': '285870',
        'name': 'Squidward',
        'url': 'https://i.imgflip.com/64ku.jpg',
        'width': 500,
        'height': 750,
        'box_count': 2},
       {'id': '163573',
        'name': 'Imagination Spongebob',
        'url': 'https://i.imgflip.com/3i7p.jpg',
        'width': 500,
        'height': 366,
        'box_count': 2},
       {'id': '8279814',
        'name': 'Cute Cat',
        'url': 'https://i.imgflip.com/4xgqu.jpg',
        'width': 480,
        'height': 532,
        'box_count': 2},
       {'id': '47235368',
        'name': 'Good Fellas Hilarious',
        'url': 'https://i.imgflip.com/s4f1k.jpg',
        'width': 1600,
        'height': 1150,
        'box_count': 2},
       {'id': '61585',
        'name': 'Bad Luck Brian',
        'url': 'https://i.imgflip.com/1bip.jpg',
        'width': 475,
        'height': 562,
        'box_count': 2},
       {'id': '6531067',
        'name': 'See Nobody Cares',
        'url': 'https://i.imgflip.com/3vzej.jpg',
        'width': 620,
        'height': 676,
        'box_count': 2},
       {'id': '61580',
        'name': 'Too Damn High',
        'url': 'https://i.imgflip.com/1bik.jpg',
        'width': 420,
        'height': 316,
        'box_count': 2},
       {'id': '460541',
        'name': 'Jack Sparrow Being Chased',
        'url': 'https://i.imgflip.com/9vct.jpg',
        'width': 500,
        'height': 375,
        'box_count': 2},
       {'id': '101716',
        'name': 'Yo Dawg Heard You',
        'url': 'https://i.imgflip.com/26hg.jpg',
        'width': 500,
        'height': 323,
        'box_count': 2},
       {'id': '101910402',
        'name': 'Who Would Win?',
        'url': 'https://i.imgflip.com/1ooaki.jpg',
        'width': 802,
        'height': 500,
        'box_count': 2},
       {'id': '259680',
        'name': 'Am I The Only One Around Here',
        'url': 'https://i.imgflip.com/5kdc.jpg',
        'width': 500,
        'height': 348,
        'box_count': 2},
       {'id': '405658',
        'name': 'Grumpy Cat',
        'url': 'https://i.imgflip.com/8p0a.jpg',
        'width': 500,
        'height': 617,
        'box_count': 2},
       {'id': '29562797',
        'name': "I'm The Captain Now",
        'url': 'https://i.imgflip.com/hlmst.jpg',
        'width': 478,
        'height': 350,
        'box_count': 2},
       {'id': '40945639',
        'name': 'Dr Evil Laser',
        'url': 'https://i.imgflip.com/odluv.jpg',
        'width': 500,
        'height': 405,
        'box_count': 2},
       {'id': '12403754',
        'name': 'Bad Pun Dog',
        'url': 'https://i.imgflip.com/7dusq.jpg',
        'width': 575,
        'height': 1200,
        'box_count': 3},
       {'id': '61527',
        'name': 'Y U No',
        'url': 'https://i.imgflip.com/1bh3.jpg',
        'width': 500,
        'height': 500,
        'box_count': 2},
       {'id': '61539',
        'name': 'First World Problems',
        'url': 'https://i.imgflip.com/1bhf.jpg',
        'width': 552,
        'height': 367,
        'box_count': 2},
       {'id': '1367068',
        'name': 'I Should Buy A Boat Cat',
        'url': 'https://i.imgflip.com/tau4.jpg',
        'width': 500,
        'height': 368,
        'box_count': 2},
       {'id': '61581',
        'name': 'Put It Somewhere Else Patrick',
        'url': 'https://i.imgflip.com/1bil.jpg',
        'width': 343,
        'height': 604,
        'box_count': 2},
       {'id': '922147',
        'name': 'Laughing Men In Suits',
        'url': 'https://i.imgflip.com/jrj7.jpg',
        'width': 500,
        'height': 333,
        'box_count': 2},
       {'id': '61582',
        'name': 'Creepy Condescending Wonka',
        'url': 'https://i.imgflip.com/1bim.jpg',
        'width': 550,
        'height': 545,
        'box_count': 2},
       {'id': '1202623',
        'name': 'Keep Calm And Carry On Red',
        'url': 'https://i.imgflip.com/pry7.jpg',
        'width': 500,
        'height': 704,
        'box_count': 2},
       {'id': '21604248',
        'name': 'Mugatu So Hot Right Now',
        'url': 'https://i.imgflip.com/cv1y0.jpg',
        'width': 620,
        'height': 497,
        'box_count': 2},
       {'id': '53764',
        'name': 'Peter Parker Cry',
        'url': 'https://i.imgflip.com/15hg.jpg',
        'width': 400,
        'height': 992,
        'box_count': 4},
       {'id': '16464531',
        'name': "But That's None Of My Business",
        'url': 'https://i.imgflip.com/9sw43.jpg',
        'width': 600,
        'height': 600,
        'box_count': 2},
       {'id': '56225174',
        'name': 'Be Like Bill',
        'url': 'https://i.imgflip.com/xh3me.jpg',
        'width': 913,
        'height': 907,
        'box_count': 4},
       {'id': '71428573',
        'name': 'Say it Again, Dexter',
        'url': 'https://i.imgflip.com/16iyn1.jpg',
        'width': 698,
        'height': 900,
        'box_count': 2},
       {'id': '28034788',
        'name': 'Marvel Civil War 1',
        'url': 'https://i.imgflip.com/govs4.jpg',
        'width': 423,
        'height': 734,
        'box_count': 2}]}}



Elige una api pública (a poder ser sin token de autorización) y explora sus endpoints con alguna librería de protocolo http

https://github.com/public-apis/public-apis
