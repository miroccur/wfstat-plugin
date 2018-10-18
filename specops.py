import requests

help_message0="-特殊行动 服务器 角色名 —— 查询特殊行动记录\n示例：-狗头 NA marchRPL\n\n-stat 服务器 角色名 —— 查询玩家个人信息\n示例：-stat NA marchRPL\n\n -pvp 服务器 角色名 —— 查询玩家PvP数据\n示例：-pvp na marchRPL"
def result(string):
	splited=string.split()
	num=len(splited)-1
	return splited[num]
	
def isValidStat(response):
	try:
		if response["code"] ==0:
			return False
	except:
		return True
		
def getUserStat(server,username):
	if server.lower() == "eu" or server.lower() == "na":
		if server.lower()=="eu":
			sp=1
		elif server.lower()=="na":
			sp=2
		url="http://api.wf.my.com/user/stat?name=%s&server=%i"%(username,sp)
		return requests.get(url).json()
	elif server.lower()=="alpha" or server.lower()=="bravo" or server.lower()=="charlie":
		if server.lower()=="alpha":
			sp=1
		elif server.lower()=="bravo":
			sp=2
		elif server.lower()=="charlie":
			sp=3
		url="http://api.warface.ru/user/stat?name=%s&server=%i"%(username,sp)
		return requests.get(url).json()
		
def getFullResponse(stat):
	FRstring=stat["full_response"]
	return FRstring.split("\n")


def getAnubisStat(server,username):
	wl={"anubishardloss":None,"anubishardwon":None,"anubisnormalloss":None,"anubisnormalwon":None,"anubiseasyloss":None,"anubiseasywon":None}
	userstat=getUserStat(server, username)
	if isValidStat(userstat):
		statlist=getFullResponse(userstat)
		for x in statlist:
			if "anubishard " in x and "lost" in x:
				wl["anubishardloss"]=result(x)
			elif "anubishard " in x and "won" in x:
				wl["anubishardwon"]=result(x)
			elif "anubisnormal " in x and "lost" in x:
				wl["anubisnormalloss"]=result(x)
			elif "anubisnormal " in x and "won" in x:
				wl["anubisnormalwon"]=result(x)
			elif "anubiseasy " in x and "lost" in x:
				wl["anubiseasyloss"]=result(x)
			elif "anubiseasy " in x and "won" in x:
				wl["anubiseasywon"]=result(x)
		for x in wl:
			if wl[x]==None:
				wl[x]=0
		finalstat="%s：\n阿努比斯\n简单：%s/%s\n普通：%s/%s\n困难：%s/%s"%(userstat["nickname"],wl["anubiseasywon"],wl["anubiseasyloss"],wl["anubisnormalwon"],wl["anubisnormalloss"],wl["anubishardwon"],wl["anubishardloss"])
		return finalstat
	else:
		return "您所输入的玩家名称不存在或该玩家选择隐藏个人数据"

def getBSStat(server,username):
	wl={"hardloss":None,"hardwon":None,"normalloss":None,"normalwon":None,"easyloss":None,"easywon":None}
	userstat=getUserStat(server, username)
	if isValidStat(userstat):
		statlist=getFullResponse(userstat)
		for x in statlist:
			if "zombietowerhard " in x and "lost" in x:
				wl["hardloss"]=result(x)
			elif "zombietowerhard " in x and "won" in x:
				wl["hardwon"]=result(x)
			elif "zombietowernormal " in x and "lost" in x:
				wl["normalloss"]=result(x)
			elif "zombietowernormal " in x and "won" in x:
				wl["normalwon"]=result(x)
			elif "zombietowereasy " in x and "lost" in x:
				wl["easyloss"]=result(x)
			elif "zombietowereasy " in x and "won" in x:
				wl["easywon"]=result(x)
		for x in wl:
			if wl[x]==None:
				wl[x]=0
		finalstat="%s：\n黑鲨\n简单：%s/%s\n普通：%s/%s\n困难：%s/%s"%(userstat["nickname"],wl["easywon"],wl["easyloss"],wl["normalwon"],wl["normalloss"],wl["hardwon"],wl["hardloss"])
		return finalstat
	else:
		return "您所输入的玩家名称不存在或该玩家选择隐藏个人数据"

def getBOStat(server,username):
	wl={"hardloss":None,"hardwon":None,"normalloss":None,"normalwon":None,"easyloss":None,"easywon":None}
	userstat=getUserStat(server, username)
	if isValidStat(userstat):
		statlist=getFullResponse(userstat)
		for x in statlist:
			if "anubishard2 " in x and "lost" in x:
				wl["hardloss"]=result(x)
			elif "anubishard2 " in x and "won" in x:
				wl["hardwon"]=result(x)
			elif "anubisnormal2 " in x and "lost" in x:
				wl["normalloss"]=result(x)
			elif "anubisnormal2 " in x and "won" in x:
				wl["normalwon"]=result(x)
			elif "anubiseasy2 " in x and "lost" in x:
				wl["easyloss"]=result(x)
			elif "anubiseasy2 " in x and "won" in x:
				wl["easywon"]=result(x)
		for x in wl:
			if wl[x]==None:
				wl[x]=0
		finalstat="%s：\n灯火管制\n简单：%s/%s\n普通：%s/%s\n困难：%s/%s"%(userstat["nickname"],wl["easywon"],wl["easyloss"],wl["normalwon"],wl["normalloss"],wl["hardwon"],wl["hardloss"])
		return finalstat
	else:
		return "您所输入的玩家名称不存在或该玩家选择隐藏个人数据"

def getPPStat(server,username):
	wl={"hardloss":None,"hardwon":None,"normalloss":None,"normalwon":None,"easyloss":None,"easywon":None}
	userstat=getUserStat(server, username)
	if isValidStat(userstat):
		statlist=getFullResponse(userstat)
		for x in statlist:
			if "chernobylhard " in x and "lost" in x:
				wl["hardloss"]=result(x)
			elif "chernobylhard " in x and "won" in x:
				wl["hardwon"]=result(x)
			elif "chernobylnormal " in x and "lost" in x:
				wl["normalloss"]=result(x)
			elif "chernobylnormal " in x and "won" in x:
				wl["normalwon"]=result(x)
			elif "chernobyleasy " in x and "lost" in x:
				wl["easyloss"]=result(x)
			elif "chernobyleasy " in x and "won" in x:
				wl["easywon"]=result(x)
		for x in wl:
			if wl[x]==None:
				wl[x]=0
		finalstat="%s：\n普里皮亚季\n简单：%s/%s\n普通：%s/%s\n困难：%s/%s"%(userstat["nickname"],wl["easywon"],wl["easyloss"],wl["normalwon"],wl["normalloss"],wl["hardwon"],wl["hardloss"])
		return finalstat
	else:
		return "您所输入的玩家名称不存在或该玩家选择隐藏个人数据"

def getIBStat(server,username):
	wl={"hardloss":None,"hardwon":None,"normalloss":None,"normalwon":None,"easyloss":None,"easywon":None}
	userstat=getUserStat(server, username)
	if isValidStat(userstat):
		statlist=getFullResponse(userstat)
		for x in statlist:
			if "icebreakerhard " in x and "lost" in x:
				wl["hardloss"]=result(x)
			elif "icebreakerhard " in x and "won" in x:
				wl["hardwon"]=result(x)
			elif "icebreakernormal " in x and "lost" in x:
				wl["normalloss"]=result(x)
			elif "icebreakernormal " in x and "won" in x:
				wl["normalwon"]=result(x)
			elif "icebreakereasy " in x and "lost" in x:
				wl["easyloss"]=result(x)
			elif "icebreakereasy " in x and "won" in x:
				wl["easywon"]=result(x)
		for x in wl:
			if wl[x]==None:
				wl[x]=0
		print(wl)
		finalstat="%s：\n破冰者\n简单：%s/%s\n普通：%s/%s\n困难：%s/%s"%(userstat["nickname"],wl["easywon"],wl["easyloss"],wl["normalwon"],wl["normalloss"],wl["hardwon"],wl["hardloss"])
		return finalstat
	else:
		return "您所输入的玩家名称不存在或该玩家选择隐藏个人数据"
		
def getESStat(server,username):
	wl={"hardloss":None,"hardwon":None,"normalloss":None,"normalwon":None,"easyloss":None,"easywon":None,"nmloss":None,"nmwon":None}
	userstat=getUserStat(server, username)
	if isValidStat(userstat):
		statlist=getFullResponse(userstat)
		for x in statlist:
			if "volcanohard " in x and "lost" in x:
				wl["hardloss"]=result(x)
			elif "volcanohard " in x and "won" in x:
				wl["hardwon"]=result(x)
			elif "volcanonormal " in x and "lost" in x:
				wl["normalloss"]=result(x)
			elif "volcanonormal " in x and "won" in x:
				wl["normalwon"]=result(x)
			elif "volcanoeasy " in x and "lost" in x:
				wl["easyloss"]=result(x)
			elif "volcanoeasy " in x and "won" in x:
				wl["easywon"]=result(x)
			elif "volcanosurvival " in x and "lost" in x:
				wl["nmloss"]=result(x)
			elif "volcanosurvival " in x and "won" in x:
				wl["nmwon"]=result(x)
		for x in wl:
			if wl[x]==None:
				wl[x]=0
		finalstat="%s：\n撼地者\n简单：%s/%s\n普通：%s/%s\n困难：%s/%s\n噩梦：%s/%s"%(userstat["nickname"],wl["easywon"],wl["easyloss"],wl["normalwon"],wl["normalloss"],wl["hardwon"],wl["hardloss"],wl["nmwon"],wl["nmloss"])
		return finalstat
	else:
		return "您所输入的玩家名称不存在或该玩家选择隐藏个人数据"

def getCPStat(server,username):
	wl={"s1loss":None,"s1won":None,"s2loss":None,"s2won":None,"s3loss":None,"s3won":None,"marathonloss":None,"marathonwon":None}
	userstat=getUserStat(server, username)
	if isValidStat(userstat):
		statlist=getFullResponse(userstat)
		for x in statlist:
			if "campaignsection1 " in x and "lost" in x:
				wl["s1loss"]=result(x)
			elif "campaignsection1 " in x and "won" in x:
				wl["s1won"]=result(x)
			elif "campaignsection2 " in x and "lost" in x:
				wl["s2loss"]=result(x)
			elif "campaignsection2 " in x and "won" in x:
				wl["s2won"]=result(x)
			elif "campaignsection3 " in x and "lost" in x:
				wl["s3loss"]=result(x)
			elif "campaignsection3 " in x and "won" in x:
				wl["s3won"]=result(x)
			elif "campaignsections " in x and "lost" in x:
				wl["marathonloss"]=result(x)
			elif "campaignsections " in x and "won" in x:
				wl["marathonwon"]=result(x)
		for x in wl:
			if wl[x]==None:
				wl[x]=0
		finalstat="%s：\n冷峰\n矛头：%s/%s\n伏击：%s/%s\n顶点：%s/%s\n马拉松：%s/%s"%(userstat["nickname"],wl["s1won"],wl["s1loss"],wl["s2won"],wl["s2loss"],wl["s3won"],wl["s3loss"],wl["marathonwon"],wl["marathonloss"])
		return finalstat
	else:
		return "您所输入的玩家名称不存在或该玩家选择隐藏个人数据"

def getHQStat(server,username):
	wl={"s1loss":None,"s1won":None}
	userstat=getUserStat(server, username)
	if isValidStat(userstat):
		statlist=getFullResponse(userstat)
		for x in statlist:
			if "survivalmission " in x and "lost" in x:
				wl["s1loss"]=result(x)
			elif "survivalmission " in x and "won" in x:
				wl["s1won"]=result(x)
		for x in wl:
			if wl[x]==None:
				wl[x]=0
		finalstat="%s：\n总部\n夺塔：%s/%s"%(userstat["nickname"],wl["s1won"],wl["s1loss"])
		return finalstat
	else:
		return "您所输入的玩家名称不存在或该玩家选择隐藏个人数据"


	


def onQQMessage(bot, contact, member, content):
	arglist=content.split()
	if arglist[0]=="[@ME]":
		if arglist[1]=="阿努比斯" or arglist[1]=="狗头":
			print("getting anubis stats")
			bot.SendTo(contact,getAnubisStat(arglist[2], arglist[3]))
		elif arglist[1]=="黑鲨":
			bot.SendTo(contact,getBSStat(arglist[2], arglist[3]))
		elif arglist[1]=="灯火管制" or arglist[1]=="灯火":
			bot.SendTo(contact,getBOStat(arglist[2], arglist[3]))
		elif arglist[1]=="普里皮亚季" or arglist[1]=="皮城":
			bot.SendTo(contact,getPPStat(arglist[2], arglist[3]))
		elif arglist[1]=="破冰者" or arglist[1]=="破冰":
			bot.SendTo(contact,getIBStat(arglist[2], arglist[3]))
		elif arglist[1]=="冷锋" or arglist[1]=="冷峰" or arglist[1]=="马拉松":
			bot.SendTo(contact,getCPStat(arglist[2], arglist[3]))
		elif arglist[1]=="总部" or arglist[1]=="大白鲨":
			bot.SendTo(contact,getHQStat(arglist[2], arglist[3]))
		elif arglist[1]=="撼地者" or arglist[1]=="火山":
			bot.SendTo(contact,getESStat(arglist[2], arglist[3]))	
		elif arglist[1]=="help":
			bot.SendTo(contact,help_message0)
	else:
		if arglist[0]=="-阿努比斯" or arglist[0]=="-狗头":
			print("getting anubis stats")
			bot.SendTo(contact,getAnubisStat(arglist[1], arglist[2]))
		elif arglist[0]=="-黑鲨":
			bot.SendTo(contact,getBSStat(arglist[1], arglist[2]))
		elif arglist[0]=="-灯火管制" or arglist[0]=="-灯火":
			bot.SendTo(contact,getBOStat(arglist[1], arglist[2]))
		elif arglist[0]=="-普里皮亚季" or arglist[0]=="-皮城":
			bot.SendTo(contact,getPPStat(arglist[1], arglist[2]))
		elif arglist[0]=="-破冰者" or arglist[0]=="-破冰":
			print("getting ib stats")
			bot.SendTo(contact,getIBStat(arglist[1], arglist[2]))
		elif arglist[0]=="-冷锋" or arglist[0]=="-冷峰" or arglist[0]=="-马拉松":
			bot.SendTo(contact,getCPStat(arglist[1], arglist[2]))
		elif arglist[0]=="-总部" or arglist[0]=="-大白鲨":
			bot.SendTo(contact,getHQStat(arglist[1], arglist[2]))
		elif arglist[0]=="-撼地者" or arglist[0]=="-火山":
			bot.SendTo(contact,getESStat(arglist[1], arglist[2]))	
		elif arglist[0]=="-help":
			bot.SendTo(contact,help_message0)		
