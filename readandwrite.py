import argparse
import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def read_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def write_file(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data)

def encrypt_decrypt(args):
    key = read_file(args.key)
    plaintext = read_file(args.plain)
    iv = read_file(args.iv) if args.mode != 'ECB' else None

    if args.mode in ['CBC', 'CFB', 'OFB', 'ECB']:
        cipher = AES.new(key, getattr(AES, f"MODE_{args.mode}"), iv)
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
        write_file(args.cipher, ciphertext)
        print(f"加密完成，密文已保存到 {args.cipher}")
    else:
        print("不支持的加密模式")

def input_settings():
    parser = argparse.ArgumentParser(description="AES加密程序")
    parser.add_argument("-p", "--plain", type=str, help="指定明文文件的位置和名称", default="des_plain.txt")
    parser.add_argument("-k", "--key", type=str, help="指定密钥文件的位置和名称", default="des_key.txt")
    parser.add_argument("-v", "--iv", type=str, help="指定初始化向量文件的位置和名称（ECB模式除外）", default="des_iv.txt")
    parser.add_argument("-m", "--mode", type=str, help="指定加密的操作模式 (ECB, CBC, CFB, OFB)", default="ECB")
    parser.add_argument("-c", "--cipher", type=str, help="指定密文文件的位置和名称", default="des_cipher.txt")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = input_settings()
    encrypt_decrypt(args)
