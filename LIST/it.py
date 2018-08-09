#Jangan ganti author , hargai creator cape loh buat nya

import requests,os,re

b="\033[0;34m"
g="\033[1;32m"
w="\033[1;37m"
r="\033[1;31m"
y="\033[1;33m"


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}



def italy():
    global page
    res = requests.get('https://www.insecam.org/en/bycountry/IT/', headers=headers)
    findpage = re.findall('"?page=",\s\d+', res.text)[1]
    rfindpage = findpage.replace('page=", ', '')
    os.system('clear')
    print (g+"|=|============================|=|")
    print (y+"         IPCam Scanner v1")
    print (y+"       Kancot Team - HVmbl3")
    print (y+"   https://github.com/kancotdiq")
    print (g+"|=|============================|=|")
    print ""
    print (str(g)+str("    List page : ")+rfindpage)
    run()
    
def run():
    try:
        page = input(str(b)+"    Page "+str(r)+": "+str(y))
        url = ("https://www.insecam.org/en/bycountry/ID/?page="+str(page))
        print ""
        res = requests.get(url, headers=headers)
        findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
        count = 1
        for _ in findip:
             hasil = findip[count]
             print (str(r)+">>> "+str(y)+hasil+str(r)+" <<<")
             count += 1
    except:
        print ""
        print r+"Makasi udh pake tools kami"+w