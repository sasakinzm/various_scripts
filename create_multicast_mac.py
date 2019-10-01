#!/usr/bin/env python

#マルチキャストグループアドレスからマルチキャストMACアドレスを生成する
# 変数:
#   ipaddr : マルチキャストグループアドレス
#
# サンプル:
#   $ python create_multicast_mac.py 239.0.0.1
# output:
#   01:00:5e:00:00:01

import sys

def create_mac(ipaddr):
    mac1, mac2, mac3  = "01", "00", "5e"
    mac4 = bin(int(ipaddr.split(".")[1]))[2:]
    mac4 = mac4.zfill(8)[1:].zfill(7)
    mac4 = "0" + mac4
    mac4_1 = format(int(mac4[:4], 2), "x")
    mac4_2 = format(int(mac4[4:], 2), "x")
    mac4 = mac4_1 + mac4_2
    mac5 = hex(int(ipaddr.split(".")[2]))[2:].zfill(2)
    mac6 = hex(int(ipaddr.split(".")[3]))[2:].zfill(2)
    mac = mac1 + ":" + mac2 + ":" + mac3 + ":" + mac4 + ":" + mac5 + ":" + mac6
    return mac

if __name__ == '__main__':
    print(create_mac(sys.argv[1]))
