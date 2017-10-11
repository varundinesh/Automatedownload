import time
from selenium import webdriver
chrome_path = r"C:\Users\Varun\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

def pdfloader(x):

    driver.get(r"https://my.dynamic-learning.co.uk/Titles/AQAPhysics2WeT_9781471807787/Content/OEBPS/page"+str(x)+".xhtml")

    driver.execute_script('''window.print();''') #call print function
    if str(x)== str("001"):                           #for initioal load
        time.sleep(10)
    else:
        time.sleep(1)

rec=0
def autoincrement():  #generate page nos
 global rec
 pstart = 1
 pinterval = 1
 if (rec == 0):
  rec = pstart
 else:
  rec = rec + pinterval
 return str(rec).zfill(3)

for x in range(0,305):
    pdfloader(autoincrement())

#################################################   autohotkey code
'''
#F2::                   #perform script when press window key + F2
loop,999999999999999    #no of iterations ,you may need to increase this digit
{
send {Enter}
sleep 500
}
return
'''

