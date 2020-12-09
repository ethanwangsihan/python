import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
key_list = ["abcde",
            "fghik",
            "lmnop",
            "qrstu",
            "vwxyz"]


def caesar_e(plaintext, shift):
    ciphertext = ""
    for c in plaintext:
        if c.islower():
            t = (ord(c) - ord("a") + shift) % 26 + ord("a")
        else:
            t = (ord(c) - ord("A") + shift) % 26 + ord("A")
        ciphertext += chr(t)
    return ciphertext


def caesar_d(ciphertext, shift):
    plaintext = ""
    for c in ciphertext:
        if c.islower():
            t = (ord(c) - ord("a") - shift) % 26 + ord("a")
        else:
            t = (ord(c) - ord("A") - shift) % 26 + ord("A")
        plaintext += chr(t)
    return plaintext


def reverse_e(plaintext):
    ciphertext = ""
    key = alphabet[::-1]
    for c in plaintext:
        i = alphabet.index(c)
        ciphertext += key[i]
    return ciphertext


def reverse_d(ciphertext):
    plaintext = ""
    key = alphabet[::-1]
    for c in ciphertext:
        i = key.index(c)
        plaintext += alphabet[i]
    return plaintext


def rail_fence_e(plaintext):
    ciphertext = plaintext[::2] + plaintext[1::2]
    return ciphertext


def rail_fence_d(ciphertext):
    plaintext = ""
    length = int(len(ciphertext) / 2 + 0.5)
    r1 = list(ciphertext[:length])
    r2 = list(ciphertext[length:])
    while r1:
        plaintext += r1.pop(0)
        if r2:
            plaintext += r2.pop(0)
    return plaintext


def sparta_e(plaintext, key):
    ciphertext = ""
    for c in plaintext:
        ciphertext += c
        for i in range(key):
            ciphertext += random.choice(alphabet)
    return ciphertext


def sparta_d(ciphertext, key):
    plaintext = ciphertext[0::key + 1]
    return plaintext


def chess_e(plaintext):
    ciphertext = ""
    for c in plaintext:
        if c == "j":
            c = "i"
        for k in key_list:
            if c in k:
                i = key_list.index(k) + 1
                j = k.index(c) + 1
                ciphertext += str(i) + str(j)
    return ciphertext


def chess_d(ciphertext):
    plaintext = ""
    ciphertext_list = list(ciphertext)
    while ciphertext_list:
        a = int(ciphertext_list.pop(0))
        b = int(ciphertext_list.pop(0))
        plaintext += key_list[a - 1][b - 1]
    return plaintext


def main():
    plaintext = input("请输入要加密的明文: \n")
    
    while True:
        choice = input('''请选择加密方法:
                    1. 凯撒加密
                    2. 逆序加密
                    3. 栅栏加密
                    4. 斯巴达加密
                    5. 棋盘加密
                    6. 退出\n''')
        if choice == "1":
            shift = int(input("请输入加密的位移量: \n"))
            ct = caesar_e(plaintext, shift)
            pt = caesar_d(ct, shift)
        elif choice == "2":
            ct = reverse_e(plaintext)
            pt = reverse_d(ct)
        elif choice == "3":
            ct = rail_fence_e(plaintext)
            pt = rail_fence_d(ct)
        elif choice == "4":
            n = int(input("请输入混淆字母的数量: \n"))
            ct = sparta_e(plaintext, n)
            pt = sparta_d(ct, n)
        elif choice == "5":
            ct = chess_e(plaintext)
            pt = chess_d(ct)
        elif choice == "6":
            break
        else:
            print("输入错误，请重新输入!\n")
            continue
        print("加密后的密文是: %s" % ct)
        print("解密后的明文是: %s" % pt)


if __name__ == '__main__':
    main()
