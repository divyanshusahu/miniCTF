from base64 import b64encode as be
from secret import msg, KEY

#msg and KEY are meaningful english sentences in l33t
msg2 = msg.replace('_','')
KEY = KEY.replace('_','')

assert  (len(KEY)==7) and KEY.isalnum() and msg2.isalnum()
assert 'n00bCTF' in msg2

def XOR(A, B):
	return ''.join(chr(ord(A[i])^ord(B[i%len(B)])) for i in range(len(A)))

def encryption(msg, key):
	return be(XOR(msg, KEY))

def print_flag(msg):
	print 'CTF{%s}' % msg

if __name__ == '__main__':
	print encryption(msg2, KEY)					#DRcGGQBfGw1QEA4XBUURCA0MDQdGBlFTCTo7MxwJUhgAXBQa
	#Decrypt msg2 to get the flag
	print_flag(msg2)
	
