
import random
class About_training:
    def __init__(self):
        print("TRAINING:")
        print("""We offer standardized and customized Information and Communications Technology related training programmes 
for individuals and organisations. Our walk-in training programmes for individuals are currently physical and are 
offered at our corporate head office. Our corporate trainings are designed to suit the preference of customers and 
are offered on and off customer’s location. The areas covered by our courses and training programmes include desktop 
publishing, software development/ programming, website design/development, digital marketing, hardware repairs and 
networking. We also offer a specialized bouquet of training leading to the award of the International Computer 
Driving License.""")
        Readmore.querry_readmore(self)

class About_engineering:
    def __init__(self):
        print("""we design and develop computer software to meet the needs of individuals, private organisations and 
public institutions. These solutions are designed to manage their several databases, make their business 
operations more efficient, make their reporting function more value added and their decision making process 
real-time. Other features of our solutions provide our clients with the ability to monitor their business activities 
remotely and real-time. Included in our bouquet of software solutions are e-commerce platforms, database management 
systems, leaning management systems, business enterprise solutions, communication and mobile applications.
        
        """)
        Readmore.querry_readmore(self)

class Training:
    def __init__(self, name: str, department: str, role: str):
        self.name=name
        self.department=department
        self.role=role
        if  self.role.upper() == 'T' or self.role.upper() == 'TEACHER':
            print(f"WELCOME TO THE TRAINING DEPARTMENT, TEACHER {self.name.upper()}  ")
            Training.takeclass(self, 1)
        elif  self.role.upper() == 'ST' or self.role.upper() == 'STUDENT':
            print(f"WELCOME TO THE TRAINING DEPARTMENT, {self.name.upper()}  ")
            Training.toclass(self, 1)

    def teaching(self, num):
        """Teaching simulation"""
        self.num=num
        print("... You have entered a 2hrs class ...")
        print("... A teacher is teaching ...")
        print("Our topic for today is ...")
        print("...class well in progress...")
        print("... Students taking notes ...")
        q=input("Do you have a question? Enter Yes or No: ")
        if q.upper() =="Y" or q.upper()=='YES':
            while q.upper() == "Y" or q.upper()=="YES":
                print(f"Teacher@{self.name}: Please ask your question.")
                print(f"...{self.name} asked question:...?")
                print(f"...Teacher answers question...")
                q = input("Do you have another question? Teacher asked, Enter Yes or No: ")
                if q.upper() =="N" or q.upper()=='NO':
                    q="NO"
        print("...class continues...")
        print("...class well in progress...")
        print("...class reaching end time...")
        print("...class ends...")
        print(f"{self.name} you...")
        self.num = self.num + 1
        Training.toclass(self, self.num)


    def teaching_teacher(self, num):
        """Teaching simulation"""
        self.num=num
        print(f"... {self.name}, taking a 2hrs class ...")
        print(f"... {self.name} is teaching ...")
        print("Our topic for today is ...")
        print("...class well in progress...")
        print("... Students taking notes ...")
        q='yes'
        while q.upper() == "Y" or q.upper()=="YES":
            print("I have a question Sir ...")
            print(f"{self.name}@student: Please ask your question.")
            print(f"...Student asked question:...?")
            print(f"... {self.name} answers question...")
            #use a random number to determine if a sudent has another question or not
            list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            rand=random.choice(list1)
            if rand >=5:
                q="NO"
            else:
                q="YES"

        print("...class continues...")
        print("...class well in progress...")
        print("...class reaching end time...")
        print("...class ends...")

        self.num = self.num + 1
        Training.toclass(self, self.num)

    def takeclass(self, num):
        self.num=num
        while self.num < 3:
            q = input(f"Time for {self.num} class is here, will you take it? Enter Yes or No: ")
            if q.upper() == "Y" or q.upper() == 'YES':
                Training.teaching_teacher(self, num)
            else:
                num=num+1
                print(f"class skipped")
        else:
            q = input(f"Class is over for today, Would you like to go home? Enter Yes or No: ")
            if q.upper() == "Y" or q.upper() == 'YES':
                MrSoft.sighnout(self)
            else:
                q = input(f"Would you like to read? Enter Yes or No: ")
                if q.upper() == "Y" or q.upper() == 'YES':
                    Training.studentreading(self)
                else:
                    Training.studentchatting(self)

    def toclass(self, num):
        self.num=num
        while self.num < 2:
            q = input(f"Time for {self.num} class is here, will you join? Enter Yes or No: ")
            if q.upper() == "Y" or q.upper() == 'YES':
                Training.teaching(self, num)
            else:
                num=num+1
                print(f"class skipped")
        else:
            q = input(f"Class is over for today, Would you like to go home? Enter Yes or No: ")
            if q.upper() == "Y" or q.upper() == 'YES':
                MrSoft.sighnout(self)
            else:
                q = input(f"Would you like to read? Enter Yes or No: ")
                if q.upper() == "Y" or q.upper() == 'YES':
                    Training.studentreading(self)
                else:
                    Training.studentchatting(self)




    def requestgohome(self):
        q = input(f"Would you like to go home? Enter Yes if you want to: ")
        if q.upper() == "Y" or q.upper() == 'YES':
            MrSoft.sighnout(self)
        else:
            print(f"... {self.name.title()}, Hanging around ...")
            Training.requestgohome(self)

    def confamgohome(self):
        q = input(f"Would you like to go home? Enter Yes if you want to: ")
        if q.upper() == "Y" or q.upper() == 'YES':
            MrSoft.sighnout()(self)
        else:
            print(f"... {self.name.title()}, Hanging around ...")
            Training.requestgohome(self)


    def studentchatting(self):
        print(f"... {self.name.upper()} CHATTING ...?")
        Training.requestgohome(self)
    def studentreading(self):
        print(f"... {self.name.upper()} READING...?")
        Training.requestgohome(self)




class Visiting:
    def __init__(self, name: str, department: str, role: str):
        self.name=name
        self.department=department
        self.role=role
        print(f"WELCOME TO MR SOFT RECEPTION HALL, {self.name.upper()}  ")
        print("I am Onome, Please how may i help you.")
        print(f"... ONOME INITIATING CONVERSATION ...")
        respond=input(f"Would you like to interact with Onome? Enter yes or no: ")
        if respond.upper()=="YES" or respond.upper()=="Y":
            print(f"... {self.name} interacting with Onome ...")
            respond = input(f"Enter yes when you are done interacting with Onome: ")
            if respond.upper()=="Y" or  respond.upper()=="YES":
                Training.requestgohome(self)


class SoftwareEng:
    def __init__(self, name: str, department: str, role: str):
        self.name=name
        print("WELCOME TO MR SOFT ENGINEERING DEPARTMENT")
        print("... Here is your assignment for today ...")
        print(f"... {self.name} working ...")
        print(f"... {self.name} writing programs ...")
        print(f"... {self.name} developing codes ...")
        Work_in_progress(self.name)


class Work_in_progress:
    def __init__(self, name):
        self.name=name
        w='on'
        while w == "on":
            respond = input(f"Enter yes or y when you are done working for the day: ")
            if respond.upper() == "Y" or respond.upper() == "YES":
                w='off'
                Training.requestgohome(self)
            else:
                print(f"... {self.name} working ...")

class Webapp:
     def __init__(self):
         print("WEB DEVELOPMENT.")
         print("""We build highly responsive web applications using state-of-the-art technologies 
tomeet the strategic needs of individuals, private organisation and public institutions. 
We’ve got the tools and expertise to help you create an intuitive and engaging user experience 
that your customers will enjoy. Using industry best practices, we ensure your website, 
critical network infrastructure and systems are secured at all times.
        
        \n""")
         Readmore.querry_readmore(self)


class Admin:
    def __init__(self, name: str, department: str, role: str):
        self.name=name
        self.department=department
        self.role=role
        print("WELCOME TO MR SOFT ADMINISTRATIVE HALL")
        print("... Here is your assignment for today ...")
        print(f"... {self.name} working ...")
        print(f"... {self.name} work progress ...")
        print(f"... {self.name} tending to issues ...")
        Work_in_progress(self.name)


class MrSoft:
    def __init__(self, name: str, department: str, role: str):
        self.name=name
        self.department=department
        self.role=role
        #action
        if self.department.upper()=='A' or self.department.upper()=='ADMIN':
            self.department="Admin"
            if self.role.upper() == 'V' or self.role.upper() == 'VISITING':
                #see receptionist
                Visiting(self.name, self.department, self.role)
            else:
                #go to admin's main office hall
                Admin(self.name, self.department, self.role)
        elif self.department.upper()=='T' or self.department.upper()=='TRAINING':
            if self.role.upper() == 'T' or self.role.upper() == 'TEACHER' or  self.role.upper() == 'ST' or self.role.upper() == 'STUDENT':
                # you are a teacher/student, to class
                self.department = "Training"
                Training(self.name, self.department, self.role)

            elif self.role.upper() == 'S' or self.role.upper() == 'STAFF':
                # you are a staff, do staff work
                Admin(self.name, self.department, self.role)
            else:
                #you are a visitor
                print('... VISITORS ARE NOT ALLOWED INTO THE CLASS ...')
                print('... BACK TO RECEPTION ...')
                Visiting(self.name, self.department, self.role)


        elif self.department.upper()=='S' or self.department.upper()=='SOFTWARE DESIGN':
            self.department = "Software Design"
            SoftwareEng(self.name, self.department, self.role)

    def sighnout(self):
        print(f"... {self.name.upper()} SIGNING OUT ...")
        print(f"... Bye, {self.name.title()} going home ...\n")
        MrSoft.finish(self)
    def back(self):
        MrSoft.readmore(self)

    def finish(self):
        print("HOME.")
    def about(self):
        print("""ABOUT US: 
M-R International is a world-class technological hub for 
the design and delivery of innovative ICT solutions.\n""")

    def ourservices(self):
        print("OUR SERVICES:")
        print("""Web Development, Software Development, Training, Data Center and Hosting and Internet Services Provider
        \n""")

    def contact(self):
        print("CONTACT US:")
        print("""MRsoft Technology Complex, Plot 3 Road 1, Centenary Garden Estate, 
eneka Link Road, Off G.U. Ake Road, Port Harcourt, Rivers State. Nigeria.
Website: www.m-rinternational.com
Email: enquiries@m-rinternational.com
Tel. No: +(234) 810 1162 767")\n""")

    def signin(self):
        signin = input("Would you like to signin? Enter Yes or No: ")
        if signin.upper() == 'YES' or signin.upper() == 'Y':
            Get_in(name)
        else:
            print("... THANK YOU FOR THINKING GOOD ABOUT MR SOFT ...")
            print("... We hop to hear from you soon ...")


    def readmore(self):
        choice=input("Would you like to know more about our service? Enter Yes or No: ")
        if choice.upper()=='YES' or choice.upper()=='Y':
            Readmore()
        else:
            MrSoft.signin(self)



class Get_in:
    def __init__(self, name):
        self.name=name
        print("For Department Enter A for Admin, T for Training, S for software design ")
        department = input("Enter department: ").strip()
        print("For Role Enter S for Staff, T for teacher, ST for student or V for visiting")
        role = input('enter role: ').strip()
        print(f"... {self.name.upper()} SIGNING IN ...")
        MrSoft(self.name, department, role)


class Internet_service:
    def __init__(self):
        print("Internet Services Provider:")
        print("""our fixed wireless internet service provides clients with a 24hours, unlimited, secured and 
    high speed Internet connectivity at low cost. It is suitable for individual and small group users 
    who are located within a close geographical location. With our wireless service groups and 
    individuals can cut down on their monthly internet access cost without the acquisition of additional equipment.
        
        """)
        Readmore.querry_readmore()



class Data_cener:
    def __init__(self):
        print(""""Data Center and Hosting:
    We have a well-equipped data center in a safe and secured environment with uninterrupted power supply. 
    We are equipped and able to offer data storage and hosting services to individuals, non-profit, 
    small and medium scale enterprise and large corporation. Our hosting services are ideal, 
    affordable and available providing the needed backup for saved data. 
    
    """)
        Readmore.querry_readmore(self)

class Readmore:
    def __init__(self):
        print("Enter W for Web Development, S for Software Development, T for Training, D for Data Center and Hosting and I for Internet Services Provider")
        self.reader = input("Enter service of interest: ").strip()
        if self.reader.upper() == "W":
            Webapp()
        elif  self.reader.upper() == "S":
            About_engineering()
        elif  self.reader.upper() == "T":
            About_training()
        elif  self.reader.upper() == "D":
            Data_cener()
        elif  self.reader.upper() == "I":
            Internet_service()
    def querry_readmore(self):
        self.reader = input("Enter yes to read more and no finish: ").strip()
        if self.reader.upper() == "Y" or self.reader.upper() == "Y":
            Readmore()
        else:
            print('Done reading.')
            print('... GOING HOME ...')
            MrSoft.finish(self)

class Mrsoft_online:
    def __init__(self, name: str):
        self.name=name
        MrSoft.about(self.name)
        MrSoft.ourservices(self.name)
        MrSoft.readmore(self.name)


print("MR SOFT MODEL SIMULAION PROGRAM")
print("... HELLOW WORLD! ...")
name = input("Enter your name: ").strip()
print(f"IT'S A NEW DAY, {name.upper()}.")
MrSoft.finish(name)
print(f"... {name.upper()}, THINKING, MR SOFT ...")
print("Would you like to read about MR SOFT online or get to MR_soft office?")
th = input(" Enter yes or y to read online and g or go to get to MR_soft office, else you are done: ").strip()
if th.upper() == "Y" or th.upper() == "YES":
    print(f"... {name.upper()}, BROWSING THE INTERNET ...")
    print(f"... {name.upper()}, on Website: www.m-rinternational.com ...")
    Mrsoft_online(name)
elif th.upper() == "G" or th.upper() == "GO":
    Get_in(name)
else:
    print('Done with MR soft today.')
    print('... GOING TO SOMETHING ELSE ...')





