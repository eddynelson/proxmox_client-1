# Proxmox-client

This is a proxmox client for manage proxmox through python methods and command line interface.

## Intallation for use as python methods

* ### Clone repository
 ``` bash
 $ git clone https://github.com/akevinieron/proxmox_client.git
 ```
* ### Move (your-clone-dir)/proxmox_client/main.py to (your-project-dir)/proxmoxclient
``` bash
$ mv (your-clone-dir)/proxmox_client/main.py (your-project-dir)/proxmoxclient
```
## Installation for use as CLI

# TODO

## How use in python

``` python
from proxmoxclient.main import ProxmoxClient

config = {
  "base_url": "your_host",
  "verify_ssl": False,
  "password": "your_password",
  "username": "your_username"
}

pxpx = ProxmoxClient(config)

# start use your method
```

## How use in CLI

# TODO


### Cluster methods

Cluster Management in proxmox-client

check <https://pve.proxmox.com/pve-docs/api-viewer/>

``` python

pxpx.get_cluster_tasks() # return list of tasks

pxpx.get_cluster_status() # return list of status

pxpx.get_cluster_resources() # return list of resources

pxpx.get_cluster_nextid() # return intenger

pxpx.get_cluster_logs() # return list of logs

pxpx.get_cluster_replications() # return list of replications

pxpx.update_cluster_options() # update cluster options

```