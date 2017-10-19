#!/usr/bin/env python
import urllib3
import urllib
import hashlib
import hmac
import base64

def create_url(host, command, apikey, secretkey):
    baseurl='http://' + host + ':8080/client/api?'

    command_list = command.split('&')
    command_dict = {}
    for cmd in command_list:
        command_dict[cmd.split('=')[0]] = cmd.split('=')[1]

    request={}
    request['response'] ='json'
    request['apikey'] = apikey
    request.update(command_dict)
    request_str='&'.join(['='.join([k,urllib.parse.quote_plus(request[k])]) for k in request.keys()])

    secretkey = secretkey.encode('utf-8')
    sig_str='&'.join(['='.join([k.lower(),urllib.parse.quote_plus(request[k].lower().replace('+','%20'))])for k in sorted(request.keys())]).encode('utf-8')
    sig=hmac.new(secretkey,sig_str,hashlib.sha1)
    sig=hmac.new(secretkey,sig_str,hashlib.sha1).digest()
    sig=base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest())
    sig=base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip()
    sig=urllib.parse.quote_plus(base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip())
    req=baseurl+request_str+'&signature='+sig
    print(req)

host = input("host :")
command = input("command: ")
apikey = input("apikey: ")
secretkey = input("secretkey: ")
create_url(host, command, apikey, secretkey)
