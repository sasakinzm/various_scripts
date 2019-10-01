#!/bin/bash python

#nw_address で指定したセグメントのIPアドレスを列挙する
# 変数:
#   address : ネットワークアドレス
#   n : サブネットマスク長
#
# サンプル:
# input:
#   $ python gen_ip_address_list.py 192.168.100.64 28
# output:
#   192.168.100.64
#   192.168.100.65
#   192.168.100.66
#   192.168.100.67
#   192.168.100.68
#   192.168.100.69
#   192.168.100.70
#   192.168.100.71
#   192.168.100.72
#   192.168.100.73
#   192.168.100.74
#   192.168.100.75
#   192.168.100.76
#   192.168.100.77
#   192.168.100.78
#   192.168.100.79


def address(nw_address, n):
    first_octet, second_octet, third_octet, fourth_octet = map(int, nw_address.split("."))
    nw_address_bin = bin(first_octet)[2:].zfill(8) + bin(second_octet)[2:].zfill(8) + bin(third_octet)[2:].zfill(8) + bin(fourth_octet)[2:].zfill(8)
    nw_address_dec = int(nw_address_bin, 2)
    host_addr_bitlength = 32 - int(n)
    for i in range(2**host_addr_bitlength):
        hostaddr_dec = nw_address_dec + i
        hostaddr_bin = bin(hostaddr_dec)[2:].zfill(32)
        hostaddr = str(int(hostaddr_bin[:8], 2)) + "." + str(int(hostaddr_bin[8:16], 2)) + "." + str(int(hostaddr_bin[16:24], 2)) + "." + str(int(hostaddr_bin[24:32], 2))
        print(hostaddr)

if __name__ == "__main__":
    import sys
    nw_address = sys.argv[1]
    n = sys.argv[2]
    address(nw_address, n)
