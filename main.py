# coding: utf-8

#thanks
#原案：twitter:3hiragana_bot様
#ひらがなのランダム生成:https://qiita.com/sora410/items/aad7e17c8c9c35a94f45 qiita:@sora410様
###
import random
import tweepy

a = random.randint(ord('あ'),ord('ん'))
b = random.randint(ord('あ'),ord('ん'))
c = random.randint(ord('あ'),ord('ん'))
d = random.randint(ord('あ'),ord('ん'))
text = chr(a) + chr(b) + chr(c) + chr(d)
print(text)