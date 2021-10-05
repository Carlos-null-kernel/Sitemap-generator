import os
import os, time, datetime
url = input("URL, your site: ");
sitemap = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">";
pasta = input("root file folder: ");
sitemapfile="";
for diretorio, subpastas, arquivos in os.walk(pasta):
    created = os.path.getctime(diretorio);
    year,month,day,hour,minute,second=time.localtime(created)[:-3]
    parte1 = "\n<url> \n<loc>" + diretorio.replace(pasta, url).replace("\\","/");
    parte2 = "</loc> \n<lastmod>";
    parte3 = "%02d-%02d-%d"%(year,month,day);
    parte4 = "</lastmod>\n<priority>0.8</priority>\n</url>\n";
    concaternar = parte1 + parte2 + parte3 + parte4;
    sitemapfile = sitemapfile + concaternar;
    print(sitemapfile);
else:
    final = sitemap + sitemapfile + "</urlset> "
    #print(final)
    try:
        arquivo = open(pasta + "\sitemap.xml", 'w');
        arquivo.write(final);
        arquivo.close();
    except FileNotFoundError:
        arquivo = open(pasta + "\sitemap.xml", 'w');
        arquivo.write(final);
        arquivo.close();
        