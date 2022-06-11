import os, sys, re, requests

sandi = ""
id = ""
url1 = "https://m.facebook.com/"
url2 = "m.facebook.com"
ua = "Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"

def metod(): 
	session= requests.Session()
	header = {"Host":url2,
	"upgrade-insecure-requests":"1",
	"user-agent":ua,
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"dnt":"1",
	"x-requested-with":"mark.via.gp",
	"sec-fetch-site":"none",
	"sec-fetch-mode":"navigate",
	"sec-fetch-user":"?1",
	"sec-fetch-dest":"document",
	"referer":url1,
	"accept-encoding":"gzip, deflate",
	"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"} 
	r = session.get(f"{url1}index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",headers=header) 
	das = {"lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),"uid":id,"flow":"login_no_pin","pass":sandi,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
	header1 = {"Host":url2,
	"cache-control":"max-age=0",
	"upgrade-insecure-requests":"1",
	"origin":f"https://{url2}",
	"content-type":"application/x-www-form-urlencoded",
	"user-agent":ua,
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"x-requested-with":"mark.via.gp",
	"sec-fetch-site":"same-origin",
	"sec-fetch-mode":"navigate",
	"sec-fetch-user":"?1",
	"sec-fetch-dest":"document",
	"referer":f"{url1}index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
	"accept-encoding":"gzip, deflate",
	"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	po = session.post(f"{url1}login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False) 
	if "c_user" in session.cookies.get_dict(): 
		kue = session.cookies.get_dict()
		coklat = 'datr=' + kue['datr'] + ';' + ('c_user=' + kue['c_user']) + ';' + ('fr=' + kue['fr']) + ';' + ('xs=' + kue['xs'])  
		print(f" ✓ {id} - {sandi} - {coklat}")
	elif "checkpoint" in session.cookies.get_dict():
		print(f" X {id} - {sandi}")
	
metod()
