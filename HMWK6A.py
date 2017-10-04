import bs4
import urllib.request
def sum_nums (htmname):
    summ = 0
    htmlfile=urllib.request.urlopen(htmname)
    for ele in bs4.BeautifulSoup(htmlfile).find_all('span',{'class':'comments'}):
        summ+=int(ele.text)
    return summ

print('all intergers in the sample has a sum of {}'.format(sum_nums('http://py4e-data.dr-chuck.net/comments_42.html')))
print('all intergers in the actual has a sum of {}'.format(sum_nums('http://py4e-data.dr-chuck.net/comments_36346.html')))