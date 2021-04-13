tillverkmugg = float(input("Hur många antal var det som tillverkades? "))
#Hur många muggar var det som tillverkades
tillverkning = 22 * tillverkmugg 
#Hur mycket det kostar för att tillverka alla muggar
såldamuggar = float(input("Hur många antal muggar var det som såldes? "))
#Hur många muggar såldes
inkomst = 62 * såldamuggar
#Inkomst från de muggarna som såldes
utgifter = 3800 + 2500 + 700 + 1000
#alla utgifter för lokalen
inkomst = inkomst - tillverkning - utgifter 
#Inkomst för den här månaden
if(inkomst > 0):
    print("Vinsten för den här månaden blir: ", inkomst, "kr. ")
elif(inkomst == 0):
    print("Den här månaden fick du ingen vinst :( kanske nästa månad blir bättre :) ")
else: 
    print("Förlusten för den här månaden blir: ", inkomst, "kr. ")
#Proggram som räknar vinsten/förlusten för den här månaden