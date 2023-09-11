import csv
locfile=[r""]
deffie=""
datadict={}
val=False
def searche(dat,ind,txt,trig=1,trig2=0):
	for i in ind:
		try:
			if trig:
				if trig2:
					dat[i[0]][txt]=deffie
				else:
					dat[i[0]][txt]=i[1]
			else:
				dat[i[0]][txt]=[i[1],i[2]]
				
		except KeyError:
			pass
	if trig2:
		for nm in locfile:
			with open(nm,"r") as fws:
				daloc=eval(fws.read())
				for i in daloc:
					try:
						dat[i[0].decode('utf8')]["attachment"]=i[1]
					except KeyError:
						pass
	return dat	

with open('replied_to.csv',newline='', encoding='utf-8') as fil:
    aa = list(csv.reader(fil))
reply=[]
aa.pop(0)
k=0
for i in aa:
	reply.append(i)
	k+=1
	if k==val:
		break

with open('reactions.csv',newline='', encoding='utf-8') as fil:
    aa = list(csv.reader(fil))
aa.pop(0)
reactions=[]
k=0
for i in aa:
	i=[i[0],i[1],i[2]]
	reactions.append(i)
	k+=1
	if k==val:
		break

attachments=[]
with open('attachments.csv',newline='', encoding='utf-8') as fil:
    aa = list(csv.reader(fil))
aa.pop(0)
k=0
for i in aa:
	attachments.append([i[0],i[4]])
	k+=1
	if k==val:
		break
"""
embeds=[]
with open('embeds.csv', newline='', encoding='utf-8') as fil:
    aa = list(csv.reader(fil))
aa.pop(0)
k=0
for i in aa:
	ii=json.loads(i[1]) 
	embeds.append([i[0],ii['url']])
	k+=1
	if k==val:
		break
"""
with open('messages.csv',newline='', encoding='utf-8') as fil:
    aa = list(csv.reader(fil))
aa.pop(0)
messages=[]
k=0
for i in aa:
	messages.append([i[0],i[1],i[3]])
	k+=1
	if k==val:
		break
for i in messages:
	datadict[i[0]]={"sender":i[1],"mssgcontent":i[2],"reacts":"","replyto":"","attachment":""}

print(attachments[0:5])
datadict=searche(datadict,attachments,"attachment",1,1)
print("--"*45)
print(reply[0:5])
datadict=searche(datadict,reply,"replyto")
print("--"*45)
"""
print(embeds[0:5])
datadict=searche(datadict,embeds,"embedlink")
print("--"*45)
"""
print(reactions[0:5])
datadict=searche(datadict,reactions,"reacts",0)
print("--"*45)
print("_"*45)
with open("jhsadj.txt","w",encoding="utf-8") as ff: 
	for i in datadict:
		ff.write(f"{i} {datadict[i]}\n")
print(len(datadict))
"""
with open('messages.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    print(type(csv_reader))

    for row in csv_reader:
            print(row)
            line_count += 1
            if line_count==10:
            	break
    print(f'Processed {line_count} lines.')
"""
