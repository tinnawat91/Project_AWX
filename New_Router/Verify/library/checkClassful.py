#!/usr/bin/python
from ansible.module_utils.basic import *

def Cal(str):
  ip_split = str.split('.')
  if int(ip_split[0]) < 127 :
    return "255.0.0.0"
  elif int(ip_split[0]) < 191 :
    return "255.255.0.0"
  else :
    return "255.255.255.0"

if __name__ == '__main__':
    fields = {
          "ip": {"required": True, "type": "str"},
         }
    module = AnsibleModule(argument_spec=fields)
    ip = module.params['ip']
    result = Cal(ip) 
    module.exit_json(msg=result)

