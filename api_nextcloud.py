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
        return version
      
      if argument == "freespace":
        freespace = results['ocs']['data']['nextcloud']['system']['freespace']
        return freespace
      
      if argument == "num_users":
        num_users = results['ocs']['data']['nextcloud']['storage']['num_users']
        return num_users
      
      if argument == "num_files":
        num_files = results['ocs']['data']['nextcloud']['storage']['num_files']
        return num_files
      
      if argument == "num_storages_local":
        num_storages_local = results['ocs']['data']['nextcloud']['storage']['num_storages_local']
        return num_storages_local
      
      if argument == "memory_limit":
        memory_limit = results['ocs']['data']['server']['php']['memory_limit']
        return memory_limit
      
      if argument == "max_execution_time":
        max_execution_time = results['ocs']['data']['server']['php']['max_execution_time']
        return max_execution_time
      
      if argument == "upload_max_filesize":
        upload_max_filesize = results['ocs']['data']['server']['php']['upload_max_filesize']
        return upload_max_filesize
      
      if argument == "database_size":
        database_size = results['ocs']['data']['server']['database']['size']
        return database_size

      if argument == "activeUsers":
        activeUsers = results['ocs']['data']['activeUsers']['last5minutes']
        return activeUsers
      
def main(baseUrl,user,token,argument):
  api = Api(baseUrl,user,token)
  results = api.requesting()
  result = api.params(results,argument)
  return result

if __name__ == '__main__':
  baseUrl = sys.argv[1]
  user = sys.argv[2]
  token = sys.argv[3]
  argument = sys.argv[4]
  result = main(baseUrl,user,token,argument)
  print(result)
