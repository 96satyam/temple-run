print('''
               V        V    	
                          +........+
                          J||||||||L
                        /            \
                       ~/~~~~~~~~~~~~\~
                       /              \
                    ~~/~~~~~~~~~~~~~~~~\~~
        _--^I^--_    /                  \
       / /^~|~^\ \~~~~~~+~+~~~~~~~~+~+~~~~~
      / /   |   \ \     | |        | |
      | |   |   | |     = =        = =
~~~~~~~ |   |o  | ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
------- |   |   | ---------------------------------
------- |   |   | ---------------------------------
======= |===|===| ================================

         V        V    	
         +........+
         J||||||||L
       /            \
      ~/~~~~~~~~~~~~\~
      /              \
   ~~/~~~~~~~~~~~~~~~~\~~
    /                  \
 ~~~~~~+~+~~~~~~~~+~+~~~~~
       | |        | |
       = =   i    = =
       | |   U    | |
      /   \ | |  /   \
 mmmmmmmmmmmmmmmmmmmmmmmmmm
 mmmmmmmmmmmmmmmmmmmmmmmmmm
''')
print("Welcome to Temple Run.")
print("Your mission is to reach the temple.") 
print("RUN! ")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice1 = input("Select left or right!\n")
choice1.lower()
if choice1 == "left":
          print("Good Move")
else:
          print("Oops! You have choosen longer path.")
choice2 = input("select left, right or straight\n")
choice2.lower()
if(choice2=="left"):
          print("Be safe! There is a well in front of you.")
elif(choice2=="right"):
          print("You got 100 coins and a safe route.")
else:
          print("You have caught! Game Over.")
choice3 = input("Select left or right\n")
choice3.lower()
if(choice3 == "left"):
          print("Got Fire! Game Over.")
else:
          print("Congratulations! You have reached the temple.")
