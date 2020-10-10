import requests
from bs4 import BeautifulSoup
import smtplib 

# To set the time of activation according to you
import time

# url of the product
URL = 'https://www.amazon.in/F-Goal-Mens-Football-Jersey-Large/dp/B08DTQNCSR/ref=sr_1_44?dchild=1&keywords=football+jersey&qid=1602328910&sr=8-44https://www.amazon.in/dp/B077PWJ8RS/ref=gwdb_bmc_3_CP_Latest_Redmi9Promax?pf_rd_s=merchandised-search-7&pf_rd_t=Gateway&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=G7YAXTJHT0STZ64X64NY&pf_rd_p=6c1f63dd-d673-460c-aa20-1a9261118fde'

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}


def Check_price():

    page = requests.get(URL,headers=headers)


    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    # To scrap the price using product id
    price = soup.find(id="priceblock_ourprice").get_text()
    
#     To convert the string into float for comparison
    converted_price = float(price[1:].replace(",",""))


    # if (converted_price <1100.0):
    #     send_email()

    print(title.strip())
    print(converted_price)

    if(converted_price >1100.0):
        send_email()


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # EHLO = extended hello
    server.ehlo()

    # the password is generated using Google app password after 2-Step verification
    server.login('jangidnaveen05@gmail.com','wxqqbdeoaqsmkheo')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.in/F-Goal-Mens-Football-Jersey-Large/dp/B08DTQNCSR/ref=sr_1_44?dchild=1&keywords=football+jersey&qid=1602328910&sr=8-44https://www.amazon.in/dp/B077PWJ8RS/ref=gwdb_bmc_3_CP_Latest_Redmi9Promax?pf_rd_s=merchandised-search-7&pf_rd_t=Gateway&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=G7YAXTJHT0STZ64X64NY&pf_rd_p=6c1f63dd-d673-460c-aa20-1a9261118fde'
    
    msg=f"Subject: {subject}\n\n{body}"

    server.sendmail(
        # from
        'jangidnaveen05@gmail.com',  

        #to
        'jangidnaveen03@gmail.com',

        msg
    )
    print('HEY THE EMAIL HAS BEEN SENT!')

    server.quit()


Check_price()    

# while(True):

#     Check_price()
#     time.sleep(60*60)    


