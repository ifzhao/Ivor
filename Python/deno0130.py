fp=open('D:/test.txt','a+')
print('20230130', file=fp)
fp.close()

with open('D:/test1.txt','a+') as file:
    file.write('今天是2023年1月30日')
