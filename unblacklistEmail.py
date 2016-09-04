import json
import requests
import sys
api_key=""
domain="broenink.email"

def getRecordId(value):
    resp = requests.get('https://api.digitalocean.com/v2/domains/'+domain+'/records', headers={"Authorization":"Bearer "+api_key})
    data = json.loads(resp.text)
    for record in data['domain_records']:
        if record['type'] == 'CNAME':
            print "CNAME: "+record['name'] #show list
            if record['name'] == value:
                return record['id']
    return -1

def removeRecord(id):
    resp = requests.delete('https://api.digitalocean.com/v2/domains/'+domain+'/records/'+str(id), headers={"Authorization":"Bearer "+api_key})
    return resp

def main():
    id = getRecordId(sys.argv[1])
    if id != -1:
        removal = removeRecord(id)
        if removal.status_code == 204:
            print "Record removed!"
        else:
            print "Removal failed."

if __name__ == "__main__":
    main()


