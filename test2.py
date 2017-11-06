import ecdsa
import hashlib


sk_s = hashlib.sha256('hello world').digest()
sk = ecdsa.SigningKey.from_string(sk_s, curve=ecdsa.SECP256k1)
print sk.to_string()
rk = sk.get_verifying_key()
print rk.to_string()

m = 'O re ha ka mi da'
signature = sk.sign(m)
print rk.verify(signature, m)
print '\04\09'.encode('hex')
