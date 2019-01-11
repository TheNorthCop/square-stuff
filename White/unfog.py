import requests
import random
import string
import json
import time


print ('Created by @WashedChief')
print ('///////////////////////////////////////////////////////')

config = json.loads(open('setup').read())

Firstname = config['First Name'] 
Size = config['Size']
Email1 = config['Email']
Address = config['Shipping Address']
PhoneNumber = config['Phone Number']


def gettoken():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    token = 'https://unknwn.typeform.com/app/form/result/token/xbZN7i/default.json'
    tokenreq = requests.get(token, headers=headers)
    #print (tokenreq.status)
    print (tokenreq.text)
    formtoken = tokenreq.text
    
    sending(formtoken)

def sending(formtoken):
 
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    
    url = 'https://unknwn.typeform.com/app/form/submit/xbZN7i'
 
    
    name_extra = ''.join(random.choice(string.digits))
    name_extra2 = ''.join(random.choice(string.digits))
    name_extra3 = ''.join(random.choice(string.digits))
    name_extra4 = ''.join(random.choice(string.digits))
    
    Email = (Email1 + '+' + name_extra + name_extra2 + name_extra3 + '@gmail.com')  
    
    data = {

        'form[textfield:Q1uSARM6Hftc]': Firstname,
        'form[dropdown:scAixp8kbyat]': Size,
        'form[email:uVSbIrml2yRH]': Email,
        'form[textfield:XLPlDb0szZf4]': Address,
        'form[textfield:blPtC6TItch7]': PhoneNumber,
        'form[yes-no:BTfW7xl5mOVs]': '0',
        'form[token]': formtoken,
        'form[landed_at]': '1547172307',
        'form[language]': 'en'

    }

    r = requests.post(url, allow_redirects=False, data= data, headers=headers)
    print (r.text)
    if 'success' in r.text:
        print ('Entered raffle for: First Name = {} Size = {} Email = {} with token {}'.format(Firstname, Size, Email, formtoken))
        #print (data)
    
    else: 
        print (r)
        print ('error') 
        print ('Entered raffle for: First Name = {} Size = {} Email = {} with token {}'.format(Firstname, Size, Email, formtoken))


def main():
    while(True):
        #sending()
        gettoken()
        
        
    return

if __name__ == "__main__":
    main()
