#!/bin/python

import sys

def lonelyinteger(a):
    if len(a) < 2:
	return a[0]
    else:
	xor = 0
	for i in range(0,len(a)):
		xor ^= a[i]
		
	return xor

	   


n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
result = lonelyinteger(a)
print(result)
