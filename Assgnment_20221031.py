print("UNIT CONVERTER (TEMPRATURE AND LENGHT)")
#child classes
class Temp:
    """TEMPERATURE CONVERTERS"""
    def c_to_f(self, value: int):
        C=self.value
        f=(C*(9/5))+32
        print(f"Temperature convertion, {C} degree Celcius = {f} degree Fahrenheit")
    def c_to_k(self, value: int):
        C=self.value
        k=C+273.15
        print(f"Temperature convertion, {C} degree Celcius to Kelvin is = {k} degree Kelvin")
    def c_to_r(self, value: int):
        C=self.value
        r=C+273.15
        print(f"Temperature convertion, {C} degree Celcius to Kelvin is = {r} degree Rankine")
    def r_to_f(self, value: int):
        r=self.value
        f=r-459.67
        print(f"Temperature convertion, {r} degree Rankine to Fahrenheit is = {f} degree Fahrenheit")
    def r_to_k(self, value: int):
        r=self.value
        k=r*(5/9)
        print(f"Temperature convertion, {r} degree Rankine to Kelvin is = {k} degree Kelvin")
    def f_to_c(self, value: int):
        f=self.value
        c=(f-32)*(5/9)
        print(f"Temperature convertion, {f} degree Fahrenheit to Celcius is = {c} degree Celcius")
    def f_to_k(self, value: int):
        f=self.value
        k=(f+459.69)*(5/9)
        print(f"Temperature convertion, {f} degree Fahrenheit to Celcius is = {k} degree Kelvin")
    def f_to_r(self, value: int):
        f=self.value
        r=(f+459.69)
        print(f"Temperature convertion, {f} degree Fahrenheit to Rankine is = {r} degree Rankine")
    def k_to_f(self, value: int):
        k=self.value
        f=(k*(9/5))-459.67
        print(f"Temperature convertion, {f} degree Kelvin to Fahrenheit is = {k} degree Fahrenheit")
    def k_to_r(self, value: int):
        k=self.value
        r=k*(9/5)
        print(f"Temperature convertion, {k} degree Kelvin to Fahrenheit is = {r} degree Rankine")
    def k_to_c(self, value: int):
        k=self.value
        c=k-273.15
        print(f"Temperature convertion, {k} degree Kelvin to Fahrenheit is = {c} degree Celcius")


    def __init__(self,fromx: str, to:str, value: float ):
        self.fromx=fromx
        self.to = to
        self.value = value




class Lenght:
    def cm_to_m(self, value: int):
        cm=self.value
        m=cm*100
        print(f"Lenght convertion, {cm}cm  = {m}m")
    def cm_to_ft(self, value: int):
        cm=self.value
        ft= (1/30.48)*cm
        print(f"Lenght convertion, {cm}cm  = {ft}ft")
    def cm_to_in(self, value: int):
        cm=self.value
        i=(cm/2.54)
        print(f'Lenght convertion, {cm}cm  = {i}" ')
    def m_to_cm(self, value: int):
        m=self.value
        cm=0.01*m
        print(f"Lenght convertion, {cm}cm  = {m}m")
    def m_to_ft(self, value: int):
        m=self.value
        ft=0.3048*m
        print(f"Lenght convertion, {m}m  = {ft}ft")
    def m_to_in(self, value: int):
        m=self.value
        i=0.0254*m
        print(f'Lenght convertion, {m}m  = {i}"')
    def ft_to_cm(self, value: int):
        ft=self.value
        cm=(1/30.48)*ft
        print(f"Lenght convertion, {ft}ft  = {cm}cm")
    def ft_to_m(self, value: int):
        ft=self.value
        m=(1/0.3048)*ft
        print(f"Lenght convertion, {ft}ft  = {m}m")
    def ft_to_in(self, value: int):
        ft=self.value
        i=(1/12)*ft
        print(f'Lenght convertion, {ft}ft  = {i}"')
    def in_to_cm(self, value: int):
        i=self.value
        cm=(1/30.48)*i
        print(f'Lenght convertion, {i}"  = {cm}cm')
    def in_to_ft(self, value: int):
        i=self.value
        ft=12*i
        print(f'Lenght convertion, {i}"  = {ft}ft')
    def in_to_m(self, value: int):
        i=self.value
        m=(1/0.0254)*i
        print(f'Lenght convertion, {i}"  = {m}m')

    def __init__(self,fromx: str, to:str, value: float ):
        self.fromx=fromx
        self.to = to
        self.value = value





class Temp_driver:

    def __init__(self, fromx: str, to: str, value: int):
        self.fromx=fromx
        self.to = to
        self.value=value
        self.A = ''
        self.B = ''


        if self.fromx.upper() == 'FAHRENHEIT' or self.fromx.upper() == 'FAHRENHEIT(F)' or self.fromx.upper() == 'F':
            self.A='f'
        elif self.fromx.upper() == 'CELCIUS' or self.fromx.upper() == 'CELCIUS(C)' or self.fromx.upper() == 'C':
            self.A='c'
        elif self.fromx.upper() == 'KELVIN' or self.fromx.upper() == 'KELVIN(K)' or self.fromx.upper() == 'K':
            self.A='k'
        elif self.fromx.upper() =='RANKINE' or self.fromx.upper() == 'RANKINE(R)' or self.fromx.upper() == 'R':
            self.A='r'

        if self.to.upper()  == 'FAHRENHEIT' or self.to.upper() == 'FAHRENHEIT(F)' or self.to.upper() == 'F':
            self.B = 'f'
        elif self.to.upper()  == 'CELCIUS' or self.to.upper() == 'CELCIUS(C)' or self.to.upper() == 'C':
            self.B = 'c'
        elif self.to.upper()  == 'KELVIN' or self.to.upper() == 'KELVIN(K)' or self.to.upper() == 'K':
            self.B = 'k'
        elif self.to.upper() == 'RANKINE' or self.to.upper() == 'RANKINE(R)' or self.to.upper() == 'R':
            self.B = 'r'


        if F'{self.A}_to_{self.B}'=='r_to_f':
            Temp.r_to_f(self, self.value)
        elif F'{self.A}_to_{self.B}'=='r_to_k':
            Temp.r_to_k(self, self.value)
        elif F'{self.A}_to_{self.B}'=='c_to_f':
            Temp.c_to_f(self, self.value)

        elif F'{self.A}_to_{self.B}'=='c_to_k':
            Temp.c_to_k(self, self.value)
        elif F'{self.A}_to_{self.B}'=='c_to_r':
            Temp.c_to_r(self, self.value)

        elif F'{self.A}_to_{self.B}'=='f_to_c':
            Temp.f_to_c(self, self.value)
        elif F'{self.A}_to_{self.B}'=='f_to_k':
            Temp.f_to_k(self, self.value)

        elif F'{self.A}_to_{self.B}'=='f_to_r':
            Temp.f_to_r(self, self.value)
        elif F'{self.A}_to_{self.B}'=='k_to_f':
            Temp.k_to_f(self, self.value)

        elif F'{self.A}_to_{self.B}' == 'k_to_r':
            Temp.k_to_r(self, self.value)
        elif F'{self.A}_to_{self.B}' == 'r_to_f':
            Temp.r_to_f(self, self.value)
        elif F'{self.A}_to_{self.B}' == 'k_to_c':
            Temp.k_to_c(self, self.value)
        elif F'{self.A}_to_{self.B}' == F'{self.A}_to_{self.B}':
            print('CONVERTING TO SAME UNITE')
            print(f'Convertion, {self.value}{self.fromx} = {self.value}{self.to}')



class Lenght_driver:
    def __init__(self, fromx: str, to: str, value: int):
        self.fromx=fromx
        self.to = to
        self.value=value
        self.A = ''
        self.B = ''

        if self.fromx.upper() == 'METER' or self.fromx.upper() == 'METER(M)' or self.fromx.upper() == 'M':
            self.A='m'
        elif self.fromx.upper() == 'CENTIMETER' or self.fromx.upper() == 'CENTIMETER(CM)' or self.fromx.upper() == 'CM':
            self.A='cm'
        elif self.fromx.upper() == 'FEET' or self.fromx.upper() == 'FEET(FT)' or self.fromx.upper() == 'FT':
            self.A='ft'
        elif self.fromx.upper() =='INCH' or self.fromx.upper() == 'INCH(")' or self.fromx.upper() == '"':
            self.A='in'

        if self.to.upper()  == 'METER' or self.to.upper() == 'METER(M)' or self.to.upper() == 'M':
            self.B = 'm'
        elif self.to.upper()  == 'CENTIMETER' or self.to.upper() == 'CENTIMETER(CM)' or self.to.upper() == 'CM':
            self.B = 'cm'
        elif self.to.upper()  == 'FEET' or self.to.upper() == 'FEET(FT)' or self.to.upper() == 'FT':
            self.B = 'ft'
        elif self.to.upper() == 'INCH' or self.to.upper() == 'INCH(")' or self.to.upper() == '"':
            self.B = 'in'

        if F'{self.A}_to_{self.B}'=='cm_to_m':
            Lenght.cm_to_m(self.value)

        elif F'{self.A}_to_{self.B}'=='cm_to_ft':
            Lenght.cm_to_ft(self.value)

        elif F'{self.A}_to_{self.B}' == 'cm_to_in':
            Lenght.cm_to_in(self, self.value)

        elif F'{self.A}_to_{self.B}' == 'm_to_cm':
            Lenght.m_to_cm(self, self.value)

        elif F'{self.A}_to_{self.B}'=='m_to_ft':
            Lenght.m_to_ft(self, self.value)

        elif F'{self.A}_to_{self.B}'=='m_to_in':
            Lenght.m_to_in(self, self.value)

        elif F'{self.A}_to_{self.B}'=='ft_to_cm':
            Lenght.ft_to_cm(self, self.value)

        elif F'{self.A}_to_{self.B}'=='ft_to_m':
            Lenght.ft_to_m(self, self.value)

        elif F'{self.A}_to_{self.B}'=='ft_to_in':
            Lenght.ft_to_in(self, self.value)

        elif F'{self.A}_to_{self.B}'=='in_to_cm':
            Lenght.in_to_cm(self, self.value)

        elif F'{self.A}_to_{self.B}'=='in_to_ft':
            Lenght.in_to_ft(self, self.value)

        elif F'{self.A}_to_{self.B}'=='in_to_m':
            Lenght.in_to_m(self, self.value)
        elif F'{self.A}_to_{self.B}' == F'{self.A}_to_{self.B}':
            print('CONVERTING TO SAME UNITE')
            print(f'Convertion, {self.value}{self.fromx} = {self.value}{self.to}')




#supper class
class Converter:
    Acceptedtemp = ['CELCIUS', 'CELCIUS(C)', 'C', 'FAHRENHEIT', 'FAHRENHEIT(F)', 'F', 'KELVIN', 'KELVIN(K)', 'K',
                    'RANKINE', 'RANKINE(R)', 'R']
    Acceptedlenght = ['METER', 'METER(M)', 'M', 'CENTIMETER', 'CENTIMETER(CM)', 'CM', 'FEET', 'FEET(FT)', 'FT', 'INCH',
                      'INCH(")', '"']

    MyKelvin=['KELVIN', 'KELVIN(K)', 'K']
    MyCelcius=['CELCIUS', 'CELCIUS(C)', 'C']
    MyFahreinheit=['FAHRENHEIT', 'FAHRENHEIT(F)', 'F']
    MyRankine = ['RANKINE', 'RANKINE(R)', 'R']

    def temprature(self, fromx: str, to:str, value: float):
        self.result = Temp(self.fromx, self.to, self.value)
        return self.result

    def lenght(self, fromx: str, to:str, value: float):
        self.result = Lenght(self.fromx, self.to, self.value)
        return self.result

    def __init__(self, type: str, fromx: str, to:str, value: float ):
        self.type=type
        self.fromx=fromx
        self.to=to
        self.value = value
        # Actions to execute
        # we us an if statement to call a method
        if self.type.upper()=='TEMPERATURE' or self.type.upper()=='T' or self.type.upper()=='TEMP' or self.type.upper()=='TEMPERATURE(T)':
            #call the temprature driver
            acceptedtemp=Converter.Acceptedtemp
            assert self.fromx.upper() in acceptedtemp, f"Temperature {self.fromx} is not an accepted temperature!"
            assert self.to.upper() in acceptedtemp, f"Temperature {self.to} is not an accepted temperature!"
            Temp_driver(self.fromx, self.to, self.value)


        elif self.type.upper()=='L' or self.type.upper()=='LENGHT' or self.type.upper()=='LEN' or self.type.upper()=='LENGHT(T)' :
            # call the lenght driver
            acceptedlenght=Converter.Acceptedlenght
            assert self.fromx.upper() in acceptedlenght, f"Temperature {self.fromx} is not an accepted temperature!"
            assert self.to.upper() in acceptedlenght, f"Temperature {self.to} is not an accepted temperature!"
            Lenght_driver(self.fromx, self.to, self.value)

        else:
            print(f"Error: The 'type' parameter {self.type} is not accepted!")




type=input('What are you converting, Enter (L or Lenght) for Lenght or Enter (T or Temprature) for Temperature: ').strip()
if type.upper()=='TEMPERATURE' or type.upper()=='T' or type.upper()=='TEMP' or type.upper()=='TEMPERATURE(T)':
    print("...INITIATING TEMPERATURE CONVERSION...")
    print("The accepted units of Temperature are Celsius(C), Fahrenheit(F), Kelvin(K) and Rankine(R)")
    proceed = 'on'
elif type.upper()=='METER' or type.upper()=='METER(M)' or type.upper()=='M' or type.upper()=='CENTIMETER' or type.upper()=='CENTIMETER(CM)' or type.upper()=='CM' or type.upper()=='FEET' or type.upper()=='FEET(FT)' or type.upper()=='FT' or type.upper()=='INCH' or type.upper()=='INCH(")' or type.upper()=='"':
    print("...INITIATING LENGHT CONVERSION...")
    print('The accepted units of Lenght are centimeter(cm), meter(m), feet(Ft), inch(")')
    proceed = 'on'
else:
    print("Conversion type not supported!!!")
    proceed = 'off'

if proceed=="on":
    fromx=input("Enter 'From' unit: ").strip()
    to=input("Enter 'To' unit: ").strip()
    value=float(input('enter number value: ').strip())

    print("...PROCESSING...")
    Converter(type,fromx,to,value)
else:
    print("...PROCESS TERMINATED!...")
