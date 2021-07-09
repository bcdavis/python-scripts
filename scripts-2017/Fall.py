"""
Ben Davis
Let's make a game
"""

#Fall
coolKeys = {'z':6,'x':7,'c':8,'v':9,'b':10,'n':12,'m':13}

def Heart():
    print("   zzzz       zzzz   ")
    print(" zz    zz   zz    zz ")
    print("zz       zzz       zz")
    print("zz                 zz")
    print(" zz               zz ")
    print("  zz             zz  ")
    print("   zz           zz   ")
    print("     zz       zz     ")
    print("       zz   zz       ")
    print("         zzz         ")
    


keyPressed = input()
num = coolKeys[keyPressed]
#nu = "%-" + str(num)
#print(nu)
if keyPressed in coolKeys:
    if ord(keyPressed) == ord('z'):
        Heart()
    print("\n   |   %-6s  |"% keyPressed)
    
   
   
    

