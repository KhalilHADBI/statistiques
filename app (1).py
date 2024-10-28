import requests
import datetime
import time
import calendar
import pandas as pd
url_base = 'https://analytics.tadao.fr'
#url_base = 'http://umami.docker1.local'


def Login():
    methode = '/api/auth/login'
    url = url_base+methode
    json = {
        "username": "admin",
        "password": "PortailAdminTADAO"
    }
    
    
    try:
        response = requests.post(url, data=json).json()
        return response
        #token = response.json()['token']
        #id = response.json()['user']['id']
        #username = response.json()['user']['username']
        #createdAt = response.json()['user']['createdAt']
        #data={'token': token, 'id': id, 'username': username, 'createdAt': createdAt}
        #return data
    except:
        return False
def Verify(token):
    methode = '/api/auth/verify'
    url = url_base+methode
    headers = {'accept': 'application/json',"Authorization": "Bearer "+token}
    response = requests.get(url, headers=headers).json()
    print(response)

def Websites(token):
    methode = '/api/websites'
    url = url_base+methode
    headers = {'accept': 'application/json',"Authorization": "Bearer "+token}
    response = requests.get(url, headers=headers).json()
    print(response)


def Website_stats(websiteId, month, year):
    res = calendar.monthrange(year, month)
    day = res[1]
    start_date = datetime.datetime.strptime('01.'+str(month)+'.'+str(year)+' 00:00:00', '%d.%m.%Y %H:%M:%S')
    end_date = datetime.datetime.strptime(str(day)+'.'+str(month)+'.'+str(year)+' 23:59:59', '%d.%m.%Y %H:%M:%S')
    start_timestamp = int(time.mktime(start_date.timetuple())*1000)
    end_timestamp = int(time.mktime(end_date.timetuple())*1000)
    login = Login()
    token = login['token']
    #print(token)
    headers = {'accept': 'application/json',"Authorization": "Bearer "+token}
    methode = '/api/websites/'+str(websiteId)+"/stats?startAt="+str(start_timestamp)+"&endAt="+str(end_timestamp)
    print(methode)
    url = url_base+methode
    response = requests.get(url, headers=headers).json()
    print(response)
    # df = pd.DataFrame(response)
    # df.to_csv (str(month)+'_'+str(year)+'.csv', index = None, sep =';')

def Website_metrics(websiteId, month, year):
    res = calendar.monthrange(year, month)
    day = res[1]
    start_date = datetime.datetime.strptime('01.'+str(month)+'.'+str(year)+' 00:00:00', '%d.%m.%Y %H:%M:%S')
    end_date = datetime.datetime.strptime(str(day)+'.'+str(month)+'.'+str(year)+' 23:59:59', '%d.%m.%Y %H:%M:%S')
    start_timestamp = int(time.mktime(start_date.timetuple())*1000)
    end_timestamp = int(time.mktime(end_date.timetuple())*1000)
    login = Login()
    token = login['token']
    #print(token)
    headers = {'accept': 'application/json',"Authorization": "Bearer "+token}
    methode = '/api/websites/'+str(websiteId)+"/metrics?startAt="+str(start_timestamp)+"&endAt="+str(end_timestamp)+"&type=title"
    print(methode)
    url = url_base+methode
    response = requests.get(url, headers=headers)
    print(response)
    df = pd.DataFrame(response.json())
    df.to_csv (str(month)+'_'+str(year)+'.csv', index = None, sep =';')
    


def Website_events(websiteId, month, year):
    res = calendar.monthrange(year, month)
    day = res[1]
    start_date = datetime.datetime.strptime('01.'+str(month)+'.'+str(year)+' 00:00:00', '%d.%m.%Y %H:%M:%S')
    end_date = datetime.datetime.strptime(str(day)+'.'+str(month)+'.'+str(year)+' 23:59:59', '%d.%m.%Y %H:%M:%S')
    start_timestamp = int(time.mktime(start_date.timetuple())*1000)
    end_timestamp = int(time.mktime(end_date.timetuple())*1000)
    login = Login()
    token = login['token']
    #print(token)
    headers = {'accept': 'application/json',"Authorization": "Bearer "+token}
    methode = '/api/websites/'+str(websiteId)+"/events?startAt="+str(start_timestamp)+"&endAt="+str(end_timestamp)+"&&unit=hour&timezone=Europe%2FParis"
    print(methode)
    url = url_base+methode
    response = requests.get(url, headers=headers).json()
    print(response)
    #df = pd.DataFrame(response)
    #df.to_csv (str(month)+'_'+str(year)+'.csv', index = None, sep =';')
    #print(response)

def Website_pageviews(websiteId, month, year):
    res = calendar.monthrange(year, month)
    day = res[1]
    start_date = datetime.datetime.strptime('01.'+str(month)+'.'+str(year)+' 00:00:00', '%d.%m.%Y %H:%M:%S')
    end_date = datetime.datetime.strptime(str(day)+'.'+str(month)+'.'+str(year)+' 23:59:59', '%d.%m.%Y %H:%M:%S')
    start_timestamp = int(time.mktime(start_date.timetuple())*1000)
    end_timestamp = int(time.mktime(end_date.timetuple())*1000)
    login = Login()
    token = login['token']
    #print(token)
    headers = {'accept': 'application/json',"Authorization": "Bearer "+token}
    methode = '/api/websites/'+str(websiteId)+"/pageviews?startAt="+str(start_timestamp)+"&endAt="+str(end_timestamp)+"&&unit=hour&timezone=Europe%2FParis"
    print(methode)
    url = url_base+methode
    response = requests.get(url, headers=headers).json()
    print(response)
    #df = pd.DataFrame(response)
    #df.to_csv (str(month)+'_'+str(year)+'.csv', index = None, sep =';')
    #print(response)

if __name__ == '__main__':
    #login = Login()
    #token = login['token']

    #Websites(token)
    #Verify(token)
    #Website_stats('e37dec56-59d4-4fc3-87ae-0bac2042f99c',5,2023) #tadao
    Website_metrics('e37dec56-59d4-4fc3-87ae-0bac2042f99c',10,2023) #site tadao
    #Website_events('e37dec56-59d4-4fc3-87ae-0bac2042f99c',5,2023) #tadao
    #Website_pageviews('e37dec56-59d4-4fc3-87ae-0bac2042f99c',5,2023) #tadao