import requests
import math

def WeaponIDtoName(weaponID):
	
	
def result(string):
	splited=string.split()
	num=len(splited)-1
	return splited[num]

def className(theclass):
	if theclass=="Rifleman":
		return "步枪手"
	elif theclass=="Medic":
		return "医疗兵"
	elif theclass=="Engineer":
		return "工程师"
	elif theclass=="Recon":
		return "狙击手"
	
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

def isValidStat(response):
	try:
		if response["code"] ==0:
			return False
	except:
		return True

def getWeaponID(usgstr):
	usglist=usgstr.split()
	return usglist[2][11:]

def getWeaponUsage(FRlist,theClass):
	if theClass=="rifleman":
		wpn=None
		usage=0
		for x in FRlist:
			if "Rifleman" in x and "player_wpn_usage" in x:
				if int(result(x))>usage:
					usage=int(result(x))
					wpn=getWeaponID(x)
		return {wpn:usage}
	elif theClass=="medic":
		wpn=None
		usage=0
		for x in FRlist:
			if "Medic" in x and "player_wpn_usage" in x:
				if int(result(x))>usage:
					usage=int(result(x))
					wpn=getWeaponID(x)
		return {wpn:usage}
	elif theClass=="engineer":
		wpn=None
		usage=0
		for x in FRlist:
			if "Engineer" in x and "player_wpn_usage" in x:
				if int(result(x))>usage:
					usage=int(result(x))
					wpn=getWeaponID(x)
		return {wpn:usage}
	elif theClass=="sniper":
		wpn=None
		usage=0
		for x in FRlist:
			if "Recon" in x and "player_wpn_usage" in x:
				if int(result(x))>usage:
					usage=int(result(x))
					wpn=getWeaponID(x)
		return {wpn:usage}

def getProfileInfo(server,username):
	userstat=getUserStat(server,username)
	if isValidStat(userstat):
		if userstat["nickname"] == "Medcull..MMP":
			nickname="%s\n称号：27场噩梦只出一个头的人！"%(userstat["nickname"])
		else:
			nickname=userstat["nickname"]
		rank=userstat["rank_id"]
		try:
			clan=userstat["clan_name"]
		except:
			clan="无战队"
		kill=userstat["kill"]
		friendly_kill=userstat["friendly_kills"]
		death=userstat["death"]
		kd=userstat["pvp"]
		fav_class_pvp=className(userstat["favoritPVP"])
		fav_class_pve=className(userstat["favoritPVE"])
		playtime="%s小时%s分钟"%(userstat["playtime_h"],userstat["playtime_m"])
		return "名称：%s\n等级：%s\n战队：%s\n杀敌数：%s\n死亡数：%s\n杀死队友数：%s\nKD：%s\nPvP常用职业：%s\nPvE常用职业：%s\n游戏时长：%s"%(nickname,rank,clan,kill,death,friendly_kill,kd,fav_class_pvp,fav_class_pve,playtime)
	else:
		return "您所输入的玩家名称不存在或该玩家选择隐藏个人数据"

def getPvPInfo(server,username):
	userstat=getUserStat(server,username)
	if isValidStat(userstat):
		FRlist=getFullResponse(userstat)
		if userstat["nickname"] == "Medcull..MMP":
			nickname="%s\n称号：27场噩梦只出一个头的人！"%(userstat["nickname"])
		else:
			nickname=userstat["nickname"]
		rank=userstat["rank_id"]
		try:
			clan=userstat["clan_name"]
		except:
			clan="无战队"
		kill=userstat["kill"]
		friendly_kill=userstat["friendly_kills"]
		death=userstat["death"]
		kd=userstat["pvp"]
		fav_class_pvp=className(userstat["favoritPVP"])
		for x in FRlist:
			if "[class]Rifleman [mode]PVP [stat]player_playtime" in x:
				rifletime=int(result(x))
			elif "[class]Medic [mode]PVP [stat]player_playtime" in x:
				medictime=int(result(x))
			elif "[class]Engineer [mode]PVP [stat]player_playtime" in x:
				engitime=int(result(x))
			elif "[class]Recon [mode]PVP [stat]player_playtime" in x:
				snipertime=int(result(x))
			elif "[class]Rifleman [mode]PVP [stat]player_shots" in x:
				rifleshots=int(result(x))
			elif "[class]Medic [mode]PVP [stat]player_shots" in x:
				medicshots=int(result(x))
			elif "[class]Engineer [mode]PVP [stat]player_shots" in x:
				engishots=int(result(x))
			elif "[class]Recon [mode]PVP [stat]player_shots" in x:
				snipershots=int(result(x))
			elif "[class]Rifleman [mode]PVP [stat]player_hits" in x:
				riflehits=int(result(x))
			elif "[class]Medic [mode]PVP [stat]player_hits" in x:
				medichits=int(result(x))
			elif "[class]Engineer [mode]PVP [stat]player_hits" in x:
				engihits=int(result(x))
			elif "[class]Recon [mode]PVP [stat]player_hits" in x:
				sniperhits=int(result(x))
			elif "[class]Rifleman [mode]PVP [stat]player_headshots" in x:
				riflehs=int(result(x))
			elif "[class]Medic [mode]PVP [stat]player_headshots" in x:
				medichs=int(result(x))
			elif "[class]Engineer [mode]PVP [stat]player_headshots" in x:
				engihs=int(result(x))
			elif "[class]Recon [mode]PVP [stat]player_headshots" in x:
				sniperhs=int(result(x))
			elif "[mode]PVP [stat]player_sessions_kicked" in x:
				kicked=int(result(x))
			elif "[mode]PVP [stat]player_sessions_left" in x:
				left=int(result(x))
		if "rifletime" not in locals():
			rifletime=0
		if "medictime" not in locals():
			medictime=0
		if "engitime" not in locals():
			engitime=0
		if "snipertime" not in locals():
			snipertime=0
		if "rifleshots" not in locals():
			rifleshots=0
		if "medicshots" not in locals():
			medicshots=0
		if "engishots" not in locals():
			engishots=0
		if "snipershots" not in locals():
			snipershots=0
		if "riflehits" not in locals():
			riflehits=0
		if "medichits" not in locals():
			medichits=0
		if "engihits" not in locals():
			engihits=0
		if "sniperhits" not in locals():
			sniperhits=0
		if "riflehs" not in locals():
			riflehs=0
		if "medichs" not in locals():
			medichs=0
		if "engihs" not in locals():
			engihs=0
		if "sniperhs" not in locals():
			sniperhs=0
		if "kicked" not in locals():
			kicked=0
		if "left" not in locals():
			left=0
		gameWon=userstat["pvp_wins"]
		gameLost=userstat["pvp_lost"]
		gameTotal=gameWon+gameLost
		pvpWL=userstat["pvpwl"]
		rifleplaytime="%i小时%i分钟"%(math.floor(rifletime/36000),math.floor(((rifletime/36000)-math.floor(rifletime/36000))*60))
		medicplaytime="%i小时%i分钟"%(math.floor(medictime/36000),math.floor(((medictime/36000)-math.floor(medictime/36000))*60))
		engiplaytime="%i小时%i分钟"%(math.floor(engitime/36000),math.floor(((engitime/36000)-math.floor(engitime/36000))*60))
		sniperplaytime="%i小时%i分钟"%(math.floor(snipertime/36000),math.floor(((snipertime/36000)-math.floor(snipertime/36000))*60))
		try:
			rifleacc=str(math.floor((riflehits/rifleshots)*100))
		except:
			rifleacc=0
		try:
			medicacc=str(math.floor((medichits/medicshots)*100))
		except:
			medicacc=0
		try:
			engiacc=str(math.floor((engihits/engishots)*100))
		except:
			engiacc=0
		try:
			sniperacc=str(math.floor((sniperhits/snipershots)*100))
		except:
			sniperacc=0
		string="名称：%s\n等级：%s\n战队：%s\n杀敌数：%s\n死亡数：%s\n杀死队友数：%s\nKD：%s\n比赛数：%s\n胜利场次：%s\n失败场次：%s\n胜率：%s\n中途退出：%s\n常用职业：%s\n\n步枪手\n时长：%s\n精准度：%s%%\n爆头：%s\n\n医疗兵\n时长：%s\n精准度：%s%%\n爆头：%s\n\n工程师\n时长：%s\n精准度：%s%%\n爆头：%s\n\n狙击手\n时长：%s\n精准度：%s%%\n爆头：%s\n\n注：此处精准度为PvP精准度，游戏内数据为总精准度"%(nickname,rank,clan,kill,death,friendly_kill,kd,gameTotal,gameWon,gameLost,pvpWL,left,fav_class_pvp,rifleplaytime,rifleacc,riflehs,medicplaytime,medicacc,medichs,engiplaytime,engiacc,engihs,sniperplaytime,sniperacc,sniperhs)
		return string
	else:
		return "您所输入的玩家名称不存在或该玩家选择隐藏个人数据"

def onQQMessage(bot, contact, member, content):
	arglist=content.split()
	if arglist[0]=="[@ME]":
		if len(arglist)==4:
			if arglist[1].lower()=="stat":
				bot.SendTo(contact,getProfileInfo(arglist[2],arglist[3]))
			elif arglist[1].lower()=="pvp":
				bot.SendTo(contact,getPvPInfo(arglist[2], arglist[3]))
	else:
		if len(arglist)==3:
			if arglist[0].lower()=="-stat":
				bot.SendTo(contact,getProfileInfo(arglist[1], arglist[2]))
			elif arglist[0].lower()=="-pvp":
				bot.SendTo(contact,getPvPInfo(arglist[1], arglist[2]))
