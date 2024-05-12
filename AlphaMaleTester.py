import webbrowser
print("Tell me your name: ")
def getMogged():
    while(1):
        print("kys")
        
        
try:
    a = str(input()).lower()
    lista = ["fanti","oli","fantom","fanthomas77","olikavezer","olcsi","sebi","darksnhun"]
    
    if a.isalpha() == False or a in lista:
        getMogged()
    elif a.isalpha():
        webbrowser.open("https://youtu.be/0GVExpdmoDs?t=183")
        print("Based")


except Exception as e:
    print(e,"agyhalott vagy")


