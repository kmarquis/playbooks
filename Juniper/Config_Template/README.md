# Configuration Template Generation

This Playbook will generate a base config for Juniper Switch that is using Enhanced Layer 2 Software CLI and will push the configuration to an IP reachable device

You will need the following packages installed on your ansible host:

* build-essential 
* libssl-dev 
* libffi-dev 
* python-dev 
* libxml2-dev 
* libxslt-dev 
* python-pip 

Once pip has been installed you will to pip install the following:

* junos-eznc 
* napalm 
* ansible 
* napalm-ansible
* Jinja2

To Run this playbook, please use the command from within the playbook directory:
```
ansible-playbook ex_playbook.yaml
```