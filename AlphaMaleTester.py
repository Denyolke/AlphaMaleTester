import webbrowser

def getMogged():
    while(1):
        print(" kys")
        
try:
    a = str(input()).lower()
    lista = ["fanti","oli","fantom","fanthomas77","olikavezer","olcsi","sebi"]
    
    if a.isalpha() == False or a in lista:
        getMogged()
    elif a.isalpha():
        webbrowser.open("https://youtu.be/0GVExpdmoDs?t=183")
        print("yes")


except Exception as e:
    print(e,"agyhalott vagy")


