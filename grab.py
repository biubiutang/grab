import urllib2
from BeautifulSoup import BeautifulSoup
import xlwt
import codecs

book = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = book.add_sheet('dede',cell_overwrite_ok=True)
#url='http://detail.zol.com.cn/274/273715/review.shtml'
url= 'http://detail.zol.com.cn/xhr3_Review_GetListAndPage_isFilter=1%5EproId=273715%5Epage=2.html'
request=urllib2.Request(url)
response = urllib2.urlopen(request)
html = response.read()
parser= BeautifulSoup(html)

print type(html)

row1=0
row2=0
comments_all=parser.findAll('div','comments-content')
		
for i in comments_all:
	strong_list= i.findAll('strong')
	for child in strong_list:
		sheet.write(row2,0,child.string) 
		row2+=1
for m in comments_all:
	comments_list= m.findAll('span')
	for child in comments_list:
		sheet.write(row1,1,child.string)
		row1+=1
book.save('commentsjd.xls')
