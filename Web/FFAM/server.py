from flask import *
from flask_session import *
import jwt
import os
import subprocess

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(100)
app.config['SESSION_TYPE'] = 'filesystem'


class JWT_class:
    def __init__(self):
        with open('ASECRETKEY.txt', 'r') as file:
            SECRETKEY = file.readline()
            self.secret_key = SECRETKEY.encode()
        print(self.secret_key)


    def JWT_user(self):
        data = {'id': 2, 'role': "User"}

        token = jwt.encode(data, self.secret_key, algorithm='HS256')
        return token

    def JWT_Naup(self):
        data = {'id': 1, 'role': "Naup"}

        token = jwt.encode(data, self.secret_key, algorithm='HS256')

        return token
    
def init_session():
    if  "money" not in session:
        session["money"]=2000
    if "USB" not in session:
        session["USB"]=0
    if "KEYBOARD" not in session:
        session["KEYBOARD"]=0
    if "RAM" not in session:
        session["RAM"]=0

JWTMODE=JWT_class()


@app.route("/")
def home():
    init_session()
    return redirect("/FFAM")

@app.route("/FFAM")
def FFAM():
    if "RAM" not in session:
        session["RAM"]=0
    if session['RAM']>=3:
        return redirect("/shell")
    
    return render_template("cmd.html",RAM=2+session['RAM']*2)

@app.route("/robots.txt")
def robotstxt():
    return send_from_directory(app.static_folder,"robots.txt")



@app.route("/ShopAboutComputerEquipment")
def ShopAboutComputerEquipment():

    init_session()

    resp = make_response(render_template('menu.html',MONEY=session["money"],USB=session["USB"],Keyboard=session["KEYBOARD"],FFAMRAM=session["RAM"]))
    resp.set_cookie('YourToKeNinShop', JWTMODE.JWT_user())
    return resp

@app.route("/webshell")
def webshell():
    return render_template("webshell.html")

@app.route("/webshellexe",methods=["GET", "POST"])
def webshellexe():
    BLACKLIST = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"`:\'\\{}[]'
    code = request.json
    cmd=code.get('cmd')

    if len(cmd) >= 5:
        return 'Too long!!!'

    for i in BLACKLIST:
        if i in cmd:
            return "You don't use this characters!!"
                
    proc = subprocess.Popen(["/bin/sh", "-c", cmd], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    return proc.stdout.read().decode('utf-8')


@app.route("/redeemcode", methods=["GET", "POST"])
def redeem_code():
    if request.method == "GET":
  
        return render_template('redeemcode.html')
    elif request.method == "POST":
        code = request.json
        userinput=code.get('redeemcode')
        
        if userinput=="NaupRedeemCode":
            res="Success!{redeemcode} is Correct!\nHere is secret:https://www.youtube.com/watch?v=dQw4w9WgXcQ".format(redeemcode=userinput)
            return {"redeemcode":userinput,"resp":res}
        else:
            res="Failed!!{redeemcode} is not true!Nothing to do!".format(redeemcode=userinput)
            return {"redeemcode":userinput,"resp":res}

@app.route("/ORDER", methods=["GET", "POST"])
def ORDER():
    USB=int(request.values["USB"])
    KEYBOARD=int(request.values["Keyboard"])
    RAM=int(request.values["RAM"])
    YourToKeNinShop = request.cookies.get('YourToKeNinShop')
    if YourToKeNinShop!=JWTMODE.JWT_Naup() and (RAM>0 or RAM<0):
        
        flash("You are not my MASTER!Bad hacker!")
        return redirect('/ShopAboutComputerEquipment')
    else:
        if session["money"]-USB*300-KEYBOARD*1000-RAM*200000>=0:
            session["money"]=session["money"]-USB*300-KEYBOARD*1000-RAM*200000
            session["USB"]+=USB
            session["KEYBOARD"]+=KEYBOARD
            session["RAM"]+=RAM
            flash("Success!!")
            return redirect('/ShopAboutComputerEquipment')
        else:
            flash("You don't have enough money.")
            return redirect('/ShopAboutComputerEquipment')
        
@app.route("/REFRESH", methods=["GET", "POST"])
def REFRESH():
    session["money"]=2000
    session["USB"]=0
    session["KEYBOARD"]=0
    session["RAM"]=0
    return redirect('/ShopAboutComputerEquipment')

@app.route("/shell")
def shell():
    if session["RAM"] <3:
        return redirect("/FFAM")
    return render_template("shell.html",RAM=2+session["RAM"]*2)

@app.route("/exe", methods=["GET", "POST"])
def exe():
    if session["RAM"] <3:
        return redirect("/FFAM")
    data = request.json
    user_input = data.get('userInput')
   
    BLACKLIST=[ ';', '>','|', '&', '<', '\n','`', '*', '?','{' , '}', '[', ']','%']
    for i in BLACKLIST:
        if i in user_input:
            return "You are not my MASTER.You don't use this character."
        
    cmd="cat %s.txt"% (user_input)
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        output = str(result.stdout)
        
        return output
    else:
        output = "Command failed with error code:"+str(result.returncode)
        return output
    

if __name__ == "__main__":

    app.run(host="0.0.0.0",port="10000",debug=False)
