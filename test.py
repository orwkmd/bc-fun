import ecdsa
import hashlib
import logging
import struct

def split(n):
    print n/2, n/2
    return '{0:x},{1:x} '.format(n/2, n/2)
l = [100, 50, 6]
print ''.join(map(split, l))