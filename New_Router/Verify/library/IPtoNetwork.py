#!/usr/bin/python
from ansible.module_utils.basic import *

def DectoBin(n):
  test='{:08b}'.format(n)
  return test

def BintoDec(n):
  test=str(int(n,2))
  return test

def ArraytoString(s):
  str = ""
  for i in s:
    str += i
  return str


def Cal(str,str2):
  ip_split = str.split('.')
  mask_split = str2.split('.')
  bin_ip = [0] * 4
  bin_mask = [0] * 4
  bin_net = [[0] * 8 for i in range(4)]
  net_split = [0] * 4
  for i in range(4):
    bin_ip[i] = DectoBin(int(ip_split[i]))
    bin_mask[i] = DectoBin(int(mask_split[i]))
    for j in range(8):
      bin_net[i][j] = AND(int(bin_ip[i][j]),int(bin_mask[i][j]))
    net_split[i] = BintoDec(ArraytoString(bin_net[i]))
  
  return ".".join(net_split)

def AND(a,b):
  if a == 1 and b == 1:
     return "1"
  else:
     return "0"

if __name__ == '__main__':
    fields = {
          "ip": {"required": True, "type": "str"},
          "mask": {"required": True, "type": "str"},   
         }
    
    module = AnsibleModule(argument_spec=fields)
    ip = module.params['ip']
    mask = module.params['mask']
    result = Cal(ip,mask)  
    module.exit_json(msg=result)

