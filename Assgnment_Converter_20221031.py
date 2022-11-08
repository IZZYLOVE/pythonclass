try:
    # A unit converter program limited to temperature and length
    # Five classes, Applied containment, inheritance, polymorphism, error handling etc
    class Notice:
        def head(self):
            print("UNIT CONVERTER (TEMPERATURE AND LENGTH)")
        def terminate(self):
            print("... PROCESS TERMINATED! ...")
        def processing(self):
            print("... PROCESSING ...")
        def done(self):
            print("... DONE ...")
        def acceptedtempx(self):
            Acceptedtemp = ['CELCIUS', 'CELCIUS(C)', 'C', 'FAHRENHEIT', 'FAHRENHEIT(F)', 'F', 'KELVIN', 'KELVIN(K)',
                            'K', 'RANKINE', 'RANKINE(R)', 'R']
            return Acceptedtemp
        def acceptedlengthx(self):
            Acceptedlength = ['METER', 'METER(M)', 'M', 'CENTIMETER', 'CENTIMETER(CM)', 'CM', 'FEET', 'FEET(FT)', 'FT',
                              'INCH', 'INCH(")', '"']
            return Acceptedlength
    class Temp_driver(Notice):
        def __init__(self, *args):
            args = args
            lenargs = len(args)
            if lenargs > 3 or lenargs < 3:
                print("Please enter only three parameters!")
                check_args = 'no'
            else: # catch the first two parameters that a naturally strings
                self.fromx = str(args[0]).upper()
                self.to = str(args[1]).upper()
                check_args = 'ok'
            try:# check if the last parameter is a number
                self.value = float(args[2])
            except:
                print('the last parameter should be a number')
                check_args = 'no'
            if check_args=='ok':
                pass
        def head(self):# applying polymorphism on the head method
            print("... CONVERTING TEMPERATURE ...")
        # Using methods names that matches the method names that will be generated/derived below from user inputs to create methods
        def c_to_f(self):
            C = self.value
            f = (C * (9 / 5)) + 32
            print(f"{C} degree Celcius = {f} degree Fahrenheit"), Notice.done(self)
        def c_to_k(self):
            C = self.value
            k = C + 273.15
            print(f"{C} degree Celcius = {k} degree Kelvin"), Notice.done(self)
        def c_to_r(self):
            C = self.value
            r = C + 273.15
            print(f"{C} degree Celcius = {r} degree Rankine"), Notice.done(self)
        def r_to_f(self):
            r = self.value
            f = r - 459.67
            print(f"{r} degree Rankine = {f} degree Fahrenheit"), Notice.done(self)
        def r_to_k(self):
            r = self.value
            k = r * (5 / 9)
            print(f"{r} degree Rankine = {k} degree Kelvin"), Notice.done(self)
        def f_to_c(self):
            f = self.value
            c = (f - 32) * (5 / 9)
            print(f"{f} degree Fahrenheit = {c} degree Celcius"), Notice.done(self)
        def f_to_k(self):
            f = self.value
            k = (f + 459.69) * (5 / 9)
            print(f"{f} degree Fahrenheit = {k} degree Kelvin"), Notice.done(self)
        def f_to_r(self):
            f = self.value
            r = (f + 459.69)
            print(f"{f} degree Fahrenheit = {r} degree Rankine"), Notice.done(self)
        def k_to_f(self):
            k = self.value
            f = (k * (9 / 5)) - 459.67
            print(f"{f} degree Kelvin  = {k} degree Fahrenheit"), Notice.done(self)
        def k_to_r(self):
            k = self.value
            r = k * (9 / 5)
            print(f"{k} degree Kelvin = {r} degree Rankine"), Notice.done(self)
        def k_to_c(self):
            k = self.value
            c = k - 273.15
            print(f"{k} degree Kelvin = {c} degree Celcius"), Notice.done(self)
        def exe(self):
            self.A = self.B = ''
            Temp_driver.head(self)
            # processing and converting the different allowed user input into a preferred variable and value
            if self.fromx.upper() == 'FAHRENHEIT' or self.fromx.upper() == 'FAHRENHEIT(F)' or self.fromx.upper() == 'F':
                self.A = 'f'
            elif self.fromx.upper() == 'CELCIUS' or self.fromx.upper() == 'CELCIUS(C)' or self.fromx.upper() == 'C':
                self.A = 'c'
            elif self.fromx.upper() == 'KELVIN' or self.fromx.upper() == 'KELVIN(K)' or self.fromx.upper() == 'K':
                self.A = 'k'
            elif self.fromx.upper() == 'RANKINE' or self.fromx.upper() == 'RANKINE(R)' or self.fromx.upper() == 'R':
                self.A = 'r'

            if self.to.upper() == 'FAHRENHEIT' or self.to.upper() == 'FAHRENHEIT(F)' or self.to.upper() == 'F':
                self.B = 'f'
            elif self.to.upper() == 'CELCIUS' or self.to.upper() == 'CELCIUS(C)' or self.to.upper() == 'C':
                self.B = 'c'
            elif self.to.upper() == 'KELVIN' or self.to.upper() == 'KELVIN(K)' or self.to.upper() == 'K':
                self.B = 'k'
            elif self.to.upper() == 'RANKINE' or self.to.upper() == 'RANKINE(R)' or self.to.upper() == 'R':
                self.B = 'r'
            # using the above derived variables to determine which conversion method to call
            if F'{self.A}_to_{self.B}' == 'r_to_f':
                Temp_driver.r_to_f(self)
            elif F'{self.A}_to_{self.B}' == 'r_to_k':
                Temp_driver.r_to_k(self)
            elif F'{self.A}_to_{self.B}' == 'c_to_f':
                Temp_driver.c_to_f(self)
            elif F'{self.A}_to_{self.B}' == 'c_to_k':
                Temp_driver.c_to_k(self)
            elif F'{self.A}_to_{self.B}' == 'c_to_r':
                Temp_driver.c_to_r(self)
            elif F'{self.A}_to_{self.B}' == 'f_to_c':
                Temp_driver.f_to_c(self)
            elif F'{self.A}_to_{self.B}' == 'f_to_k':
                Temp_driver.f_to_k(self)
            elif F'{self.A}_to_{self.B}' == 'f_to_r':
                Temp_driver.f_to_r(self)
            elif F'{self.A}_to_{self.B}' == 'k_to_f':
                Temp_driver.k_to_f(self)
            elif F'{self.A}_to_{self.B}' == 'k_to_r':
                Temp_driver.k_to_r(self)
            elif F'{self.A}_to_{self.B}' == 'r_to_f':
                Temp_driver.r_to_f(self)
            elif F'{self.A}_to_{self.B}' == 'k_to_c':
                Temp_driver.k_to_c(self)
            elif F'{self.A}_to_{self.B}' == F'{self.A}_to_{self.B}':
                print('CONVERTING TO SAME UNITE')
                print(f'Convertion, {self.value}{self.fromx} = {self.value}{self.to}')
    class Lenght_driver(Notice):
        def __init__(self, *args):
            args = args
            lenargs = len(args)
            if lenargs > 3 or lenargs < 3:# check if given parameters is not three
                print("Please enter only three parameters!")
                check_args = 'no'
            else:# catch the first two parameters that are naturally strings
                self.fromx = str(args[0]).upper()
                self.to = str(args[1]).upper()
                check_args = 'ok'
            try:# check if the last parameter is a number
                self.value = float(args[3])
            except:
                print('the last parameter should be a number')
                check_args = 'no'
            if check_args=='ok':
                pass
        def head(self):# applying polymorphism on the head method
            print("... CONVERTING LENGTH ...")
        # Using methods names that matches the method names that will be generated/derived below from user inputs to create methods
        def cm_to_m(self):
            cm = self.value
            m = cm * 100
            print(f"{cm}cm  = {m}m"), Notice.done(self)
        def cm_to_ft(self):
            cm = self.value
            ft = (1 / 30.48) * cm
            print(f"{cm}cm  = {ft}ft"), Notice.done(self)
        def cm_to_in(self):
            cm = self.value
            i = (cm / 2.54)
            print(f'{cm}cm  = {i}" '), Notice.done(self)
        def m_to_cm(self):
            m = self.value
            cm = 0.01 * m
            print(f"{cm}cm  = {m}m"), Notice.done(self)
        def m_to_ft(self):
            m = self.value
            ft = 0.3048 * m
            print(f"{m}m  = {ft}ft"), Notice.done(self)
        def m_to_in(self):
            m = self.value
            i = 0.0254 * m
            print(f'{m}m  = {i}"'), Notice.done(self)
        def ft_to_cm(self):
            ft = self.value
            cm = (1 / 30.48) * ft
            print(f"{ft}ft  = {cm}cm"), Notice.done(self)
        def ft_to_m(self):
            ft = self.value
            m = (1 / 0.3048) * ft
            print(f"{ft}ft  = {m}m"), Notice.done(self)
        def ft_to_in(self):
            ft = self.value
            i = (1 / 12) * ft
            print(f'{ft}ft  = {i}"'), Notice.done(self)
        def in_to_cm(self):
            i = self.value
            cm = (1 / 30.48) * i
            print(f'{i}"  = {cm}cm'), Notice.done(self)
        def in_to_ft(self):
            i = self.value
            ft = 12 * i
            print(f'{i}"  = {ft}ft'), Notice.done(self)
        def in_to_m(self):
            i = self.value
            m = (1 / 0.0254) * i
            print(f'{i}"  = {m}m'), Notice.done(self)
        def exe(self):
            self.A =self.B = ''
            Lenght_driver.head(self)
            # processing and converting the different allowed user input into a preferred variable and value
            if self.fromx.upper() == 'METER' or self.fromx.upper() == 'METER(M)' or self.fromx.upper() == 'M':
                self.A = 'm'
            elif self.fromx.upper() == 'CENTIMETER' or self.fromx.upper() == 'CENTIMETER(CM)' or self.fromx.upper() == 'CM':
                self.A = 'cm'
            elif self.fromx.upper() == 'FEET' or self.fromx.upper() == 'FEET(FT)' or self.fromx.upper() == 'FT':
                self.A = 'ft'
            elif self.fromx.upper() == 'INCH' or self.fromx.upper() == 'INCH(")' or self.fromx.upper() == '"':
                self.A = 'in'

            if self.to.upper() == 'METER' or self.to.upper() == 'METER(M)' or self.to.upper() == 'M':
                self.B = 'm'
            elif self.to.upper() == 'CENTIMETER' or self.to.upper() == 'CENTIMETER(CM)' or self.to.upper() == 'CM':
                self.B = 'cm'
            elif self.to.upper() == 'FEET' or self.to.upper() == 'FEET(FT)' or self.to.upper() == 'FT':
                self.B = 'ft'
            elif self.to.upper() == 'INCH' or self.to.upper() == 'INCH(")' or self.to.upper() == '"':
                self.B = 'in'
            # using the above derived variables to determine which conversion method to call
            if F'{self.A}_to_{self.B}' == 'cm_to_m':
                Lenght_driver.cm_to_m(self)
            elif F'{self.A}_to_{self.B}' == 'cm_to_ft':
                Lenght_driver.cm_to_ft(self)
            elif F'{self.A}_to_{self.B}' == 'cm_to_in':
                Lenght_driver.cm_to_in(self)
            elif F'{self.A}_to_{self.B}' == 'm_to_cm':
                Lenght_driver.m_to_cm(self)
            elif F'{self.A}_to_{self.B}' == 'm_to_ft':
                Lenght_driver.m_to_ft(self)
            elif F'{self.A}_to_{self.B}' == 'm_to_in':
                Lenght_driver.m_to_in(self)
            elif F'{self.A}_to_{self.B}' == 'ft_to_cm':
                Lenght_driver.ft_to_cm(self)
            elif F'{self.A}_to_{self.B}' == 'ft_to_m':
                Lenght_driver.ft_to_m(self)
            elif F'{self.A}_to_{self.B}' == 'ft_to_in':
                Lenght_driver.ft_to_in(self)
            elif F'{self.A}_to_{self.B}' == 'in_to_cm':
                Lenght_driver.in_to_cm(self)
            elif F'{self.A}_to_{self.B}' == 'in_to_ft':
                Lenght_driver.in_to_ft(self)
            elif F'{self.A}_to_{self.B}' == 'in_to_m':
                Lenght_driver.in_to_m(self)
            elif F'{self.A}_to_{self.B}' == F'{self.A}_to_{self.B}':
                print('CONVERTING TO SAME UNITE')
                print(f'Convertion, {self.value}{self.fromx} = {self.value}{self.to}')

    class Converter(Notice):# Supper claSS
        def __init__(self, *args):
            args = args
            lenargs = len(args)
            if lenargs > 4 or lenargs < 4:
                print("Please enter only four parameters!")
                check_args = 'no'
            else:# catch the first three parameters that are naturally strings
                self.type = str(args[0]).upper()
                self.fromx = str(args[1]).upper()
                self.to = str(args[2]).upper()
                check_args = 'ok'
            try:# check if the last parameter is a number
                self.value = float(args[3])
            except:
                print('the last parameter should be a number')
                check_args='no'

            if check_args=='ok':
                if self.type.upper() == 'TEMPERATURE' or self.type.upper() == 'T' or self.type.upper() == 'TEMP' or self.type.upper() == 'TEMPERATURE(T)':
                    accepted = Converter.acceptedtempx(self)
                    Driver = Temp_driver(self.fromx, self.to, self.value)
                    proceed = 'yes'
                elif self.type.upper() == 'L' or self.type.upper() == 'LENGHT' or self.type.upper() == 'LEN' or self.type.upper() == 'LENGHT(T)':
                    accepted = Converter.acceptedlengthx(self)
                    Driver = Lenght_driver(self.fromx, self.to, self.value)
                    proceed = 'yes'
                else:
                    Driver = accepted = ''
                    print(f"Error: The 'type' parameter {self.type} is not accepted!")
                    proceed = 'no', Converter.terminate(self)

                if proceed == 'yes':
                    if self.fromx.upper() in accepted and self.to.upper() in accepted:
                        Driver.exe()
                    else:
                        print("Error: Conversion units does not belong to the same class of measurement!")
                        Converter.terminate(self)
    class Interface:
        def __init__(self):
            goo = 'off'
            Notice.head(goo)
            type = input('Enter L for Lenght or T for Temperature: ').strip()
            if type.upper() == 'TEMPERATURE' or type.upper() == 'T' or type.upper() == 'TEMP' or type.upper() == 'TEMPERATURE(T)':
                print("The accepted units of Temperature are Celsius(C), Fahrenheit(F), Kelvin(K) and Rankine(R)")
                proceed = 'on'
            elif type.upper() == 'L' or type.upper() == 'LENGTH(L)' or type.upper() == 'LENGTH':
                print('The accepted units of Lenght are centimeter(cm), meter(m), feet(Ft), inch(")')
                proceed = 'on'
            else:
                Notice.processing(type), print("Conversion type not supported!!!")
                proceed = 'off'

            if proceed == "on":
                fromx = input("Enter 'From' unit: ").strip()
                to = input("Enter 'To' unit: ").strip()
                try:
                    value = float(input('enter number value: ').strip())
                    goo = 'on'
                except:
                    Notice.processing(type), print(f"ERROR: entered value is not a number!")
                    goo = 'off', Notice.terminate(type)
                if goo == "on":
                    Notice.processing(type), \
                    Converter(type, fromx, to, value)
            else:
                Notice.terminate(type)
    Interface()
except:
    print("Program Error; E1")