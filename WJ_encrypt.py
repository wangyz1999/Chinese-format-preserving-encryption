import pyffx
import thulac
import os

class WJE:
    def __init__(self):
        self.str = None
        self.digit = "0123456789"
        self.lower = "abcdefghijklmnopqrstuvwxyz"
        self.upper = self.lower.upper()
        self.com_per = ",."
        self.que_exc = "?!"
        self.sem_col = ";:"
        self.math = "+-*/="
        self.model = thulac.thulac()
        self.pos_set = dict()
        self.pos_list = dict()
        self.get_pos_dict()


    def get_pos_dict(self):
        file_names = os.listdir('data_pos\\sets')
        for fn in file_names:
            pos = fn[:fn.index('_')]
            length = fn[fn.index('_')+1:fn.index('.')]
            if pos in self.pos_set:
                self.pos_set[pos][length] = eval(open('data_pos\\sets\\' + fn, encoding='utf-8').read())
            else:
                self.pos_set[pos] = {length: eval(open('data_pos\\sets\\' + fn, encoding='utf-8').read())}
        file_names = os.listdir('data_pos\\lists')
        for fn in file_names:
            pos = fn[:fn.index('_')]
            length = fn[fn.index('_')+1:fn.index('.')]
            if pos in self.pos_list:
                self.pos_list[pos][length] = eval(open('data_pos\\lists\\' + fn, encoding='utf-8').read())
            else:
                self.pos_list[pos] = {length: eval(open('data_pos\\lists\\' + fn, encoding='utf-8').read())}

    def break_parts(self, message):
        return self.model.cut(message), self.model.cut(message, text=True)

    def get_encrypter(self, pos, length, key):
        alpha = self.pos_list[pos][length]
        e = pyffx.Sequence(bytearray(key.encode()), alphabet=alpha, length=1)
        return e

    def append_dict(self, parts):
        # print(parts)
        for msg, pos in parts:
            length = str(len(msg))
            if length not in self.pos_set[pos]:
                self.pos_set[pos][length] = {msg}
                self.pos_list[pos][length] = [msg]
            elif msg not in self.pos_set[pos][length]:
                self.pos_set[pos][length].add(msg)
                self.pos_list[pos][length].append(msg)

    def encrypt(self, message, key="wj"):
        parts, parts_text = self.break_parts(message)
        # print(parts)
        self.append_dict(parts)
        enc_msg = ""
        for msg, pos in parts:
            e = self.get_encrypter(pos, str(len(msg)), key)
            enc_msg += e.encrypt([msg])[0]
        return enc_msg, parts_text

    def decrypt(self, message, key="wj"):
        parts, parts_text = self.break_parts(message)
        # print(parts)
        self.append_dict(parts)
        dec_msg = ""
        for msg, pos in parts:
            e = self.get_encrypter(pos, str(len(msg)), key)
            dec_msg += e.decrypt([msg])[0]
        return dec_msg, parts_text

if __name__ == "__main__":
    wje = WJE()
    # print(wje.pos_set)
    # print(wje.pos_dic['u'])

    for key in list("abcdefghijklmnopqrstuvwxyz"):
        try:
            print("\n")
            msg = "程序员头发太短"
            enc, enc_text = wje.encrypt(msg, key=key)
            dec, dec_text = wje.decrypt(enc, key=key)
            print("原话:", msg)
            print("加密:", enc)
            print("解密:", dec)
            print("原话分词:", enc_text)
            print("加密分词:", dec_text)
        except:
            pass