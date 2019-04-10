# -*- coding:utf-8 -*-
import requests
import re
print"*******************************************************"
print"Bem-Vindo ao Web Crawler","versão 2.0"
print"*******************************************************"
print"Os links pegos pelo Crawler serão salvos em links.txt e emails.txt\nPara Desliga o Crawler de Control+C"
print"*******************************************************"
print"Digite o endereço para o Crawler busca por links e Pega Emails"
To_crawl = ['http://'+raw_input('Endereço: ')]
email=" "
crawled= set()
emails_found=set()
#useragent para o waf não barra o crawler
head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/2010$'}
#Processo de requisição do siti
while True:
        url= To_crawl[0]
        try:
               req=requests.get(url, headers=head)
        except:
                print"****************************************"
                print "conecção falhou ou Crawler Canelado !"
                print"****************************************"
                To_crawl.remove(url)
                crawled.add(url)
#procurando os links
	html=req.text
        links=re.findall(r'href="?\'?(https?:\/\/[^"\'>]*)', html)
	emails=re.findall(r'[\w\._-]+@[\w_-]+\.[\w\._-]+\w', html)
        print 'Links Pegos: ',url
	print 'emails pegos: ',emails

        To_crawl.remove(url)
        crawled.add(url)
#salvando os links
        for link in links:
                if link not in crawled and link not in To_crawl:
                        To_crawl.append(link)
                        arquivos= open('links.txt','a')
                        arquivos.write(link)
                        arquivos.write("\n")
                        arquivos.close()
	for email in emails:
			emails_found.add(email)
	txt= open('emails.txt','a')
	txt.write(email)
	txt.write("\n")
	txt.close()
