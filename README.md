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

Check this <https://pve.proxmox.com/pve-docs/api-viewer/>

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

``` python

pxpx.get_cluster_tasks() # return list of tasks

pxpx.get_cluster_status() # return list of status

pxpx.get_cluster_resources() # return list of resources

pxpx.get_cluster_nextid() # return intenger

pxpx.get_cluster_logs() # return list of logs

pxpx.get_cluster_replications() # return list of replications

pxpx.update_cluster_options() # update cluster options

```

### Nodes methods

Nodes management in proxmox-client

``` python

pxpx.get_all_ct(data={...}) # get all ct in the cluster

pxpx.get_ct(data={...}) # get specific ct in the cluster

pxpx.get_nextid() # get nextid

pxpx.get_config_ct(data={...}) # get ct configuration

pxpx.get_snapshots(data={...}) # get all snapshopt on the specific ct

pxpx.get_snapshot(data={...}) # get specific snapshot on the specific ct

pxpx.start_ct(data={...}) # start a ct

pxpx.stop_ct(data={...}) # stopa a ct

pxpx.clone_ct(data={...}) # clone specific ct

pxpx.create_snapshot(data={...}) # create a snapshot in the specific ct

pxpx.create_template(data={...}) # create a template in the specific ct

pxpx.update_config_ct(data={...}) # update ct configuration

pxpx.update_snapshot(data={...}) # update snapshot on a specifit ct

pxpx.delete_snapshot(data={...}) # delete snapshot on a specifit ct

pxpx.delete_ct(data={...}) # delete specific ct
```