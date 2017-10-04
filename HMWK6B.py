import bs4
import urllib.request
def jump (htmname,pos):
    ulist=[]
    namelist=[]
    htmlfile=urllib.request.urlopen(htmname)
    pos=pos-1
    for ele in bs4.BeautifulSoup(htmlfile).find_all('a'):
        ulist.append(ele['href'])
        namelist.append(ele.text)
    return (namelist[pos],ulist[pos])
def jump_int(htmname,pos,repeat):
    urll=htmname
    name=''
    temp=()
    for i in range(repeat):
        temp=jump(urll,pos)
        urll=temp[1]
        name=temp[0]
    return name
print('last name in the sample is {}'.format(jump_int('http://py4e-data.dr-chuck.net/known_by_Fikret.html',3,4)))
print('last name in the actual is {}'.format(jump_int('http://py4e-data.dr-chuck.net/known_by_Bailie.html',18,7)))