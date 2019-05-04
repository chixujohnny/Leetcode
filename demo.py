# coding: utf-8

# a = 'BANC'
# b = 'ABC'
# print b.split('')
# if set(b) in set(a):
#     print 'ok'


lines = open('/Users/chixu.cx/Desktop/亲子case.csv').readlines()  # ['1  2  4','1  3  5']
for line in lines:
    try:
        item = line.split('\t')[2]
        item = item.replace('\n','')
        if float(item) > 0.9:
            print item
    except:
        continue