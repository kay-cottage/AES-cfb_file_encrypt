from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex
from Crypto import Random
import base64


class AesEncryption(object):
    def __init__(self, key, mode=AES.MODE_CFB):
        self.key = self.check_key(key)
        # 密钥key长度必须为16,24或者32bytes的长度
        self.mode = mode
        self.iv = Random.new().read(AES.block_size)
        print(Random.new().read(AES.block_size))

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

if __name__ == '__main__':
    key = '1234567890123456'
    #data = open('2.png','rb').read()
    #data = 'abc,123你真帅'
    #image转base64

    with open("2 - 副本.png","rb") as f:
        base64_data = base64.b64encode(f.read())
  # base64.b64decode(base64data)
        #print(base64_data)
        data = base64_data
    #aes = AesEncryption(key)
   # e = aes.encrypt(data)  # 调用加密函数
    #d = aes.decrypt(e)  # 调用解密函数
    #print(type(e))
    with open("2 - 副本.png","w") as f:
        aes = AesEncryption(key)
        e = aes.encrypt(data)
        f.write(e)

             
    #print(d)
