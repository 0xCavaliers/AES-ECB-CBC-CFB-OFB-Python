from Crypto.Cipher import AES
import binascii

# 定义密钥和明文
hex_key = '57696C6C69616D5374616C6C696E6773'  # 示例密钥
hex_plain = '43727970746F67726170687920616E64204E6574776F726B5365637572697479'  # 32字节的示例明文
hex_iv = '5072656E7469636548616C6C496E632E'  # 示例初始化向量

# 解码为二进制数据
key = binascii.unhexlify(hex_key)
plaintext = binascii.unhexlify(hex_plain)
iv = binascii.unhexlify(hex_iv)

def aes_ecb_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)  # 不需要填充，因为32是16的倍数
    return binascii.hexlify(ciphertext).upper()

def aes_cbc_encrypt(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext)  # 不需要填充，因为32是16的倍数
    return binascii.hexlify(ciphertext).upper()

def aes_cfb_encrypt(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=8)  # 设置segment_size为8位
    ciphertext = cipher.encrypt(plaintext)
    return binascii.hexlify(ciphertext).upper()

def aes_ofb_encrypt(plaintext, key, original_iv):
    iv = original_iv[:]  # 创建IV的副本
    cipher = AES.new(key, AES.MODE_OFB, iv)
    ciphertext = cipher.encrypt(plaintext)
    return binascii.hexlify(ciphertext).upper()

# 加密并打印结果
ciphertext_ecb = aes_ecb_encrypt(plaintext, key)
print("ECB Ciphertext (hex):", ciphertext_ecb.decode())

ciphertext_cbc = aes_cbc_encrypt(plaintext, key, iv)
print("CBC Ciphertext (hex):", ciphertext_cbc.decode())

ciphertext_cfb = aes_cfb_encrypt(plaintext, key, iv)
print("CFB Ciphertext (hex):", ciphertext_cfb.decode())

ciphertext_ofb = aes_ofb_encrypt(plaintext, key, iv)
print("OFB Ciphertext (hex):", ciphertext_ofb.decode())
