import bs4
import requests
def sum_nums (htmname):
    summ = 0
    htmlfile=open(htmname,"r").read()
    for ele in bs4.BeautifulSoup(htmlfile).find_all('span',{'class':'comments'}):
        summ+=int(ele.text)
    return summ

print('all intergers in the sample has a sum of {}'.format(sum_nums('6ASAMDATA.html')))
print('all intergers in the actual has a sum of {}'.format(sum_nums('6AACTDATA.html')))