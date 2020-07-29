#!/etc/zabbix/scripts/venv/bin/python
import requests
import json
from hurry.filesize import size
import sys

class Api:
  def __init__(self,baseUrl,user,token):
    self.url = 'https://'+user+':'+token+'@'+baseUrl+'/ocs/v2.php/apps/serverinfo/api/v1/info?format=json'
    
  def requesting(self):
    response = requests.get(self.url)
    result = response.text.encode('utf8')
    results = json.loads(result)
    return results
  
  def params(self,results,argument):
    for result in results:
      if argument == "version":
        version = results['ocs']['data']['nextcloud']['system']['version']
        print(version)
        exit()
      if argument == "freespace":
        freespace = results['ocs']['data']['nextcloud']['system']['freespace']
        print(freespace)
        exit()
      if argument == "num_users":
        num_users = results['ocs']['data']['nextcloud']['storage']['num_users']
        print(num_users)
        exit()
      if argument == "num_files":
        num_files = results['ocs']['data']['nextcloud']['storage']['num_files']
        print(num_files)
        exit()
      if argument == "num_storages_local":
        num_storages_local = results['ocs']['data']['nextcloud']['storage']['num_storages_local']
        print(num_storages_local)
        exit()
      if argument == "memory_limit":
        memory_limit = results['ocs']['data']['server']['php']['memory_limit']
        print(memory_limit)
        exit()
      if argument == "max_execution_time":
        max_execution_time = results['ocs']['data']['server']['php']['max_execution_time']
        print(max_execution_time)
        exit()
      if argument == "upload_max_filesize":
        upload_max_filesize = results['ocs']['data']['server']['php']['upload_max_filesize']
        print(upload_max_filesize)
        exit()
      if argument == "database_size":
        database_size = results['ocs']['data']['server']['database']['size']
        print(database_size)
        exit()
      if argument == "activeUsers":
        activeUsers = results['ocs']['data']['activeUsers']['last5minutes']
        print(activeUsers)
        exit()
        
def main(baseUrl,user,token,argument):
  api = Api(baseUrl,user,token)
  results = api.requesting()
  result = api.params(results,argument)

if __name__ == '__main__':
  baseUrl = sys.argv[1]
  user = sys.argv[2]
  token = sys.argv[3]
  argument = sys.argv[4]
  result = main(baseUrl,user,token,argument)
