import socket
from datetime import datetime
import random
import sys
from cProfile import label
from decimal import*
#from goto import with_goto

print("UP-FIEK")
print("Rrjeta Kompjuterike")
print("UDP Server")
print("\n------------------------------------------------------------------------------\n")

serverPort = 9000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("Miresevini ne Vegim's server! ")
print("\n\tServeri eshte i gatshem, ne pritje te te merr kerkes:\n")


listaNjesi=['CelsiusToKelvin','CelsiusToFahrenheit','KelvinToFahrenheit','KelvinToCelsius','FahrenheitToCelsius','FahrenheitToKelvin','PoundToKilogram','KilogramToPound']
def zgjedhFunksionin(zgjedhja, numri):
    if(zgjedhja==listaNjesi[0]):
        return float(numri)-273.15
    elif(zgjedhja==listaNjesi[1]):
        return numri * 9/5 + 32
    elif(zgjedhja==listaNjesi[2]):
        return numri * 9/5 - 459.67
    elif(zgjedhja==listaNjesi[3]):
        return numri - 273.15
    elif(zgjedhja==listaNjesi[4]):
        return (numri- 32) * 5/9
    elif(zgjedhja==listaNjesi[5]):
        return (numri + 459.67) * 5/9
    elif(zgjedhja==listaNjesi[6]):
        return numri * 0.45359237
    elif(zgjedhja==listaNjesi[7]):
        return numri / 0.45359237
    else:
        Printo()

def Printo():
    print("Ju lutemi zgjidheni njesin nga lista dhe le te pasohet me nje numer per shenderrim:")
    for i in range(0,8):
        print(listaNjesi[i])

    




while True:
    kerkesa, clientAddress = serverSocket.recvfrom(4096)
    mesazhi=""
    zanoret=['a','e','ë','i','o','u','y']
    k=[]
    shenja=0
    eksponenti=0
    mantisa=0
    vendPika=0
    eksponentiExtra=0
    if (kerkesa=="IP"):
        mesazhi=str(clientAddress[0])
        mesazhi="IP adresa e klientit eshte :"+mesazhi
    elif(kerkesa=="PORT"):
        mesazhi=str(clientAddress[1])
        mesazhi="Klienti eshte duke perdorur portin :"+mesazhi
    elif(kerkesa.split(" ")[0]=="ZANORE"):
        teksti=kerkesa.replace("ZANORE ", "")
        teksti=teksti.lower()
        for i in range(0,len(teksti)):
            for j in range(0,len(zanoret)):
                if teksti[i]==zanoret[j]:
                    k.append(zanoret[j])
        k.sort()              
        mesazhi=str(len(k))
        mesazhi="Teksti derguar permban "+mesazhi+" zanore"
    elif(kerkesa.split(" ")[0]=="PRINTO"):
        teksti=kerkesa.replace("PRINTO ","")
        #if (teksti[0].lower()):#teksti[0].islower()
        teksti=teksti.replace(teksti[0], teksti[0].upper())
        mesazhi=teksti
    elif(kerkesa=="HOST"):
        try:
            mesazhi=socket.gethostname()
            mesazhi="Emri i klientit eshte: "+mesazhi
        except socket.error:
            mesazhi="Nuk mundemi ta gjejme hostname-in"
    elif(kerkesa=="TIME"):
        mesazhi=str(datetime.now())[0:19]
        mesazhi="Koha momentale eshte: "+mesazhi
    elif(kerkesa=="KENO"):
        vleraPas=0
        for i in range(0,20):
            vleraPara=int(random.random()*10)
            mesazhi+=str(vleraPara+vleraPas)+" "
            vleraPas=vleraPara+vleraPas
        mesazhi="Numrat e gjeneruar me funksionin e rastesishem nga 1 deri ne 80 jane:\n"+str(mesazhi)
    elif(kerkesa.split(" ")[0]=="KONVERTO"):
        zgjedh=kerkesa.split(" ")[1]
        numrin=kerkesa.split(" ")[2]
        result=zgjedhFunksionin(zgjedh, numrin)
        mesazhi="Konveritimi i numrit "+\
                numrin+ " ne njesine "+zgjedh+\
                " eshte: "+str(result)
    elif(kerkesa.split(" ")[0]=="FAKTORIEL"):
        numri=int(kerkesa.split(" ")[1])
        p=1
        for i in range(1,numri+1):
            p=p*i
        mesazhi="Faktorieli i numrit "+str(numri)+ " eshte: "+str(p)
   
    elif(kerkesa.split(" ")[0]=="FLOATNUMBER"):
        numri=kerkesa.split(" ")[1]
        numri=str(float(numri))
        nr=numri
        numraParaPikes=str(bin(int(numri.split(".")[0])))
        numraPasPikes=""
        mbetja=0
        heresi=float("0."+numri.split(".")[1])
        for i in range(0,15):
            mbetja=int(heresi*2)
            heresi=heresi*2-mbetja
            numraPasPikes+=str(mbetja)
        if(numri>=0):
            shenja=0
        else: 
            shenja=1
        if(len(numraParaPikes)==1) and (int(numraParaPikes)==1):
            eksponenti=0
        elif(len(numraParaPikes)>1):
            eksponenti=len(numraParaPikes)-1
            numraPasPikes=numraParaPikes[1:len(numraParaPikes)]+numraPasPikes
        else:
            numri=numri*10

        eksponentiExtra=str(bin(eksponenti+127)).replace("0b","")
        zero=0
        if(len(eksponentiExtra)<8):#duhet ta shikojme
            for i in range(0,8-len(eksponentiExtra)):
                zero+=str(0)
            eksponentiExtra=zero + eksponentiExtra
        elif(len(eksponentiExtra)>8):
            print("Duhet shikuar")
        mantisa=numraPasPikes.replace("b","")
        zero=0
        mantisaExtra=""
        if(len(mantisa)<23):
            for i in range(0,23-len(mantisa)):
                mantisaExtra+="0"
            mantisaExtra=mantisa+mantisaExtra
        else:print("duhet ta shikojme")        
        mesazhi="Numri "+nr +" ne Float pointing number eshte:    "+\
            str(shenja)+" "+str(eksponentiExtra)+" "+mantisaExtra

    elif(kerkesa.split(" ")[0]=="ASCII"):
        fjala=kerkesa.split(" ")[1]
        for i in range(0,len(fjala)):
            mesazhi=mesazhi+fjala[i]+" "+str(Decimal(ord(fjala[i])))+" "+str(hex(ord(fjala[i])))+" "+str(oct(ord(fjala[i])))+"\n"
    elif(kerkesa =="POEMA"):
        from random import choice, randint

        mbiemra = "brave clam delightful faithful gentle happy old young".split()
        foljet = "wants love hears live burns brings becomes grows".split()
        emrat = "sadness life books songs picture music unicorn long happiness joy ".split()
        kryefjalet="nobody he she somebody ".split()

        def poema():
        print("The poem:")
        for i in range(0,randint(5,10)):
            print(kryefjalet[randint(0,3)]+" is "+mbiemra[randint(0,7)]+" and "+foljet[randint(0,6)]+"  "+emrat[randint(0,9)])
  
        poema()

    elif(kerkesa=="GUESS"):
        random_number = random.randint(0,100)
        #print(random_number)
        random_number
        failed_attempts=0
        x=True
        while(x==True):
            guess_number = int(input("Guess the number"))
            if(guess_number>random_number):
                print("The number you've guessed is greater than the picked one")
                failed_attempts+=1
            elif(guess_number<random_number):
                print("The number you've guessed is less than the picked one")
                failed_attempts+=1
            else:
                print("You found it !")
                x=False

            print("You tried %d"%failed_attempts+"times")
			
			
			
			
		
    elif(kerkesa=="MACA"):
	okToPressReturn = True
	hunger = 100
	day = 0

	def startGame(event): 
		global okToPressReturn
		if okToPressReturn == False:
			pass  
		else:      
			startLabel.config(text="")
			updateHunger()
			updateDay()
			updateDisplay()
			okToPressReturn = False
 
	def updateDisplay():   
		global hunger
		global day
		if hunger <= 50:
			catPic.config(image = hungryphoto)
		else:
			catPic.config(image = normalphoto)
   
		hungerLabel.config(text="Hunger: " + str(hunger))   
		dayLabel.config(text="day: " + str(day))          
		catPic.after(100, updateDisplay)
 
	def updateHunger():
		global hunger
		hunger -= 1

		if isAlive():
			hungerLabel.after(500, updateHunger)

	def updateDay():    
		global day  
		day += 1
		if isAlive():        
			dayLabel.after(5000, updateDay)

	def feed():
		global hunger
		if isAlive():
			if hunger <= 95:
				hunger += 20
			else:
				hunger -=20
        
	def isAlive():
		global hunger   
		if hunger <= 0:
			startLabel.config(text="GAME OVER! YOU KILLED HIM/HER/IT!")     
			return False
		else:
			return True
        
	root = Tkinter.Tk()
	root.title("Stay Alive!")
	root.geometry("500x300")

	startLabel = Tkinter.Label(root, text="Press 'Return' to start!", font=('Helvetica', 12))
	startLabel.pack()

	hungerLabel = Tkinter.Label(root, text="Hunger: " + str(hunger), font=('Helvetica', 12))
	hungerLabel.pack()

	dayLabel = Tkinter.Label(root, text="Day: " + str(day), font=('Helvetica', 12))
	dayLabel.pack()

	hungryphoto = Tkinter.PhotoImage(file="hungry.gif")
	normalphoto = Tkinter.PhotoImage(file="normal.gif")


	catPic = Tkinter.Label(root, image=normalphoto)
	catPic.pack()

	btnFeed = Tkinter.Button(root, text="Feed Me", command=feed)
	btnFeed.pack()
	root.bind('<Return>', startGame)
	root.mainloop()
		




    elif(kerkesa =="QUIZI"):

        operatorList = [ "+", "-", "*" ]
        print("Mire se erdhet ne Kuizin e Matematikes!")
        s = 0
        g = input("Ju lutem shkruani emrin : ")

        for i in range(10): 
             nr1 = random.randint(1,10) 
             nr2 = random.randint(1,10)
             op = random.choice(operatorList)
             
             expression = "%d %s %d" % (nr1, op, nr2) 
             answer = eval(expression) 
             print (expression, "= ???") 
             reply = int(input("Shkruani pergjigjejen tuaj : ") ) 
             if (reply == answer): 
                print ("Sakte!")
                s=s+1
             else:  
                print( "Gabim! Pergjigjeja e sakte eshte"  , answer)
        print ("Te lumte")
        print ("\n Ke qelluar  %d nga 10 " % s)


    elif(kerkesa =="REVERSE"):
        reverse(text):
        lst = []
        count = 1

        for i in range(0,len(text)):

            lst.append(text[len(text)-count])
            count += 1

        lst = ''.join(lst)
        return lst

    

    elif(kerkesa =="PERFECTNUMBER"):
      Sum = 0
      for i in range(1, Number):
        if(Number % i == 0):
            Sum = Sum + i
      if (Sum == Number):
        print(" %d eshte numer perfekt !" %Number)
      else:
        print(" %d nuk eshte numer perfekt !" %Number)





    elif(kerkesa =="THJESHTE"):
        lower = int(input("Enter lower range: "))
        upper = int(input("Enter upper range: "))

        print("Prime numbers between",lower,"and",upper,"are:")

        for num in range(lower,upper + 1):
            # prime numbers are greater than 1
            if num > 1:
                for i in range(2,num):
                    if (num % i) == 0:
                           break
                    else:
                       print(num)

    elif(kerkesa =="LARGO"):
        shenjat = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        str = input("Shkruani nje fjale qe permban shenjat e pikesimit : ")

    #largimi I shenjave te pikesimit nga fjalia
        no_punct = ""
        for char in str:
           if char not in shenjat:
               no_punct = no_punct + char

        #Paraqitja e fjales pa shenja te pikesimit
        print(no_punct)




    elif(kerkesa =="COLORGAME"):
           
            #importohet moduli per krijimin e GUI
            import tkinter
            #per gjenerimin e numrave random
            import random

            #lista e ngjyrave te mundshme
            colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
            #piket ne fillim inicializohen ne zero
            score=0
            #koha(timeleft) inicializohet ne 30 sekonda
            timeleft=30

            #funksioni I cili starton lojen
            def startGame(event):

                #nese ka ende kohe…
                if timeleft == 30:
                    #fillo countdown timer.
                    countdown()
    
        
                #thirrja e funskionit per zgjedhjen e ngjyrave
                nextColour()


            #funksioni per zgjedhjen e ngjyrave
            def nextColour():

                
                global score
                global timeleft

                #nese loja starton
                if timeleft > 0:

                    #aktivizimi I tekst box 
                    e.focus_set()

                #nese ngjyra e shtypur ne text box eshte e njejte me ngjyren e teksit
                    if e.get().lower() == colours[1].lower():
                        #rrit piket per nje
                        score += 1

                    #pasi te klikohe Enter pastohet tekst box
                    e.delete(0, tkinter.END)
                    #lista e ngjyrave ne baze random
                    random.shuffle(colours)
                   #ndryshon ngjyren , duke ndryshuar tekstin edhe ngjyren ne baze random
                    label.config(fg=str(colours[1]), text=str(colours[0]))
                    #ndrysho piket
                    scoreLabel.config(text="Score: " + str(score))
                elif timeleft==0: #nese mbaron koha (timeleft=0) at’her mbaron loja 
                    Label1 = tkinter.Label(root, text="Game Over !" , font=('Helvetica', 20))
                    Label1.pack();







    else: mesazhi="\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"+\
                "Lista e metodave eshte brenda domenes:\n"+\
                "IP\n"+"PORT\n"+"ZANORE\n"+"PRINTO\n"+"HOST\n"+"TIME\n"+\
                "KENO\n"+"Konverto\n"+"\tCelsiusToKelvin\n"+"\tCelsiusToFahrenheit\n"+\
                "\tKelvinToFahrenheit\n"+"\tKelvinToCelsius\n"+"\tFahrenheitToCelsius\n"+\
                "\tFahrenheitToKelvin\n"+"\tPoundToKilogram\n"+"\tKilogramToPound\n"+\
                "FAKTORIEL\n"+"FLOATNUMBER\n"+"ASCII\n"+\
                "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"

    print("Mesazhi i pranuar: " + mesazhi)
    serverSocket.sendto(mesazhi, clientAddress)
   





