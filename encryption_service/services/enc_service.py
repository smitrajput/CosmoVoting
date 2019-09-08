from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os
import json
import uuid
from utils.enc_utils import EncUtils


class EncService(object):

    @classmethod
    def generate_key(cls):

        private_key = EncUtils.get_rsa_key()
        private_key_obj = EncUtils.import_key(private_key)
        public_key= EncUtils.export_key(private_key_obj.publickey())
        
        return {
            "private_key": private_key,
            "public_key":public_key
        }

    @classmethod
    def encrypt(cls, request: dict):

        plain_text_data = request["plain_text_data"]
        public_key = request["public_key"]
        public_key = EncUtils.import_key(public_key)
        print ("type of message : ", type(bytes(plain_text_data, 'utf8')))
        ciphertext = EncUtils.long_encrypt(bytes(plain_text_data, 'utf8'), public_key)
        encoded_ciphertext = EncUtils.encode(ciphertext)

        return {
            "encoded_ciphertext": str(encoded_ciphertext, 'utf8')
        }

        
    @classmethod
    def decrypt(cls, request: dict):

        encoded_ciphertext = request["encoded_ciphertext"]
        private_key = request["private_key"]
        private_key = EncUtils.import_key(private_key)
        ciphertext = EncUtils.decode( bytes(encoded_ciphertext, 'utf8'))
        plain_text_data = EncUtils.long_decrypt(ciphertext, private_key)

        return {
            "plain_text_data": str(plain_text_data, 'utf8')
        }
   