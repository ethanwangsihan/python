while True:
    n = input("请输入（解码1🔓）（加密2🔐）(退出3🔚)：")
    if n == "1":
        # 设置
        alphabet = "abcdefghijklmnopqrstuvwxyz ,."
        key = "defghijklmnopqrstuvwxyzabc ,."

        # 输入
        cipher = input("请输入你的密文：")

        # 解密
        message = ""  # 空字符串
        for c in cipher:
            # 获取每一个字母在密钥中的索引
            i = key.index(c)
            # 将字母表中对应索引的字母拼起来
            message += alphabet[i]
        print("你的明文是：%s" % message)
    elif n == "2":
        # 设置
        alphabet = "abcdefghijklmnopqrstuvwxyz ,."
        key = "defghijklmnopqrstuvwxyzabc ,."

        # 输入
        message = input("请输入你的明文：")

        # 加密
        cipher = ""
        for m in message:
            # 获取每一个字母m在字母表中的索引
            i = alphabet.index(m)
            # 将密钥中对应索引i的字母拼起来
            cipher += key[i]
        print("你的密文是：%s" % cipher)  # 是message还是cipher
    else:
        break