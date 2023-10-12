import csv
import json
import os
datadict={}
val=False
def searche(dat,ind,txt,trig=1,trig2=0):
	for i in ind:
		try:
			if trig:
				dat[i[0]][txt]=i[1]
			else:
				dat[i[0]][txt]=[i[1],i[2]]
				
		except KeyError:
			pass
	return dat	
def mssgread():
	global datadict
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
	with open("users.csv",newline='',encoding='utf-8') as fil:
		aa=list(csv.reader(fil))
		aa.pop(0)
		userlist={"unknown":"unknown"}
		for i in aa:
			userlist[i[0]]=i[1]
	with open('messages.csv',newline='', encoding='utf-8') as fil:
		aa = list(csv.reader(fil))
		aa.pop(0)
		messages=[]
		k=0
		for i in aa:
			try:
				i[1]=userlist[i[1]]
			except KeyError:
				i[1]=userlist["unknown"]
			messages.append([i[0],i[1],i[3]])
			k+=1
			if k==val:
				break
		for i in messages:
			datadict[i[0]]={"sender":i[1],"mssgcontent":i[2],"reacts":"","replyto":"","attachment":"","embed":""}

	datadict=searche(datadict,attachments,"attachment",1,1)
	datadict=searche(datadict,reply,"replyto")
	datadict=searche(datadict,reactions,"reacts",0)
	datadict=searche(datadict,embeds,"embed")
	return datadict
