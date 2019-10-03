# coding: utf-8
import random
import tweepy

a = random.randint(ord('あ'),ord('ん'))
b = random.randint(ord('あ'),ord('ん'))
c = random.randint(ord('あ'),ord('ん'))
d = random.randint(ord('あ'),ord('ん'))
text = chr(a) + chr(b) + chr(c) + chr(d)
print(text)