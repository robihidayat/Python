import urllib
import re

#deklarasi variabel
hasil = {}

#defisini tagnya
itle_exr = r'<title>(.*?)</title>'
time_exr = '<meta name="pubdate" content="(.*?)" itemprop="datePublished" />'
author_exr = r'<div class="author">(.*?) - detikNews</div>'
news_exr = r'<!-- E:read image orientation if potrait load this -->(.*?)<!-- POLONG -->'


#buat menghapus bagian yang gak diperlukan
erase_tag = r'<(.*?)>'


#buka urlnya
htmlfile=urllib.urlopen('http://news.detik.com/berita/3146023/pesawat-cesna-cn235-220-tni-al-ikut-dipamerkan-di-singapore-airshow')
htmltext=htmlfile.read()


#buat Paternnya
pattern2=re.compile(itle_exr)
pattern3=re.compile(time_exr)
pattern4=re.compile(author_exr)

#buat konten, ngilangin bagian yang gak diperlukan 
pattern5=re.compile(news_exr,re.DOTALL)
clean_news = re.findall(pattern5,htmltext)
clean_news = re.sub(erase_tag, '', clean_news[0])
clean_news = re.sub(r'[\t]', '', clean_news)
hasil['Berita'] = re.sub(r'[\n]', '', clean_news)


#regexnya dibuat aja
test = re.findall(pattern2,htmltext)
test2 = re.findall(pattern3,htmltext)
test3 = re.findall(pattern4,htmltext)
#test4 = re.findall(pattern5,htmltext) #GAK usah

#Print Hasilnya
print test,test2,test3,hasil


