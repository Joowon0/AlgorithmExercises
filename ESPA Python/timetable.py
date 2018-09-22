def delim() :
    for i in range(5) :
        print ("+-----", end = '')
    print ("+")

def row(time, monWed1, monWed2, tueThu1, tueThu2):
    print ("+"+time, end = '')
    print ("+"+monWed1, end = '')
    print ("+"+tueThu1, end = '')
    print ("+"+monWed1, end = '')
    print ("+"+tueThu1, end = '')
    print ("+")

    print ("+     ", end = '')
    print ("+"+monWed2, end = '')
    print ("+"+tueThu2, end = '')
    print ("+"+monWed2, end = '')
    print ("+"+tueThu2, end = '')
    print ("+")
    delim()
    
def header() :
    delim()
    print ("+     ", end = '')
    print ("+ MON ", end = '')
    print ("+ TUE ", end = '')
    print ("+ WED ", end = '')
    print ("+ THU ", end = '')
    print ("+")
    delim()

blank = "     "
header()
row("09:00", " NET ", "WORK ", blank, blank)
row("10:30", blank, blank, "INTEL", "SYSTM")
row("13:30", blank, blank, "DATA ", "MININ")
row("15:00", blank, blank, blank, blank)
row("16:30", blank, blank, blank, blank)
