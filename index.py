from tkinter import *
import pymysql
#print (dir())

def Login ():
	X = Luser.get ()
	Y = Lpwd.get ()
	conobj = pymysql.connect(host='localhost', user="root", password='')
	curobj = conobj.cursor()
	curobj.execute('use cspyproject;')
	test= f'select * from newuser uid ="{X}" and pwd= "{Y}";'
	curobj.execute(test)
	record =curobj.fetchall()
	if len (record):
		print("welcome to homepage")
		guiWindow =Tk()
		guiWindow.geometry("1000x430")
		guiWindow.title("Shakti - Quiz Portal")
		class myQuiz:
			def __init__(self):
				self.quesNumber=0
				self.displayTitle()
				self.displayQuestion()
				self.optSelected=IntVar()
				self.options=self.radioButtons()
				self.displayOptions()
				self.buttons()
				self.dataSize=len(question)
				x=len(question)
				self.rightAnswer=0
		def displayResult(self):
			wrongCount=self.dataSize-self.rightAnswer
			rightAnswer=f"Correct:{self.rightAnswer}"
			wrongAnswer=f"Wrong: {wrongCount}"
			the_score=int(self.rightAnswer/self.dataSize*100)
			the_result=f"score:{the_score}%"
			mb.showinfo("Result",f"{the_result} \n{wrongAnswer}")
			def checkAnswer(self,quesNumber):
				if self.optSelected.get()== answer[quesnumber]:
					return True
		def nextButton(self):
			if self.checkAnswer(self.quesNumber):
				self.rightAnswer +=1
			self.quesNumber+=1
			if self.quesNumber==self.dataSize:
				self.displayResult()
				guiWindow.destroy()
			else:
				self.displayQuestion()
				self.displayOptions()

		def buttons (self):
			next_button=Button(guiWindow,text="Next",command=self.nextButton,width=10,bg="red",fg="white",font=("ariel",16,"bold"))
			next_button.place(x=350,y=380)
			quit_button=Button(guiWindow,text="Quit", command=guiWindow.destroy,width=10,bg="red",fg="white",font=("ariel",16,"bold"))
			quit_button.place(x=500,y=380)
		def displayOptions(self):
			val=0
			self.optSelected.set(0)
			for opt in opts[self.quesNumber]:
				self.options[val]['text'==opt]
				val+=1
	else:
		print("try again")

print ("login user name=",X,"Login Password=",Y)

def Exit():
	win.destroy ()

def NewUser():

	win1=Tk()
	def submit():
		a=fname.get()
		b=lname.get()
		c=uid.get()
		d=gender.get()
		e=pwd.get()
		#print(a,b,c,d,e)
		conobj=pymysql.connect(host='localhost',user="root",password='')
		curobj=conobj.cursor ()
		curobj.execute('use cspyproject;')
		r='insert into newuser values ("{fname}","{lname}","{uid}","{gender}","{pwd}");'
		r1=r.format(fname=a,lname=b,uid=c,gender=d,pwd=e)
		curobj.execute(r1)
		conobj.commit()
		curobj.close()
		conobj.close()
		win1.destroy()

		
	def close():
		win1.destroy()
	win1.title("SignUp Page")
    
	win1.geometry('900x400')
	win1.maxsize(700,700)
	win1.minsize(700,700)

	Label(win1,text="please Sign Up Here",font=("Bell MT",20),bg="yellow",fg="red",width="35",height="2").place(x=100,y=50)

	Label(win1,text="Enter First Name",font=("Bell MT",15),bg="blue",fg="white",width="20",height="1").place(x=100,y=150)
	fname= Entry(win1,font=("Bell MT",15),bg="white",fg="black")
	fname.place(x=410,y=150)

	Label(win1,text="Enter Last Name",font=("Bell MT",15),bg="blue",fg="white",width="20",height="1").place(x=100,y=250)
	lname= Entry(win1,font=("Bell MT",15),bg="white",fg="black")
	lname.place(x=410,y=250)

	Label(win1,text="Enter User ID",font=("Bell MT",15),bg="blue",fg="white",width="20",height="1").place(x=100,y=350)
	uid= Entry(win1,font=("Bell MT",15),bg="white",fg="black")
	uid.place(x=410,y=350)

	Label(win1,text="Select Gender",font=("Bell MT",15),bg="blue",fg="white",width="20",height="1").place(x=100,y=450)
	gender= Entry(win1,font=("Bell MT",15),bg="white",fg="black")
	gender.place(x=410,y=450)

	Label(win1,text="Set New Password",font=("Bell MT",15),bg="blue",fg="white",width="20",height="1").place(x=100,y=550)
	pwd= Entry(win1,font=("Bell MT",15),bg="white",fg="black")
	pwd.place(x=410,y=550)

	submit=Button(win1,text="submit",font=("Bell  MT" , 15),bg="blue",fg="white",command=submit).place(x=250,y=600)
	close = Button(win1, text="close", font=("Bell  MT" , 15), bg="red", fg="white",command=close).place(x=370, y=600)
	win1.mainloop()

win=Tk()  #win is object of TK ()

win.title("home page!!!")

win.geometry("900x400")
win.maxsize(700,700)
win.minsize(700,700)

Label(win,text="please Login Here",font=("Bell MT",20),bg="yellow",fg="red",width="35",height="2").place(x=100,y=200)

Label(win,text="Enter User Id/Regno",font=("Bell MT",15),bg="aqua",fg="black",width="20",height="1").place(x=110,y=300)

Luser= Entry(win,font=("Bell MT",15),bg="white",fg="black")
Luser.place(x=410,y=300)

Label(win,text="Enter User Password",font=("Bell MT",15),bg="blue",fg="white",width="20",height="1").place(x=110,y=350)

Lpwd= Entry(win,font=("Bell MT",15),bg="white",fg="black",show="*")
Lpwd.place(x=410,y=350)

Button (win,text="Login",font=("Bell MT",10),bg="red",fg="black",width= 15,height= 2,command = Login).place(x=130,y=450)
Button (win,text="Exit",font=("Bell MT",10),bg="red",fg="black",width= 15,height= 2,command = Exit).place(x=280,y=450)

Button (win,text="SignUp",font=("Bell MT",10),bg="lightgreen",fg="black",width= 15,height= 2,command = NewUser).place(x=420,y=450)


win.mainloop()
