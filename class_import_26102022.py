# #this imports a function from a module
# a=int(input("enter first number: "))
# b=int(input("enter second number: "))
# c=int(input("enter third number: "))
#
# from class_functions_26102022 import RSum,calc
# print(RSum(a,b,c))
# print(RSum(a,b,c))
#
# print('\n')
#
# #this imports everything in the module
# #this method copies everything from the module
# #it cals any called function that is already called in the module by default
# #hence not the best practice
# from class_cardinal_to_ordinal import*
# #CtoO()


def PlayerAndScores(**kwargs):
    Mystring=f"{kwargs['player1']} score {kwargs['score1']} goals while {kwargs['player2']} scored {kwargs['score2']} goals"
    return(Mystring)
print(PlayerAndScores(player1='Messi', score1='99', player2='Ronaldo', score2='100'))