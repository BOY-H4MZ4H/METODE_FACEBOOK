# METOD FACEBOOK VERSI 2

import requests, re, random
from rich import print as prints
from rich.tree import Tree

cebok = "m.facebook.com"
aide = "" # Id Facebook
pw = "" # Sandi Facebook
ua = "" # USER AGENT

def cek(): 
	session = requests.Session()
	kawaii = {
	"Host": cebok,
	"Upgrade-Insecure-Requests": "1",
	"User-Agent": ua,
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"Dnt": "1",
	"X-Requested-With": "com.facebook.katana",
	"Sec-Fetch-Site": "same-origin",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-User": "empty",
	"Sec-Fetch-Dest": "document",
	"Referer": f"https://{cebok}/",
	"Accept-Encoding": "gzip, deflate",
	"Accept-Language": "en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7"}
	baka = session.get(f"https://{cebok}/login/device-based/password/?uid={aide}&flow=login_no_pin&refsrc=deprecated&_rdr",headers=kawaii).text 
	alicia = {
	"lsd": re.search('name="lsd" value="(.*?)"',str(baka)).group(1),
	"jazoest": re.search('name="jazoest" value="(.*?)"', str(baka)).group(1),
	"uid": aide,
	"next": f"https://{cebok}/login/save-device/",
	"flow": "login_no_pin",
	"pass": pw}
	cook = {'cookie': (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items()])+';m_pixel_ratio=1.7000000476837158;wd=424x781'}
	oppai = {
	"Host": cebok,
	"Cache-Control": "max-age=0",
	"Upgrade-Insecure-Requests": "1",
	"Origin": f"https://{cebok}",
	"Content-Type": "application/x-www-form-urlencoded",
	"User-Agent": ua,
	"Accept": "*/*",
	"X-Requested-With": "com.facebook.katana",
	"Sec-Fetch-Site": "same-origin",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-User": "empty",
	"Sec-Fetch-Dest": "document",
	'Referer': f'https://{cebok}/login/device-based/password/?uid={aide}&flow=login_no_pin&refsrc=deprecated&_rdr',
	"Accept-Encoding": "gzip, deflate",
	"Accept-Language": "en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7"}
	ikeh = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0",data=alicia,cookies=cook,headers=oppai,allow_redirects=False)
	if "c_user" in session.cookies.get_dict():
		kueh = session.cookies.get_dict()
		cookie = "datr=" + kueh["datr"] + ";" + ("sb=" + kueh["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + kueh["c_user"]) + ";" + ("xs=" + kueh["xs"]) + ";" + ("fr=" + kueh["fr"]) + ";"
		prints(session.cookies.get_dict())
		prints(cook)
		prints(alicia)
		tree = Tree("")
		tree.add(f" ✅ [#AAAAAA]{aide} - {pw} - {cookie}")
		prints(tree)
	elif "checkpoint" in session.cookies.get_dict():
		tree = Tree("")
		tree.add(f" ✖️ [#AAAAAA]{aide} - {pw}")
		prints(tree)
		
cek()
