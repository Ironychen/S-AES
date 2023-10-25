import binascii
import numpy as np
import aes128
import test
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


def spl_bin(input):
        cip = []
        for i in range (len(input)):
            cip.append(int(input[i]))
        return cip

def spl_bin1(input):
      cip = []
      input = str(input).split(',')
      for i in range (len(input)):
            cip.append(int(input[i]))
      print (cip)
      return cip


def choose():
    def change1():
        root0.destroy()
        one()
    def change2():
        root0.destroy()
        two()
    def change3():
        root0.destroy()
        three_1()
    def change4():
        root0.destroy()
        four()

    # 创建主窗口
    root0 = tk.Tk()
    root0.title('S-AES下的加解密系统')

    # 获取屏幕宽度和高度
    screen_width = root0.winfo_screenwidth()
    screen_height = root0.winfo_screenheight()

    # 计算窗口左上角坐标使其居中
    x = (screen_width - 400) // 2
    y = (screen_height - 600) // 2

    # 设置窗口大小和位置
    root0.geometry('400x600+{}+{}'.format(x, y))

    # 设置主窗口背景颜色
    root0.configure(bg='blue')

    # 创建一个Frame来容纳按钮，并使其在窗口中垂直居中
    frame = tk.Frame(root0)
    frame.pack(expand=True, fill=tk.BOTH)
    # 添加背景图片
    background_image = Image.open("background.jpg")  # 替换成你的背景图片文件路径
    background_image = background_image.resize((400, 600), Image.ANTIALIAS)  # 调整大小
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(frame, image=background_photo)
    background_label.place(relwidth=1, relheight=1)
    # 创建并设置标签的外观
    label = tk.Label(frame, text='请选择你要使用的功能', bg='lightblue', font=('宋体', 14))
    label.pack(fill=tk.X, pady=10)

    # 创建并设置按钮的外观
    btn01 = tk.Button(frame, text="二进制加密", command=change1, font=('宋体', 12), width=15, height=2)
    btn01.pack(pady=30, padx=5, anchor='center')

    btn02 = tk.Button(frame, text="字符加密", command=change2, font=('宋体', 12), width=15, height=2)
    btn02.pack(pady=30, padx=5, anchor='center')

    btn03 = tk.Button(frame, text="多重加密", command=change3, font=('宋体', 12), width=15, height=2)
    btn03.pack(pady=30, padx=5, anchor='center')

    btn04 = tk.Button(frame, text="CBC加密", command=change4, font=('宋体', 12), width=15, height=2)
    btn04.pack(pady=30, padx=5, anchor='center')


    root0.mainloop()

def one():
    def encrypt():
        # k = [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        k = spl_bin(str(entry.get()))
        # pla = [0, 0, 0, 0]
        pla = spl_bin1(str(en1.get()))
        
        crypted_part = aes128.encrypt(pla, k)
        print(crypted_part)
        messagebox.showinfo("密文",crypted_part)

    def solve():
        k = spl_bin(str(entry.get()))
        crypted_part = spl_bin1(str(en2.get()))
        d = aes128.decrypt(crypted_part, k)
        print(d)
        messagebox.showinfo("明文",d)

    def back():
        root1.destroy()
        choose()

     # 创建主窗口
    root1 = tk.Tk()
    root1.title('二进制编码')

    # 获取屏幕宽度和高度
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()

    # 计算窗口左上角坐标使其居中
    x = (screen_width - 400) // 2
    y = (screen_height - 600) // 2

    # 设置窗口大小和位置
    root1.geometry('400x600+{}+{}'.format(x, y))

    # 添加背景图片
    background_image = Image.open("background.jpg")  # 替换成你的背景图片文件路径
    background_image = background_image.resize((400, 600), Image.ANTIALIAS)  # 调整大小
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root1, image=background_photo)
    background_label.place(relwidth=1, relheight=1)

    # 创建文本变量
    v1 = tk.StringVar()

    # 创建输入框
    # 创建文本变量
    v1 = tk.StringVar()
    lab00 = tk.Label(root1, text='密钥', bg='lightblue', font=('宋体', 12))
    lab00.pack(pady=20)
    # 创建输入框并设置字体和大小
    entry = tk.Entry(root1, textvariable=v1, font=('宋体', 12), width=40)
    v1.set("0010110101010101")
    entry.pack(pady=10)

    # 创建标签并设置字体、大小和背景颜色
    lab01 = tk.Label(root1, text='请输入明文', bg='lightblue', font=('宋体', 12))
    lab01.pack(pady=30)

    # 创建明文输入框并设置字体和大小
    en1 = tk.Entry(root1, font=('宋体', 12), width=40)
    en1.pack(pady=5)

    # 创建加密按钮，设置字体、大小和背景颜色
    button1 = tk.Button(root1, text="加密", command=encrypt, font=('宋体', 12), width=15, height=2)
    button1.pack(pady=10)

    # 创建标签并设置字体、大小和背景颜色
    lab02 = tk.Label(root1, text='请输入密文', bg='lightblue', font=('宋体', 12))
    lab02.pack(pady=30)

    # 创建密文输入框并设置字体和大小
    en2 = tk.Entry(root1, font=('宋体', 12), width=40)
    en2.pack(pady=5)

    # 创建解密按钮，设置字体、大小和背景颜色
    button2 = tk.Button(root1, text="解密", command=solve, font=('宋体', 12), width=15, height=2)
    button2.pack(pady=12)

    # 创建返回按钮，设置字体、大小和背景颜色
    button3 = tk.Button(root1, text="返回", command=back, font=('宋体', 12), width=15, height=1)
    button3.pack(pady=8)


    root1.mainloop()

def two():
    def back():
        root2.destroy()
        choose()
    
    def encrypt():
        k = spl_bin(str(entry1.get()))
        pla = test.spl(str(en3.get()))
        print(pla)
        temp = []
        crypted_data = []
        for byte in pla:
            temp.append(test.binary_array_to_int(byte[:4]))
            temp.append(test.binary_array_to_int(byte[4:]))
            if len(temp) == 4:
                crypted_part = aes128.encrypt(temp, k)
                crypted_data.extend(crypted_part)
                del temp[:]
        else:
            # padding v1
            # crypted_data.extend(temp)
            # padding v2
            if 0 < len(temp) < 4:
                empty_spaces = 4 - len(temp)
                for i in range(empty_spaces - 1):
                    temp.append(0)
                    temp.append(1)
                    crypted_part = aes128.decrypt(temp, k)
                    crypted_data.extend(crypted_part)

        print(crypted_data)
        messagebox.showinfo("明文",crypted_data)


    def solve():
        k = spl_bin(str(entry1.get()))
        crypted_data = spl_bin1(str(en4.get()))
        decrypted_data = []
        temp = []
        for byte in crypted_data:
            temp.append(byte)
            if len(temp) == 4:
                decrypted_part = aes128.decrypt(temp, k)
                decrypted_data.extend(decrypted_part)
                del temp[:]
        else:
            if 0 < len(temp) < 4:
                empty_spaces = 4 - len(temp)
                for i in range(empty_spaces - 1):
                    temp.append(0)
                temp.append(1)
                decrypted_part = aes128.encrypt(temp, k)
                decrypted_data.extend(decrypted_part)
        decrypted_str = ""
        for i in range(len(decrypted_data)):
            if i % 2 == 0:
                t = 16 * decrypted_data[i] + decrypted_data[i + 1]
                decrypted_str += chr(t)

        print(decrypted_str)
        messagebox.showinfo("明文",decrypted_str)


    root2 = tk.Tk()
    root2.title('二进制编码')

    # 获取屏幕宽度和高度
    screen_width = root2.winfo_screenwidth()
    screen_height = root2.winfo_screenheight()

    # 计算窗口左上角坐标使其居中
    x = (screen_width - 400) // 2
    y = (screen_height - 600) // 2

    # 设置窗口大小和位置
    root2.geometry('400x600+{}+{}'.format(x, y))

    # 添加背景图片
    background_image = Image.open("background.jpg")  # 替换成你的背景图片文件路径
    background_image = background_image.resize((400, 600), Image.ANTIALIAS)  # 调整大小
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root2, image=background_photo)
    background_label.place(relwidth=1, relheight=1)

    # 创建文本变量
    v1 = tk.StringVar()

    # 创建输入框
    # 创建文本变量
    v1 = tk.StringVar()
    lab00 = tk.Label(root2, text='密钥', bg='lightblue', font=('宋体', 12))
    lab00.pack(pady=20)
    # 创建输入框并设置字体和大小
    entry1 = tk.Entry(root2, textvariable=v1, font=('宋体', 12), width=40)
    v1.set("0010110101010101")
    entry1.pack(pady=10)

    # 创建标签并设置字体、大小和背景颜色
    lab01 = tk.Label(root2, text='请输入明文', bg='lightblue', font=('宋体', 12))
    lab01.pack(pady=30)

    # 创建明文输入框并设置字体和大小
    en3 = tk.Entry(root2, font=('宋体', 12), width=40)
    en3.pack(pady=5)

    # 创建加密按钮，设置字体、大小和背景颜色
    button1 = tk.Button(root2, text="加密", command=encrypt, font=('宋体', 12), width=15, height=2)
    button1.pack(pady=10)

    # 创建标签并设置字体、大小和背景颜色
    lab02 = tk.Label(root2, text='请输入密文', bg='lightblue', font=('宋体', 12))
    lab02.pack(pady=30)

    # 创建密文输入框并设置字体和大小
    en4 = tk.Entry(root2, font=('宋体', 12), width=40)
    en4.pack(pady=5)

    # 创建解密按钮，设置字体、大小和背景颜色
    button2 = tk.Button(root2, text="解密", command=solve, font=('宋体', 12), width=15, height=2)
    button2.pack(pady=10)

    # 创建返回按钮，设置字体、大小和背景颜色
    button3 = tk.Button(root2, text="返回", command=back, font=('宋体', 12), width=15, height=2)
    button3.pack(pady=10)

    root2.mainloop()

def three_1():
    def back():
        root31.destroy()
        choose()
    def change1():
        root31.destroy()
        three_2()
    def change2():
        root31.destroy()
        three_3()
    # 创建主窗口
    root31 = tk.Tk()
    root31.title('多重加密')

    # 获取屏幕宽度和高度
    screen_width = root31.winfo_screenwidth()
    screen_height = root31.winfo_screenheight()

    # 计算窗口左上角坐标使其居中
    x = (screen_width - 400) // 2
    y = (screen_height - 600) // 2

    # 设置窗口大小和位置
    root31.geometry('400x600+{}+{}'.format(x, y))

    # 设置主窗口背景颜色
    root31.configure(bg='blue')

    # 创建一个Frame来容纳按钮，并使其在窗口中垂直居中
    frame = tk.Frame(root31)
    frame.pack(expand=True, fill=tk.BOTH)
    # 添加背景图片
    background_image = Image.open("background.jpg")  # 替换成你的背景图片文件路径
    background_image = background_image.resize((400, 600), Image.ANTIALIAS)  # 调整大小
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(frame, image=background_photo)
    background_label.place(relwidth=1, relheight=1)
    # 创建并设置标签的外观
    label = tk.Label(frame, text='请选择你要使用的功能', bg='lightblue', font=('宋体', 14))
    label.pack(fill=tk.X, pady=10)

    # 创建并设置按钮的外观
    btn01 = tk.Button(frame, text="双重加密", command=change1, font=('宋体', 15), width=15, height=2)
    btn01.pack(pady=45, padx=5, anchor='center')

    btn02 = tk.Button(frame, text="三重加密", command=change2, font=('宋体', 15), width=15, height=2)
    btn02.pack(pady=45, padx=5, anchor='center')

    btn02 = tk.Button(frame, text="返回", command=back, font=('宋体', 12), width=8, height=1)
    btn02.pack(pady=60, padx=5, anchor='center')


    root31.mainloop()

# 双重加密窗口
def three_2():
    def back():
        root32.destroy()
        three_1()

    def encrypt():
        key1 = spl_bin(str(entry1.get()))
        key2 = spl_bin(str(entry2.get()))
        pla = spl_bin1(str(en1.get()))
        cip = aes128.encrypt(pla,key1)
        cip1 = aes128.decrypt(cip,key2)
        print(cip1)
        messagebox.showinfo("密文",cip1)

    def solve():
        key1 = spl_bin(str(entry1.get()))
        key2 = spl_bin(str(entry2.get()))
        cip = spl_bin1(str(en2.get()))
        dec = aes128.encrypt(cip,key2)
        dec1 = aes128.decrypt(dec,key1)
        print(dec1)
        messagebox.showinfo("明文",dec1)

    root32 = tk.Tk()
    root32.title('双重加解密')

    # 获取屏幕宽度和高度
    screen_width = root32.winfo_screenwidth()
    screen_height = root32.winfo_screenheight()

    # 计算窗口左上角坐标使其居中
    x = (screen_width - 400) // 2
    y = (screen_height - 600) // 2

    # 设置窗口大小和位置
    root32.geometry('400x600+{}+{}'.format(x, y))

    # 添加背景图片
    background_image = Image.open("background.jpg")  # 替换成你的背景图片文件路径
    background_image = background_image.resize((400, 600), Image.ANTIALIAS)  # 调整大小
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root32, image=background_photo)
    background_label.place(relwidth=1, relheight=1)

    # 创建文本变量
    v1 = tk.StringVar()

    # 创建输入框
    # 创建文本变量
    v1 = tk.StringVar()
    v2 = tk.StringVar()
    lab00 = tk.Label(root32, text='请分别输入两个密钥密钥', bg='lightblue', font=('宋体', 12))
    lab00.pack(pady=20)
    # 创建输入框并设置字体和大小
    entry1 = tk.Entry(root32, textvariable=v1, font=('宋体', 12), width=40)
    v1.set("0010110101010101")
    entry1.pack(pady=5)

    entry2 = tk.Entry(root32, textvariable=v2, font=('宋体', 12), width=40)
    v2.set("0000111100001111")
    entry2.pack(pady=2)

    # 创建标签并设置字体、大小和背景颜色
    lab01 = tk.Label(root32, text='请输入明文', bg='lightblue', font=('宋体', 12))
    lab01.pack(pady=30)

    # 创建明文输入框并设置字体和大小
    en1 = tk.Entry(root32, font=('宋体', 12), width=40)
    en1.pack(pady=5)

    # 创建加密按钮，设置字体、大小和背景颜色
    button1 = tk.Button(root32, text="加密", command=encrypt, font=('宋体', 12), width=15, height=2)
    button1.pack(pady=10)

    # 创建标签并设置字体、大小和背景颜色
    lab02 = tk.Label(root32, text='请输入密文', bg='lightblue', font=('宋体', 12))
    lab02.pack(pady=30)

    # 创建密文输入框并设置字体和大小
    en2 = tk.Entry(root32, font=('宋体', 12), width=40)
    en2.pack(pady=5)

    # 创建解密按钮，设置字体、大小和背景颜色
    button2 = tk.Button(root32, text="解密", command=solve, font=('宋体', 12), width=15, height=2)
    button2.pack(pady=12)

    # 创建返回按钮，设置字体、大小和背景颜色
    button3 = tk.Button(root32, text="返回", command=back, font=('宋体', 12), width=15, height=1)
    button3.pack(pady=5)


    root32.mainloop()

# 三重加密窗口
def three_3():
    def back():
        root33.destroy()
        three_1()

    def encrypt():
        key1 = spl_bin(str(entry1.get()))
        key2 = spl_bin(str(entry2.get()))
        pla = spl_bin1(str(en1.get()))
        cip = aes128.encrypt(pla,key1)
        cip = aes128.decrypt(cip,key2)
        cip = aes128.encrypt(cip,key1)
        print(cip)
        messagebox.showinfo("密文",cip)

    def solve():
        key1 = spl_bin(str(entry1.get()))
        key2 = spl_bin(str(entry2.get()))
        cip = spl_bin1(str(en2.get()))
        dec = aes128.decrypt(cip,key1)
        dec = aes128.encrypt(dec,key2)
        dec = aes128.decrypt(dec,key1)
        print(dec)
        messagebox.showinfo("明文",dec)

    root33 = tk.Tk()
    root33.title('三重加解密')

    # 获取屏幕宽度和高度
    screen_width = root33.winfo_screenwidth()
    screen_height = root33.winfo_screenheight()

    # 计算窗口左上角坐标使其居中
    x = (screen_width - 400) // 2
    y = (screen_height - 600) // 2

    # 设置窗口大小和位置
    root33.geometry('400x600+{}+{}'.format(x, y))

    # 添加背景图片
    background_image = Image.open("background.jpg")  # 替换成你的背景图片文件路径
    background_image = background_image.resize((400, 600), Image.ANTIALIAS)  # 调整大小
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root33, image=background_photo)
    background_label.place(relwidth=1, relheight=1)

    # 创建文本变量
    v1 = tk.StringVar()

    # 创建输入框
    # 创建文本变量
    v1 = tk.StringVar()
    v2 = tk.StringVar()
    lab00 = tk.Label(root33, text='请分别输入两个密钥密钥', bg='lightblue', font=('宋体', 12))
    lab00.pack(pady=20)
    # 创建输入框并设置字体和大小
    entry1 = tk.Entry(root33, textvariable=v1, font=('宋体', 12), width=40)
    v1.set("0010110101010101")
    entry1.pack(pady=5)

    entry2 = tk.Entry(root33, textvariable=v2, font=('宋体', 12), width=40)
    v2.set("0000111100001111")
    entry2.pack(pady=2)

    # 创建标签并设置字体、大小和背景颜色
    lab01 = tk.Label(root33, text='请输入明文', bg='lightblue', font=('宋体', 12))
    lab01.pack(pady=30)

    # 创建明文输入框并设置字体和大小
    en1 = tk.Entry(root33, font=('宋体', 12), width=40)
    en1.pack(pady=5)

    # 创建加密按钮，设置字体、大小和背景颜色
    button1 = tk.Button(root33, text="加密", command=encrypt, font=('宋体', 12), width=15, height=2)
    button1.pack(pady=10)

    # 创建标签并设置字体、大小和背景颜色
    lab02 = tk.Label(root33, text='请输入密文', bg='lightblue', font=('宋体', 12))
    lab02.pack(pady=30)

    # 创建密文输入框并设置字体和大小
    en2 = tk.Entry(root33, font=('宋体', 12), width=40)
    en2.pack(pady=5)

    # 创建解密按钮，设置字体、大小和背景颜色
    button2 = tk.Button(root33, text="解密", command=solve, font=('宋体', 12), width=15, height=2)
    button2.pack(pady=10)

    # 创建返回按钮，设置字体、大小和背景颜色
    button3 = tk.Button(root33, text="返回", command=back, font=('宋体', 12), width=15, height=2)
    button3.pack(pady=10)


    root33.mainloop()

def four():

    def back():
        root4.destroy()
        choose()

    def encrypt():
        key = spl_bin(str(entry.get()))
        IV = spl_bin1(str(entry2.get()))
        pla = test.spl(str(en1.get()))
        converted_list = []
        for i in range(0, len(pla), 2):
            if i + 1 < len(pla):
                combined_values = [
                    int(''.join(map(str, pla[i, :4])), 2),
                    int(''.join(map(str, pla[i, 4:])), 2),
                    int(''.join(map(str, pla[i + 1, :4])), 2),
                    int(''.join(map(str, pla[i + 1, 4:])), 2)
                ]
                converted_list.append(combined_values)
            else:
                combined_values = [
                    int(''.join(map(str, pla[i, :4])), 2),
                    int(''.join(map(str, pla[i, 4:])), 2),
                    0,
                    0
                ]
                converted_list.append(combined_values)
        # print(converted_list)

        ciphertext = encrypt_cbc(converted_list, key, IV)
        # print(ciphertext)
        encrypted_str = ""
        for i in range(len(ciphertext)):
            for j in range(len(ciphertext[0])):
                if j % 2 == 0:
                    t = 16 * ciphertext[i][j] + ciphertext[i][j + 1]
                    encrypted_str += chr(t)
        print(encrypted_str)
        messagebox.showinfo("密文",encrypted_str)



    def solve():
        key = spl_bin(str(entry.get()))
        IV = spl_bin1(str(entry2.get()))
        converted_list = []
        pla = test.spl(str(en1.get()))
        for i in range(0, len(pla), 2):
            if i + 1 < len(pla):
                combined_values = [
                    int(''.join(map(str, pla[i, :4])), 2),
                    int(''.join(map(str, pla[i, 4:])), 2),
                    int(''.join(map(str, pla[i + 1, :4])), 2),
                    int(''.join(map(str, pla[i + 1, 4:])), 2)
                ]
                converted_list.append(combined_values)
            else:
                combined_values = [
                    int(''.join(map(str, pla[i, :4])), 2),
                    int(''.join(map(str, pla[i, 4:])), 2),
                    0,
                    0
                ]
                converted_list.append(combined_values)
        # print(converted_list)
        ciphertext = encrypt_cbc(converted_list, key, IV)
        encrypted_str = ""
        for i in range(len(ciphertext)):
            for j in range(len(ciphertext[0])):
                if j % 2 == 0:
                    t = 16 * ciphertext[i][j] + ciphertext[i][j + 1]
                    encrypted_str += chr(t)

        platext = decrypt_cbc(ciphertext, key, IV)
        decrypted_str = ""
        for i in range(len(platext)):
            for j in range(len(platext[0])):
                if j % 2 == 0:
                    t = 16 * platext[i][j] + platext[i][j + 1]
                    decrypted_str += chr(t)
        print(decrypted_str)
        messagebox.showinfo("明文",decrypted_str)

    root4 = tk.Tk()
    root4.title('CBC加密')

    # 获取屏幕宽度和高度
    screen_width = root4.winfo_screenwidth()
    screen_height = root4.winfo_screenheight()

    # 计算窗口左上角坐标使其居中
    x = (screen_width - 400) // 2
    y = (screen_height - 600) // 2

    # 设置窗口大小和位置
    root4.geometry('400x600+{}+{}'.format(x, y))

    # 添加背景图片
    background_image = Image.open("background.jpg")  # 替换成你的背景图片文件路径
    background_image = background_image.resize((400, 600), Image.ANTIALIAS)  # 调整大小
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root4, image=background_photo)
    background_label.place(relwidth=1, relheight=1)

    # 创建文本变量
    v1 = tk.StringVar()

    # 创建输入框
    # 创建文本变量
    v1 = tk.StringVar()
    lab00 = tk.Label(root4, text='密钥', bg='lightblue', font=('宋体', 12))
    lab00.pack(pady=8)
    # 创建输入框并设置字体和大小
    entry = tk.Entry(root4, textvariable=v1, font=('宋体', 12), width=40)
    v1.set("0010110101010101")
    entry.pack(pady=8)

    v2 = tk.StringVar()
    lab000 = tk.Label(root4,text='请给定初始化向量',bg = 'lightblue',font=('宋体',12))
    lab000.pack(pady=8)
    entry2 = tk.Entry(root4, textvariable=v2, font=('宋体', 12), width=40)
    v2.set("5,6,7,8")
    entry2.pack(pady=8)

    # 创建标签并设置字体、大小和背景颜色
    lab01 = tk.Label(root4, text='请输入明文', bg='lightblue', font=('宋体', 12))
    lab01.pack(pady=20)

    # 创建明文输入框并设置字体和大小
    en1 = tk.Entry(root4, font=('宋体', 12), width=40)
    en1.pack(pady=7)

    # 创建加密按钮，设置字体、大小和背景颜色
    button1 = tk.Button(root4, text="加密", command=encrypt, font=('宋体', 12), width=15, height=2)
    button1.pack(pady=8)

    # 创建标签并设置字体、大小和背景颜色
    lab02 = tk.Label(root4, text='请输入密文', bg='lightblue', font=('宋体', 12))
    lab02.pack(pady=20)

    # 创建密文输入框并设置字体和大小
    en2 = tk.Entry(root4, font=('宋体', 12), width=40)
    en2.pack(pady=7)

    # 创建解密按钮，设置字体、大小和背景颜色
    button2 = tk.Button(root4, text="解密", command=solve, font=('宋体', 12), width=15, height=2)
    button2.pack(pady=12)

    # 创建返回按钮，设置字体、大小和背景颜色
    button3 = tk.Button(root4, text="返回", command=back, font=('宋体', 12), width=15, height=1)
    button3.pack(pady=8)

    root4.mainloop()


def encrypt_cbc(plain_text, key, iv):
    ciphertext = []
    previous_block = iv

    for block in plain_text:
        # CBC模式下，每个明文块先与前一个密文块异或
        block = [a ^ b for a, b in zip(block, previous_block)]
        # 然后使用密钥进行加密
        encrypted_block = aes128.encrypt(block, key)
        # 密文块添加到结果中
        ciphertext.append(encrypted_block)
        # 更新前一个密文块
        previous_block = encrypted_block

    return ciphertext


# 解密函数（CBC模式）
def decrypt_cbc(ciphertext, key, iv):
    plain_text = []
    previous_block = iv

    for block in ciphertext:
        # 使用密钥进行解密
        decrypted_block = aes128.decrypt(block, key)
        # 在CBC模式下，解密后的块再与前一个密文块异或
        plain_block = [a ^ b for a, b in zip(decrypted_block, previous_block)]
        # 明文块添加到结果中
        plain_text.append(plain_block)
        # 更新前一个密文块
        previous_block = block

    return plain_text

if __name__ == '__main__':
    choose()