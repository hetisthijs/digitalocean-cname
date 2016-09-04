import json
import requests
import sys
api_key=""
domain="broenink.email"

def createRecord(value):
    resp = requests.post('https://api.digitalocean.com/v2/domains/'+domain+'/records', data={"type":"CNAME","name":value,"data":"google.com.","priority":"null","port":"null","weight":"null"}, headers={"Authorization":"Bearer "+api_key})
    return resp

def main():
    creation = createRecord(sys.argv[1])
    if creation.status_code == 200:
        print "Record added!"
    else:
        print "Adding failed."

if __name__ == "__main__":
    main()


