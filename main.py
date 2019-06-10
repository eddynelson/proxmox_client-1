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