from gpiozero import LED, Button
from time import sleep

# A=8, B=9, C=10, D=11, E=12, F=13, G=17
sega = LED(8)
segb = LED(9)
segc = LED(10)
segd = LED(11)
sege = LED(12)
segf = LED(13)
segg = LED(17)

led = LED(26)

# btn_activate
btn = Button(27)

# Alarm zones
zone1 = Button(22)
zone2 = Button(5)
zone3 = Button(6)
zone4 = Button(19)

def ledActDe():
    led.on()
    sleep(1)  # 1 second delay
    led.off()

if zone1.is_pressed or zone2.is_pressed or zone3.is_pressed or zone4.is_pressed or btn.is_pressed:
    ledActDe()

#False= unarmed, True= armed
systemStatus = 0

def show0():
    #0
    sega.on()
    segb.on()
    segc.on()
    segd.on()
    sege.on()
    segf.on()
    segg.off()


def show1():
    #1
    sega.off()
    segb.on()
    segc.on()
    segd.off()
    sege.off()
    segf.off()
    segg.off()


def show2():
    #2
    sega.on()
    segb.on()
    segc.off()
    segd.on()
    sege.on()
    segf.off()
    segg.on()  
    

def show3():
    #3
    sega.on()
    segb.on()
    segc.on()
    segd.on()
    sege.off()
    segf.off()
    segg.on() 


def show4():
    #4
    sega.off()
    segb.on()
    segc.on()
    segd.off()
    sege.off()
    segf.on()
    segg.on() 


def show5():
    #5
    sega.on()
    segb.off()
    segc.on()
    segd.on()
    sege.off()
    segf.on()
    segg.on()  
 


def show6():
    #6
    sega.on()
    segb.off()
    segc.on()
    segd.on()
    sege.on()
    segf.on()
    segg.on() 


def show7():
    #7
    sega.on()
    segb.on()
    segc.on()
    segd.off()
    sege.off()
    segf.off()
    segg.off()     



def show8():
    #8
    sega.on()
    segb.on()
    segc.on()
    segd.on()
    sege.on()
    segf.on()
    segg.on()  


def show9():
    #9
    sega.on()
    segb.on()
    segc.on()
    segd.off()
    sege.off()
    segf.on()
    segg.on()    



def showA():
    #A
    sega.on()
    segb.on()
    segc.on()
    segd.off()
    sege.on()
    segf.on()
    segg.on()

def cout_up():
    #0
    show0
    sleep(1)

    #1
    show1()    
    sleep(1)

    #2
    show2() 
    sleep(1)

    #3
    show3()  
    sleep(1)
        
    #4
    show4()
    sleep(1)

    #5
    show5()
    sleep(1)

    #6
    show6() 
    sleep(1)

    #7
    show7() 
    sleep(1)


    #8
    show8()  
    sleep(1)


    #9
    show9()
    sleep(1)



def cout_down():
    #9
    show9    
    sleep(1)

    #8
    show8()  
    sleep(1)

    #7
    show7()   
    sleep(1)

    #6
    show6()  
    sleep(1)

    #5
    show5() 
    sleep(1)

    #4
    show4()  
    sleep(1)

    #3
    show3()    
    sleep(1)

    #2
    show2()  
    sleep(1)

    #1
    show1()    
    sleep(1)
    
    #0
    show0()
    sleep(1)



show0()
while True:
    if systemStatus == 0 and btn.is_pressed:
        cout_up()
        showA()
        systemStatus = 1
    elif systemStatus == 1 and btn.is_pressed:
        cout_down()
        show0()
        systemStatus = 0

    if systemStatus == 1:
        if zone1.is_pressed:
            show1()
        elif zone2.is_pressed:
            show2()
        elif zone3.is_pressed:
            show3()
        elif zone4.is_pressed:
            show4()
       

       





