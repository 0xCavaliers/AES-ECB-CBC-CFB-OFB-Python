# AES-ECB-CBC-CFB-OFB-Python
# 川大密码学课程项目AES加密算法python实现

本项目可以直接在Colab或Jupyter Notebook上运行
## 1.进行以下命令操作前先安装库
!pip install pycryptodome

## 2. 如果要具体运行某种加密方法，则可以采取以下指令（以ECB模式为例）：
!python main.py -p AES_plain.txt -k AES_key.txt -v AES_iv.txt -m ECB -c AES_Cipher.txt

## 3. 如果要测速，直接运行以下代码：
!python test.py

