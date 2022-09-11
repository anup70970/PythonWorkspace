from gettext import find
import re

content = 'can you buy me some coffee and buyer to me buying and buyreres if yes can you please bring my gogle from  table'
word = 'buy\w*'

def find_word(word,str1):
    content = re.findall(word,str1)
    print(content)

find_word(word,content)
def split_content(word, str1):
    content = re.split(word, str1)
    print(content)
# split_content(word,content)