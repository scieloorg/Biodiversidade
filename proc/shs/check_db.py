f = open('../bhl.ids.txt','r')
c = f.readlines()
f.close()

#lilacs
f = open('../bhl2.ids.txt','r')
c2 = f.readlines()
f.close()

d2={}
for item in c2:
    k = item.strip("\n")
    d2[k] = ''


print('######## PROC1 OK, mas nao esta em PROC2 ##########')

d1={}
for item in c:
    k = item.strip("\n")
    try:
        exist = d2[k]
    except:
        print(k)

print('######## PROC2 OK, mas nao esta em PROC1 ##########')


for k,v in d2.items():
    try:
        exist = d1[k]
    except:
        print(k)


print('######## PROC1 e 2 OK ##########')
common={}
for k,v in d1.items():
    try:
        exist = d2[k]
        common[k]=''
    except:
        pass

for k,v in d2.items():
    try:
        exist = d1[k]
        common[k]=''
    except:
        pass

for k,v in common.items():
    print(k)