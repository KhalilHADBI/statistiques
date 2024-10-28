import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
import os
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta, MO
from copy import deepcopy

# Disable warning about insecure SSL certificate
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#==========================================
# configuration
#==========================================

base_uri = "https://tadao.biz.cognidis.com/"
login = "api_user"
password ="h7i5MsM4B7"
#login = "khalil.hadbi"  # A MODIFIER !!!
#password = "2889yJnPmFb6Gr"  # A MODIFIER !!!

session = requests.Session()

#==========================================
# functions
#==========================================

def do_login():
    r = session.post(base_uri + "login", data = {"login": login, "pass": password}, verify = False)
    if r.status_code != 200:
        raise Exception("Login failed")

def do_call(filename, filters, params, accept, contenttype):

    uri = base_uri + filename
    data = {"filters": filters, "params": params}

    r = session.post(uri, headers = {"Accept": accept, "Content-Type": contenttype}, json = data)

    if r.status_code != 200:
        print("Failed to get data for URI: '%s', data: %s" % (uri, str(data)))

    return r

def do_logout():
    r = session.get(base_uri + "logout", data = {}, verify = False)
    if r.status_code != 200:
        raise Exception("Logout failed")

#==========================================
# main
#==========================================

if __name__ == "__main__":

    print("Login ...")
    do_login()
    print("Login DONE")

    print("Call ...")
    filename = "data/punctuality/transporter"
    filters = {"startDate": "2024-08-01", "endDate": "2024-08-31" }  # A MODIFIER (mettre les dates de début et de fin du mois voulu) !!!
    params = {}
    accept = "text/csv"
    contenttype = "application/json"
    response = do_call(filename, filters, params, accept, contenttype)
    print("Call DONE")

    print("Save response to file ...")
    file = open("punctuality_2024-08.csv", "wb")
    file.write(response.content)
    file.close()
    print("Save response to file DONE")

    print("Logout ...")
    do_logout()
    print("Logout DONE")

