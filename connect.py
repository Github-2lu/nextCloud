import sys, subprocess, time, signal, smtplib, os
from email.mime.text import MIMEText

def getIp():
    output = subprocess.check_output("hostname -I", shell=True)
    return output.decode("utf-8").split(" ")[0]

def handle_signal(signal, frame):
    proc.kill()
    sys.exit(0)

def send_email(link):
    sender_email = "sudipdatta2002@gmail.com"
    receiver_email = "sudipdatta2002@gmail.com"

    body = f'<a href="{link}">Connect to nextcloud</a>'
    email = MIMEText(body, "html")
    email["Subject"] = "NexCloud Link"
    email["From"] = sender_email
    email["To"] = receiver_email

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(sender_email, "rckpznwnvufgipqm")
    s.sendmail(sender_email, receiver_email, email.as_string())
    s.quit()

signal.signal(signal.SIGINT, handle_signal)

ip = getIp()
print(ip)
command = "cloudflared tunnel --url http://" + ip

home = os.environ["HOME"]
f1 = open(f"{home}/file.txt", "w")
print("connecting to cloudflare tunnel")
proc = subprocess.Popen(args=command, shell=True, stdout=f1, stderr=subprocess.STDOUT)

time.sleep(10)

f2 = open(f"{home}/file.txt", "r")
lines = f2.readlines()
for line in lines:
    if ".trycloudflare.com" in line:
        for link in line.split(" "):
            if "https://" in link:
                print(link)
                send_email(link)

while True:
    time.sleep(0.5)
