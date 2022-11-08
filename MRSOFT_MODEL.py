# six classes, Applied inheritance, polymorphism, containment etc
try:
    class Mrsot:
        def order(self):
            print(f"... Observe laws and order ...")
        def has_students(self):
            print("... Have students ...")
        def check_in(self):
            print("... Check in ...")
        def check_out(self):
            print("... Check out ...")
        def greetings(self):
            print("... WELCOME TO MR SOFT ...")
        def build_app(self):
            print("... build apps ...")
        def teaching(self):
            print("... teach students ...")
        def hire(self):
            print("... hire ...")
        def datahosting(self):
            print("... offer hosting services  ...")
        def assignment(self):
            print('... Teachers give students assignment ...')
        def students(self):
            print('... Students ask questions ...')
        def teachers(self):
            print('... Teachers ask questions ...')
        def pay(self):
            print("... pays salaries ...")

    class Admin(Mrsot):
        def has_students(self):
            print("... Admin don't have students ...")
        def greetings(self):
            print("... WELCOME TO MR SOFT ADMIN...")
        def teaching(self):
            print("... Admin does not teach! ...")
        def build_app(self):
            print("... admins don't build apps ...")
        def datahosting(self):
            print("... Admins don't offer hosting services ...")
        def assignment(self):
            print("... Admin don't give students assignment ...")
        def students(self):
            print('... Students can only ask Admins informational questions ...')
        def teachers(self):
            print("... Teachers can only ask Admins informational questions ...")

    class Training(Admin):
        def greetings(self):
            print("... WELCOME TO MR SOFT TRAINING...")
        def hire(self):
            print("... Teachers don't hire ...")
        def students(self):
            print('... Students ask teachers question ...')
        def teachers(self):
            print('... Teachers ask students question ...')
        def datahosting(self):
            print("... Teachers don't offer hosting services ...")
        def pay(self):
            print("... Teachers don't pays salaries ...")

    class Engineering(Mrsot):
        def has_students(self):
            print("... Engineering don't have students ...")
        def greetings(self):
            print("... WELCOME TO MR SOFT ENGINEERING ...")
        def teaching(self):
            print("... engineers dont teaching students ...")
        def hire(self):
            print("... Engineers don't hiring ...")
        def assignment(self):
            print("... Engineers don't give students assignment ...")
        def students(self):
            print("... Students don't ask Engineers questions ...")
        def teachers(self):
            print("... Teachers don't ask Engineers questions ...")

    class Simulation:
        def __init__(self):
            print("MR SOFT MODEL SIMULATION PROGRAM")
            print(f"WELCOME TO MR SOFT.")
            print("Enter A for Admin, T for Training, E for Engineering else Mr_Soft.")
            department = input("Enter department: ").strip()
            # process and convert user input to match department class names and apply containment
            if department.upper() == 'A' or department.upper() == 'ADMIN':
                D = Admin()
            elif department.upper() == 'T' or department.upper() == 'TRAINING':
                D = Training()
            elif department.upper() == 'E' or department.upper() == 'ENGINEERING':
                D = Engineering()
            else:
                D = Mrsot()
            D.check_in()
            D.greetings()
            D.order()
            D.hire()
            D.build_app()
            D.teaching()
            D.datahosting()
            D.assignment()
            D.students()
            D.teachers()
            D.pay()
            D.check_out()
    Simulation()
except:
    print("Error E1")