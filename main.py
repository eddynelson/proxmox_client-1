import requests
import json


class ProxmoxClient():
    # Init config
    def __init__(self, config):
        self._base_url = config['base_url']
        self._verify_ssl = config['verify_ssl']
        self._username = config['username']
        self._password = config['password']

        # security
        self._ticket = None
        self._token = None
        self._cookies = {}

        self.api_url = 'https://'+self._base_url+':8006/api2/json'

        self._get_ticket()

    def _get_ticket(self):
        res = requests.post(
          self.api_url + '/access/ticket', 
          verify = self._verify_ssl,
          data = [('username', self._username), ('password', self._password)]
        )

        res.raise_for_status()

        data = res.json()['data']
        self._ticket = data['ticket']
        self._token = data['CSRFPreventionToken']

        self._cookies = { 'PVEAuthCookie': self._ticket }

    # Cluster
    def get_cluster_tasks(self):
        params = (
          self.api_url + '/cluster/tasks',
          verify = False,
          cookies = self._cookies
        )

        res = requests.get(params)

        res.raise_for_status()

        return res.json()['data']

    def get_cluster_status(self):
        params = (
          self.api_url + '/cluster/status',
          verify = False,
          cookies = self._cookies
        )

        res = requests.get(params)

        res.raise_for_status()

        return res.json()['data']

    def get_cluster_resources(self):
        params = (
          self.api_url + '/cluster/resources',
          verify = False,
          cookies=self._cookies
        )

        res = requests.get(params)

        res.raise_for_status()

        return res.json()['data']
    
    def get_cluster_nextid(self):
        params = (
          self.api_url + '/cluster/nextid',
          verify = False,
          cookies = self._cookies
        )

        res = requests.get(params)

        res.raise_for_status()

        return res.json()['data']

    def get_cluster_logs(self):
        params = (
          self.api_url + '/cluster/log',
          verify = False,
          cookies = self._cookies
        )

        res = requests.get(params)

        res.raise_for_status()

        return res.json()['data']

    def get_cluster_replications(self):
        params = (
          self.api_url + '/cluster/replication',
          verify=False,
          cookies=self._cookies
        ) 

        res = requests.get(params)

        res.raise_for_status()

        return res.json()['data']

    def update_cluster_options(self, data):
        params = (
          self.api_url + '/cluster/options',
          verify=False,
          cookies=self._cookies,
          data=data,
          headers={ 'CSRFPreventionToken': self._token }
        )

        res = requests.put(params)

        res.raise_for_status()

        if res.status_code == 200:
            return { "message": 'Success!!' }

    # Without revision
    def create_cluster_replication(self, data):
        params = (
          self.api_url + '/cluster/replication',
          verify=False,
          cookies=self._cookies,
          data=data,
          headers={ 'CSRFPreventionToken': self._token }
        )

        res = requests.put(params)

        res.raise_for_status()

        return { "message": 'Success!!' }

    #Pools
    def create_pools(self, data):
        params = (
          self.api_url + '/pools',
          verify=False,
          cookies=self._cookies,
          data=data,
          headers={ 'CSRFPreventionToken': self._token }
        )

        res = requests.post(params)

        res.raise_for_status()

        return { "message": 'Success!!' }

# Test

config = {
  "base_url": "192.168.1.21", 
  "verify_ssl": False, 
  "password": "010203", 
  "username": "root@pam"
}

client = ProxmoxClient(config)

result = client.create_pools(data={ "poolid": "anyid", "comment": "Any comment"  })
print(result)
