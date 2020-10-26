import xml.dom.minidom 
import xml.etree.ElementTree as ET
from collections import Counter
import sys

def get( str ) :
    if str == '<title>':
        return 5
    if str == '<abstract>':
        return 3
    return 1

def normalize(str):
    str = str.lower()
    str = str.translate({
        ord(','): None,
        ord('.'): None,
        ord('?'): None,
        ord('!'): None,
    })
    return str
str = input()
stop_words = str.split(';')
str = input()
index_terms = str.split(';')
xml_data = sys.stdin.read()

xml_data = xml_data.replace("<", " <")
xml_data = xml_data.replace(">", "> ")
xml_data = xml_data.replace("\n", " \n ")
xml_data = xml_data.split(" ")
L = 0
sw = {}
open_tag = ['<body>', '<abstract>', '<title>']
close_tag = ['</body>', '</abstract>', '</title>']
cond = False
for str in xml_data:
    if str in open_tag:
        cur = str
        cond = True
        continue
    if str in close_tag:
        cur =""
        cond = False
    if cond :
        token = normalize(str)
        if  len(token) < 4 or token in stop_words or token[0] == '<':
            continue
        L = L + 1
        if token in sw :
            sw[token] = sw.get(token) + get(cur)
        else: sw[token] = get(cur)
res = {}
for w in index_terms:
    if w in sw :
        res[w] = round(sw[w] / L * 100.0,10)
sort_orders = sorted(res.items(), key=lambda x: x[1], reverse=True)

cnt = 0
last = -1
for i in sort_orders:
    if cnt < 3:
        cnt = cnt + 1
        last = i[1]
        print(i[0], ": ", i[1], sep='')
    elif i[1] == last:
 	        print(i[0], ": ", i[1], sep='')