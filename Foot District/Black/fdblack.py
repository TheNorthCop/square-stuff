import requests
import random
import string
import json
import time


print ('Created by @WashedChief')
print ('///////////////////////////////////////////////////////')

config = json.loads(open('setup').read())
Firstname = config['First Name'] 
Lastname = config['Last Name'] 
Size = config['Size']
Email1 = config['Email']


def gettoken():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    token = 'https://footdistrict.typeform.com/app/form/result/token/l5emIz/default'
    tokenreq = requests.get(token, headers=headers)
    #print (tokenreq.status)
    print (tokenreq.text)
    formtoken = tokenreq.text
    
    sending(formtoken)

def sending(formtoken):
 
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    
    url = 'https://footdistrict.typeform.com/app/form/submit/l5emIz'
 
    
    name_extra = ''.join(random.choice(string.digits))
    name_extra2 = ''.join(random.choice(string.digits))
    name_extra3 = ''.join(random.choice(string.digits))
    name_extra4 = ''.join(random.choice(string.digits))
    
    Email = (Email1 + '+' + name_extra + name_extra2 + name_extra3 + '@gmail.com')  
    
    data = {

        'form[list:ooyoEXWhdncc][choices]': 'English',
        'form[list:ooyoEXWhdncc][other]': '',
        'form[textfield:pSRqZ82DlaQK]': (Firstname + ' ' + Lastname),
        'form[email:Hycby5KHfCbH]': Email,
        'form[dropdown:q1DOJXhp5Wxk]': Size,
        'form[terms:kduEWYRwgQB1]': '1',
        'form[terms:JHKimWLumYtA]': '1',
        'form[token]': formtoken,
        'form[landed_at]': '1547166406',
        'form[language]': 'en'

    }

    r = requests.post(url, allow_redirects=False, data= data, headers=headers)
    print (r.text)
    if 'success' in r.text:
        print ('Entered raffle for: First Name = {} Last Name = {} Size = {} Email = {} with token {}'.format(Firstname, Lastname, Size, Email, formtoken))
    
    else: 
        print (r)
        print ('error') 
        print ('Error for Submitting raffle for: First Name = {} Last Name = {} Size = {} Email = {} with token {}'.format(Firstname, Lastname, Size, Email, formtoken))


def main():
    while(True):
        #sending()
        gettoken()
        
        
    return

if __name__ == "__main__":
    main()
