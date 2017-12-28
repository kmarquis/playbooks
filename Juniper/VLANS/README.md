# Switch Port & VLAN Generation

This Playbook will generate new VLANs (with or without Routed Interface), Apply any necassary ACLs and QoS Filter to switchports

The logical behind this playbook: 

If an interface is defined as TRUNK port, the VLANs that have been defined will generate config that will *ONLY* add new VLANS.

If an interface is defined as an ACCESS port, the generated config will delete the old switchport config and generate new defined configuration


To Run this playbook, please use the command:
```
ansible-playbook vlan_playbook.yaml
```

