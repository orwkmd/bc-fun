import ecdsa
import base58
import hashlib
import random


class KeyUtils:

    @staticmethod
    def private_key_to_wif(key):
        """
        :param key: 256 bit private key.
        :return: Wallet Import Format private key.
        """
        return base58.b58encode_check(key)

    @staticmethod
    def private_key_to_public_key(key):
        """
        :param key: 256 bit private key.
        :return: public key, 512 bit ECDSA public key with prefix 0x04.
        """
        sk = ecdsa.SigningKey.from_string(key, curve=ecdsa.SECP256k1)
        return '\x04' + sk.verifying_key.to_string()

    @staticmethod
    def public_key_to_addr(key):
        """
        :param key: 520 bit public key.
        :return: transaction address.
        """
        ripemd160 = hashlib.new('ripemd160')
        ripemd160.update(hashlib.sha256(key).digest())
        return base58.b58encode_check(ripemd160.digest())

    @staticmethod
    def private_key_to_addr(key):
        return KeyUtil.public_key_to_addr(KeyUtil.private_key_to_public_key(key))


private_key = (''.join(['%x' % random.randrange(16) for x in range(0, 64)])).decode('hex')
print private_key.encode('hex')
public_key = KeyUtils.private_key_to_public_key(private_key)
print public_key.encode('hex')
