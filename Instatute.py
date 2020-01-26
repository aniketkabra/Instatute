#Instatute

import pickle 
import time
import os
import sys
import string
import datetime
import json
import boto3
import math
import requests
import googlemaps
import sys







#write data down here
#data gets entered into a file
#file is accessed 

#variables
topicsdictionary={}
locdict={}
topicfile=open("topicfile.dat","ab+")
pickle.dump(topicsdictionary,topicfile) 
topicfile.close() 
#classes
class user:
    def __init__(self):
        self.name=""
        self.password=""
        self.gender="" 
        self.age=0
        self.profile=""
        self.location=""
        self.classestaken=0
        
    def getdata(self):
        clr()
        print("SIGNING UP".center(30))
        print("-----------------------------------------------------------------------")
        self.name=input("Please enter your name ")
        self.gender=input("Enter your gender ")
        self.age=eval(input("Enter your age "))
        self.profile=input("Enter a bit about yourself ")
        self.location=input("Enter your current location ")
        self.password=input("Enter your desired password ") 
        print("Success!".center(50))
        print("-----------------------------------------------------------------------")
    def editdata(self):
        flag=0
        while flag==0:     #to loop during invalid entry
            try:
                flag=1     #we assume no error happens by default
                clr()
                print("-------------------------------------------------------------------------------------")
                print("\t[1]NAME\t[2]PASSWORD\t[3]GENDER\n\t[4]AGE\t[5]BIO\t[6]LOCATION")
                print("-------------------------------------------------------------------------------------")
                ch=eval(input("What detail would you like to modify?[ENTER CORRESPONDING NUMBER ONLY]"))
                if ch==1:
                    self.name=input("Please enter your name")
                elif ch==2:
                    self.changepass()
                elif ch==3:
                    self.gender=input("Enter your gender")
                elif ch==4:
                    self.age=eval(input("Enter your age"))
                elif ch==5:
                    self.profile=input("Enter a bit about yourself")
                elif ch==6:
                    self.location=input("Enter your current location")
                else:
                    print("||ERROR: Invalid entry [number out of range]||")
                    flag=0     #assigned in the case of error so as to initiate whileloop
            except:       #handles invalid entry
                print("||ERROR: Invalid entry [string entered]||")
                flag=0     #assigned in the case of error so as to initiate whileloop
    def changepass(self):
        flag=0
        passkey=input("Enter your old password")
        if passkey==self.password:
            while flag==0:
                passkey=input("Enter your new password")
                passkeycheck=input("re-Enter your new password")
                if passkey==passkeycheck:
                    print("Password successfully changed")
                    self.password=passkey
                    
                    flag=1                                 #flag and loop for changing the password and ensured security
                else:
                    print("Sorry, those didnt match. Please enter them again")
                    flag=0
    def displaydata(self):
        print("USER: ", self.name)
        print("Gender:",self.gender,"\t\t","Age:",self.age,"\t\t","Location:",self.location,"\t\t","Classes:",self.classestaken,"\t\t","Bio:",self.profile,"\t\t")
        print("Class","\t\t","Location")
        for i in locdict.keys():
            print(i,"\t\t",locdict[i])

class student(user):
    def __init__(self):
        user.__init__(self)
        self.details=[self.name,self.gender,self.location,self.age,self.profile]
        self.status={}
    def getdatastud(self):
        user.getdata(self)
        self.details=[self.name,self.gender,self.location,self.age,self.profile]
    def editdata(self):
        user.editdata(self)
        self.details=[self.name,self.gender,self.location,self.age,self.profile]
    def displaydata(self):
        user.displaydata(self)
        
class teacher(user):
    
    def __init__(self):
        user.__init__(self) 
        self.topicdict={} #topics are now stored in a dictionary for both the global and the individual teacher instances 
        self.studnotif=0
        self.studdetails={} #dictionary which has the topic into which all of the student details for that given teacher are appended. 
        self.studarchive={} #dictionary into which all of the done students go into
    def getdatateach(self):
        user.getdata(self)
    def editdata(self):
        user.editdata(self)
    def displaydata(self):
        user.displaydata(self)
    def gettopicteach(self):
        status=0
        try: 
            while status==0:
                topicfile=open("topicfile.dat","rb+")
                topicfile.seek(0)
                topicsdictionary=pickle.load(topicfile)
                n=eval(input("Enter the number of subjects you want to register for")) 
                for i in range(n):
                    topic=input("Enter your topic")
                    location=input("Enter the location of you class")
                    locdict[topic]=location
                    self.topicdict[topic]=0
                    self.studdetails[topic]=[]
                    self.studarchive[topic]=[]
                    if topic in topicsdictionary: 
                        topicsdictionary[topic]+=1 
                    else:
                        topicsdictionary[topic]=1 
                topicfile.close()
                newfile=open("newtopfile.dat","ab+")
                pickle.dump(topicsdictionary,newfile)
                newfile.close()
                os.remove("topicfile.dat")
                os.rename("newtopfile.dat","topicfile.dat")
                status=1
        except EOFError:
            status=0
            topicfile.seek(0) 
    def removetopic(self):
        topicfile=open("topicfile.dat","b+")
        topicfile.seek(0)
        topicsdictionary=pickle.load(topicfile)
        for l in self.topic:
            print(l)
            
        topic=input("Enter the topic you want to remove") 
        del self.topicdict[topic]  
        print("Topic successfully removed from your custom list")
        topicsdictionary[topic]-=1
        newfile=open("newtopfile.dat","ab+")
        pickle.dump(topicsdictionary,newfile)
        os.remove("topicfile.dat")
        os.rename("newtopfile.dat","topicfile.dat") 
        topicfile.close()
    
    def displaytopics(self):
        print("Here are your topics \n")
        for t in list(self.topicdict.keys()):
            print(t)
    
    def create_studentarchive_list(self,topic,studdeetes):
        if topic in self.studarchive:
            self.studarchive[topic].append(studdeetes) 
        else: 
            self.studarchive[topic]=[]
            self.studarchive[topic].append(studdeetes)

    def create_studentdirectory_list(self,topic,studdeetes): 
        if topic in self.studdetails:
            self.studdetails[topic].append(studdeetes) 
        else: 
            self.studdetails[topic]=[]
            self.studdetails[topic].append(studdeetes)
    
    
                             

class Error:
    pass 

class colour:
   purple = '\033[95m'
   cyan = '\033[96m'
   darkcyan = '\033[36m'
   blueE = '\033[94m'
   green = '\033[92m'
   yellow = '\033[93m'
   red = '\033[91m'
   bold = '\033[1m'
   underline = '\033[4m'
   end = '\033[0m'

#functions

def clr():
    pass

def loading():
    word="LOADING..."
    for i in range(11):
        time.sleep(0.5)
        print(word[0:i], end="  ")
        
def loadingbar():
    for ch in "LOADING":
        time.sleep(0.05)
        sys.stdout.write(ch) #printing without spaces
    print() 
    

    
def stud_menu(stud):
    print("------------------------------------------------------------------------------------------------------")
    print("|| USER MENU ||".center(50)) 
    print("1. Display Personal Information\t2. Edit Personal Information") 
    print("3. Change your password\t4   . Get learning")
    print("5. Enter your answers to the most recent exam")
    print("6. Check your most recent score")
    print("7. Sign out")
    print("------------------------------------------------------------------------------------------------------")
    ch=input("Enter your desired choice (Only numbers)")
    topic=""
    if ch=="1": 
        stud.displaydata() 
    elif ch=="2":
        activefile=open("studlist.dat","rb+") 
        newfile=open("newfile.dat","ab+")
        stud1=student()
        status=0
        try: 
            while True: 
                stud1=pickle.load(activefile)
                if stud.name==stud1.name: 
                    stud1.editdata()
                    status=1
                pickle.dump(stud1,newfile)
                
        except EOFError:
            if status==1:
                print("Edited.")
            activefile.close()
            newfile.close()
        
        os.remove("studlist.dat")
        os.rename("newfile.dat","studlist.dat") 
   
    elif ch=="3":
         
        activefile=open("studlist.dat","rb+") 
        newfile=open("newfile.dat","ab+")
        stud1=student()
        status=0
        try: 
            while True: 
                stud1=pickle.load(activefile)
                if stud.name==stud1.name: 
                    stud1.changepass() 
                pickle.dump(stud1,newfile)
                
        except EOFError:
            activefile.close()
            newfile.close()
        
        os.remove("studlist.dat")
        os.rename("newfile.dat","studlist.dat")
        
    elif ch=="4":
        clr()
        print("CHOOSE YOUR DESIRED TOPIC TO CONTINUE".center(20))
        print("--------------------------------------------------")
        print("|| TOPIC LIST ||".center(40))
        topicfile=open("topicfile.dat","rb+")
        topicfile.seek(0)
        topicsdictionary=pickle.load(topicfile)        
        for t in list(topicsdictionary.keys()): 
            print(t, "\t", end=' ')
        print("\n--------------------------")
        topic=input("Enter a topic from the list") 
        if topic in list(topicsdictionary.keys()):
            logfile=open("teachlist.dat","rb+") 
            try: 
                while True: 
                    topiccheck=pickle.load(logfile) #each teacher is manually loaded
                    topiclist=list(topiccheck.topicdict.keys()) #topic list contains all the topics of the teacher
                    for i in locdict:
                        print(locdict[i])
                    if topic in topiclist:                        
                        print("-------------------------------------------------------------------")
                        topiccheck.displaydata() 
                    else: 
                        pass 
            except EOFError: 
                print("-------------------------------------------")
                
            print("CHOOSE YOUR TEACHER".center(20))
            teacher=input("Enter the name of the teacher") 
            newfile=open("newfile.dat","ab+")
            logfile.seek(0)
            try:
                while True:  #infinite loop
                    topiccheck=pickle.load(logfile)
                    teachername=topiccheck.name
                    if teachername==teacher:
                        topiccheck.create_studentdirectory_list(topic,stud.details)
                        topiccheck.studnotif+=1
                        topiccheck.classestaken+=1
                        pickle.dump(topiccheck,newfile)
                    else:
                        pickle.dump(topiccheck,newfile) #here, it solves the problem we were having of stuff not being dumped later. 
            except EOFError:
                logfile.close()
                newfile.close()
            
            os.remove("teachlist.dat")
            os.rename("newfile.dat","teachlist.dat") 
            
            topicfile.close()
            print(teacher, " has been sent a notification about your interest in ", topic , " and will get in touch with you. Sit tight, and happy learning!")
            print("---------------------------------------------------")
            
        else:
            print("Topic not available")
    elif ch=="5":
        studsols=input("Enter the solutions to the most recent exam in the same order as the questions in the question paper: ")
        studsolfiles=open('studsolfile.dat','wb+')
        pickle.dump(studsols,studsolfiles)
        
        studsolfiles.close()
        print('Submission saved successfuly')
        
    elif ch=="6":
        studsolfile=open('studsolfile.dat','rb+')
        solfile=open('solfile.dat','rb+')
        gradesdict=checking(studsolfile,solfile)
        
        for i in gradesdict:
            if i==user().name:
                print('Your score is: ', gradesdict[i])
        
    elif ch=="7":
        clr()
        main()
    
    else:
        print("Invalid input")
                             

                             
                             
                             
               
def teach_menu(teach):
    clr()
    print("|| USER MENU ||".center(30))
    notifcheck(teach)
    print("---------------------------------------------------------")
    print("1. Display Personal Information\t2. Edit Personal Information") 
    print("3. Change your password\t4. Add Topic")
    print("5. View all students\t6. Notification Check")
    print("7. Enter solutions to recent exam")
    print("8. Sign Out") 
    print("---------------------------------------------------------")
    ch=input("Enter your desired choice (Only numbers)") 
    if ch=="1": 
        teach.displaydata() 
    elif ch=="2": 
        activefile=open("teachlist.dat","rb+") 
        newfile=open("newfile.dat","ab+")
        teach1=teacher()
        status=0
        try: 
            while True: 
                teach1=pickle.load(activefile)
                if teach.name==teach1.name: 
                    teach1.editdata() 
                pickle.dump(teach1,newfile)
                
        except EOFError:
            activefile.close()
            newfile.close()
        
        os.remove("teachlist.dat")
        os.rename("newfile.dat","teachlist.dat")
        
    elif ch=="3":
        activefile=open("teachlist.dat","rb+") 
        newfile=open("newfile.dat","ab+")
        teach1=teacher()
        status=0 
        try: 
            while True: 
                teach1=pickle.load(activefile)
                if teach.name==teach1.name: 
                    teach1.changepass()  
                pickle.dump(teach1,newfile)
                
        except EOFError:
            activefile.close()
            newfile.close()
        
        os.remove("teachlist.dat")
        os.rename("newfile.dat","teachlist.dat")
    
    elif ch=="4":
        activefile=open("teachlist.dat","rb+") 
        newfile=open("newfile.dat","ab+")
        teach1=teacher()
        try: 
            while True: 
                teach1=pickle.load(activefile)
                if teach.name==teach1.name: 
                    teach1.gettopicteach()
                pickle.dump(teach1,newfile)
                
        except EOFError:
            activefile.close()
            newfile.close()
        
        os.remove("teachlist.dat")
        os.rename("newfile.dat","teachlist.dat") 
    
    elif ch=="5": 
        print("Students (By Topic)")
        activefile=open("teachlist.dat","rb+")
        teach1=teacher()
        try: 
            while True: 
                teach1=pickle.load(activefile)
                if teach1.name==teach.name:                 
                    topiclist=list(teach1.studarchive.keys()) #gets all the topics from studarchive
                    for topic in topiclist: #each topic
                        print(topic,"\n\n\n") 
                        for student in teach1.studarchive[topic]: #students accepted for each topic
                            for item in student: #details of each student accepted for each topic
                                print(item, end=' ') 
                            print() 
                        print()
        except EOFError: 
            activefile.close()
            
                        
    elif ch=="6": 
        notifcheck(teach)
    elif ch=="7":
        sols=input("Enter the solutions to the most recent exam in the same order as the questions in the question paper: ")
        solfile=open('solfile.dat','wb+')
        pickle.dump(sols,solfile)
        solfile.close()
        print('Solution saved successfuly')
            
    elif ch=="8": 
        print("Come back soon")
        main()
        
                         
def notifcheck(teach):
    activefile=open("teachlist.dat","rb+")
    teacherouterref=teacher()
    try: 
        while True: 
            teacherouterref=pickle.load(activefile)
            if teacherouterref.name==teach.name: 
                print("||",teacherouterref.name,"'s", "notifications (", teacherouterref.studnotif ,") ||")  
                if teacherouterref.studnotif>0:
                    print("\nHere are topics you have notifications for:\n")
                else:
                    print("You have no notifications")
    except EOFError: 
        pass
    activefile.close()
    notifcount=teacherouterref.studnotif
    teach1=teacher() 
    teachref=teacher() #so that for each iteration of the j loop, we get the updated teacher. 
    x=True
    while notifcount>0 and x==True: #this is for the number of students she needs to accept per notification trial.
        print("\nTopics and registered students. ")
        print("---------------------------------")
        print("\t\tNAME\t\tGENDER\t\tLOCATION\tAGE\t\tDETAILS\n")
        repcheck='Y'
        try:
            while x==True:
                newfile=open("newfile.dat","ab+") 
                activefile=open("teachlist.dat","rb+") 
                activefile.seek(0)
                teachref=pickle.load(activefile) 
                if teachref.name==teach.name: #and repcheck=='Y':         
                    for topic in list(teachref.topicdict.keys()):  #loop for display
                        print("TOPIC:", topic)
                        print("STUDENTS:\n")
                        for ch in teachref.studdetails[topic]: #loop for displaying student details
                            for i in range(5):
                                print("\t\t", ch[i], end=' ')
                            print()
                    topicname=input("Enter the name of the topic you want to teach: ") 
                    for topic in list(teachref.topicdict.keys()):  
                        if topic==topicname:
                            studname=input("Enter the name of the student you want to teach: ")
                            for char in teachref.studdetails[topic]: #FOR list of student details IN dictionary of lists of details of students, called by topic mentioned by teacher
                                if char[0]==studname: #student name matches the name entered by teacher, char[0] = name
                                    try: 
                                        activefile.seek(0)
                                        while x==True: 
                                            teach1=pickle.load(activefile) #active file is teachlist.dat
                                            if teach1.name==teachref.name: 
                                                teach1.create_studentarchive_list(topic,char) 
                                                teach1.studdetails[topic].remove(char)
                                                teach1.topicdict[topic]+=1
                                                teach1.studnotif=-1
                                                notifcount-=1
                                                print("Student accepted.")
                                                print("_________________________________________")
                                                pickle.dump(teach1,newfile)
                                                repcheck=input("Select another?[Y/N]")
                                                if repcheck.upper()=='N':
                                                    x=False
                                            else:
                                                pickle.dump(teach1,newfile)
                                    except EOFError: 
                                        pass


                activefile.close()
                newfile.close()
                os.remove("teachlist.dat")
                os.rename("newfile.dat","teachlist.dat")


                
        except EOFError: 
            activefile.close() 
            newfile.close()

            os.remove("teachlist.dat")
            os.rename("newfile.dat","teachlist.dat")
            
        
                    
                 
                        
def solvals(sol):
    client = boto3.client('comprehend')
    r = client.detect_key_phrases(
    Text=sol,
    LanguageCode='en')
    scrs=r['KeyPhrases']
    scr=[]
    for i in range(len(scrs)):
        #print(scrs[i])
        scr.append(scrs[i]['Score'])
    scorelist=scr
    txt=[]
    for i in range(len(scrs)):
        #print(scrs[i])
        txt.append(scrs[i]['Text'])
    txtlist=txt
    #print(scorelist,txtlist)
    return scorelist,txtlist
def studvals(studans):
    client = boto3.client('comprehend')
    res = client.detect_key_phrases(
    Text=studans,
    LanguageCode='en')
    scrss=res['KeyPhrases']
    sc=[]
    for i in range(len(scrss)):
        #print(scrs[i])
        sc.append(scrss[i]['Score'])
    studscorelist=sc
    txts=[]
    for i in range(len(scrss)):
        #print(scrs[i])
        txts.append(scrss[i]['Text'])
    studtxtlist=txts
    #print(studscorelist,studtxtlist)
    return studscorelist,studtxtlist
                        
def checking(studsolfile,solfile):
    studsolfiles=open('studsolfile.dat','rb+')
    studans=pickle.load(studsolfiles)
    studsolfiles.close()
    studscorelist,studtxtlist=studvals(studans)
    solfiles=open('solfile.dat','rb+')
    sols=pickle.load(solfiles)
    solfiles.close()
    scorelist,txtlist=solvals(sols)
    if len(studscorelist)!=len(scorelist):
        finalscore=0
    else:
        for i in range(len(studscorelist)):
           if abs(studscorelist[i]-scorelist[i])<0.05:
               finalscore=100
           elif abs(studscorelist[i]-scorelist[i])>0.05 and abs(studscorelist[i]-scorelist[i])<0.07 :
                finalscore=50
           if abs(studscorelist[i]-scorelist[i])==0:
                finalscore=0
        
    gradesdict={}
    stud=user()
    studname=stud.name
    gradesdict[studname]=finalscore
    return gradesdict
        
    
    

    
def userentry():
    returnflag=False
    while True:
        clr()
        print("--------------------------------------------")
        print("1. I am a student")
        print("2. I am a teacher")
        print("3. Return to Main Menu")
        print("--------------------------------------------")
        ch1=eval(input("Choose an option:"))
        if ch1==1:
            print("\nWelcome to Instatute, Student!")
            loadingbar()
            time.sleep(1)
            break
        elif ch1==2:
            print("\nWelcome to Instatute, Teacher!")
            loadingbar()
            time.sleep(1)
            break
        elif ch1==3:
            returnflag=True
            break
        else:
            print("Invalid entry, try again.")
            time.sleep(1)
            print("Redirecting now")
            time.sleep(1)
            clr()
    if returnflag==True:
        clr()
        main()
            

    clr()
    print("---------------------------------------------------------------------")
    print("1.Sign in")
    print("2.Sign up")
    print("---------------------------------------------------------------------")
    
    ch=input("Enter your choice in numbers only") 
    if ch=="1": #for signing in
        if ch1==1: #student 
            logfile= open("studlist.dat", "rb+")
            while True:
                try:
                    name=input("Enter your name")
                    password=input("Enter your password")
                    logfile.seek(0) 

                    while True:
                        stud=pickle.load(logfile) 
                        if stud.name==name and stud.password==password:
                            print("Success!")
                            print("Welcome, ", stud.name) 
                            logfile.close() 
                            while True:
                                stud_menu(stud)
                except EOFError:
                    print("User not found in our database. Try again? [Y/N]")
                    ch3=input('Choice:')
                    if ch3.upper()=='Y':
                        continue
                    elif ch3.upper()=='N':
                        break
                    else:
                        print("Invalid input//returning to main menu")
                        break
                    
        elif ch1==2:
            logfile= open("teachlist.dat", "rb+")
            logfile.seek(0)
            while True:
                name=input("Enter your name")
                password=input("Enter your password")
                logfile.seek(0)
                try: 
                    while True:
                        teach=pickle.load(logfile) 
                        if teach.name==name and teach.password==password:        
                            print("\n\nSuccess!")
                            print("Welcome, ", teach.name) 
                            logfile.close()
                            while True:
                                teach_menu(teach)
                except EOFError:
                    print("User not found in our database. Try again? [Y/N]") 
                    ch3=input('Choice:')
                    if ch3.upper()=='Y':
                        continue
                    elif ch3.upper()=='N':
                        break
                    else:
                        print("Invalid input//returning to main menu")
                        break
                    
                logfile.close()         
    if ch=="2":
        if ch1==1:
            newuser=student()
            newuser.getdatastud()
            logfile=open("studlist.dat", "ab+")
            pickle.dump(newuser,logfile)
            logfile.close()
        elif ch1==2:
            newuser=teacher()
            newuser.getdatateach()
            newuser.gettopicteach()
            logfile=open("teachlist.dat", "ab+")
            pickle.dump(newuser,logfile)
            logfile.close()


def distcalc():
    subl=[]
    bt=[]
    et=[]
    locl=[]
    t_times=[]
    n=int(input("Enter the number of classes you are taking: "))
    for i in range(n):
        sub=input("Enter the subject: ")
        subl.append(sub)
        begin=input("Enter the time you class begins (in hrs): ")
        bt.append(int(begin[0:2]))
        end=input("Enter the time your class ends (in hrs): ")
        et.append(int(end[0:2]))
        loc=input("Enter location of your class: ")
        locl.append(loc)
    gap = []
    for i in range(len(bt)-1):
        time = abs((bt[i+1]-et[i]))
        gap.append(time)
    
                  
    for k in range(0,(len(locl)-1)):
        originPoint=locl[k]
        destinationPoint=locl[k+1]
#Place your google map API_KEY to a variable
        apiKey='AIzaSyCtWQVnbo6nNDBtoQ6BRGSVsb0lh2vMWH8'
#Store google maps api url in a variable
        url='https://maps.googleapis.com/maps/api/distancematrix/json?'
# call get method of request module and store respose object
        r = requests.get(url+'origins='+originPoint+'&destinations='+destinationPoint+'&key='+apiKey)
#Get json format result from the above response object
        res=r.json()
#print the value of res
        x=res
        z=x['rows'][0]['elements'][0]['duration']['text']
       # for char in z:
            
        t_times.append(int(z[0:2]))
    #print(type(t_times[0])) 
    for calc in range(len(gap)):
        if (gap[calc])<((int(t_times[calc])-int(20/60))):
            print( "Not a recomended schedule. Try rescheduling :(")
        elif (gap[calc])>((int(t_times[calc])-int(20/60))):

            print("You are all set. Perfect schedule :)")
    #return result
        
    
        
    
    
def main():
    while True:
        print("-------------------------------------------------------------------")

        print("""  _____ _   _  _____ _______    _______ _    _ _______ ______ 
 |_   _| \ | |/ ____|__   __|/\|__   __| |  | |__   __|  ____|
   | | |  \| | (___    | |  /  \  | |  | |  | |  | |  | |__   
   | | | . ` |\___ \   | | / /\ \ | |  | |  | |  | |  |  __|  
  _| |_| |\  |____) |  | |/ ____ \| |  | |__| |  | |  | |____ 
 |_____|_| \_|_____/   |_/_/    \_\_|   \____/   |_|  |______|
                                                              
                                                              """.center(50))

        print("----------------------------MAIN MENU------------------------------")
        print("1.ACCESS SERVICE".center(65))
        print("2.ABOUT US".center(65))
        print("3. Check you schedule".center(65))
        print("4.QUIT".center(65))
        print("-------------------------------------------------------------------------------")
        ch=input("Enter your choice ")
        if ch.upper()=="1":
             userentry()
        elif ch.upper()=="ABOUT US" or ch=="2":    
            print("\t\t\t\t\t\t\tMASTHEAD\t\t\t\t\t\t\t")
            print("Instatute is an online platform for students to get matched to their teachers via one medium: topics. It is a pathbreaking innovation in technology and education, and now, you are a part of it. \n\n\n\n \n\n\n\n\n\n\n","Founders\n\n Laksh Anand (Chief Executive Officer)(#0)\n\n Aniket Kabra (Chief Technology Officer)(#1)\n\n Joseph Nagel (President, Innovations)(#6)\n\n Joseph Nagel (President, Public Relations)(#7)\n\n\n Original Members \n\n\n Laksh Anand (President, Design)(#3)\n\n Aniket Kabra (President, Research)(#4)\n\n Joseph Nagel (Chief Financial Officer)(#5) \n".center(50), end=' ')
        elif ch.upper()=="3":
            distcalc()
            
            
            
        elif ch.upper()=="QUIT" or ch=="4":
            print("THANK YOU FOR VISITING INSTATUTE. HOPE WE FULFILLED YOUR EVERY INSTANEED") 
            exit() 
        else: 
            print("Wrong choice. You might want to try again") 


main()


