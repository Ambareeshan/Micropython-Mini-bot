# WiFi Controlled Bot

from machine import Pin, Signal
import time
import network
import socket

#initialising the pins

motor11 = Pin(4, Pin.OUT)
motor12 = Pin(0, Pin.OUT)
enable11 = Pin(5, Pin.OUT)

motor21 = Pin(14, Pin.OUT)
motor22 = Pin(12, Pin.OUT)
enable21 = Pin(13, Pin.OUT)

#Inverting them using signal

motor_pin11 = Signal(motor11, invert = True)
motor_pin12 = Signal(motor12, invert = True)
enable1 = Signal(enable11, invert = True)

motor_pin21 = Signal(motor21, invert = True)
motor_pin22 = Signal(motor22, invert = True)
enable2 = Signal(enable21, invert = True)

#Motor Movement Function

enable11.off()
enable21.off()

def forward():
    enable11.on()
    enable21.on()
    motor_pin11.on()
    motor_pin12.off()  
    
    motor_pin21.on()
    motor_pin22.off()

def backward():
    enable11.on()
    enable21.on()
    
    motor_pin11.off()
    motor_pin12.on()
    
    motor_pin21.off()
    motor_pin22.on()

def left():
    enable11.on()
    enable21.on()
    motor_pin11.off()
    motor_pin12.off()
    
    motor_pin21.on()
    motor_pin22.off()

def right():
    enable11.on()
    enable21.on()
    motor_pin11.on()
    motor_pin12.off()
    
    motor_pin21.off()
    motor_pin22.off()

def stop():
    enable11.on()
    enable21.on()
    motor_pin11.off()
    motor_pin12.off()
    
    motor_pin21.off()
    motor_pin22.off()



#Connecting to the Wifi

sta = network.WLAN(network.STA_IF)
if not sta.isconnected():
    print('Connecting to Network')
    sta.active(True)
    sta.connect('Railnet', 'sharan*100*')
    
    while not sta.isconnected():
        pass
print('Network Config: ', sta.ifconfig())

#Configure Socket Connection

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',80))
s.listen(5)

#Creating the Webpage

def web_page():
    html_page="""
                 <html>
                 <head>
                 <meta content="width=device-width, initial-scale=1" name="viewport"></meta>
                 </head>
                     <body>
                         <center><h2>WiFi Controlled Bot</h2></center>
                         <center>
                             <form>
                                 <button name = "Button" type = "submit" value = "1">FWD</button>
                                 <button name = "Button" type = "submit" value = "2">LEFT</button>
                                 <button name = "Button" type = "submit" value = "0">STOP</button>
                                 <button name = "Button" type = "submit" value = "3">RIGHT</button>
                                 <button name = "Button" type = "submit" value = "5">BCK</button>
                             </form>
                         </center>
                     </body>
                 </html>"""
    return html_page

#Socket Accept Receive Send and Close

while True:
    #Socket Accept
    conn, addr = s.accept()
    print('Got Connection from %s' % str(addr))
    
    #Socket Receive
    request = conn.recv(1024)
    print("")
    print("")
    print("Content %s" % str(request))
    
    #Socket Send
    request=str(request)
    
    fwd = request.find('/?Button=1')
    bck = request.find('/?Button=5')
    left1 = request.find('/?Button=2')
    right1 = request.find('/?Button=3')
    stop1 = request.find('/?Button=0')
    
    if fwd==6:
        forward()
    elif bck==6:
        backward()
    elif left1==6:
        left()
    elif right1==6:
        right()
    elif stop1==6:
        stop()
    
    response = web_page()
    conn.send("HTTP/1.1 200 OK\n")
    conn.send("Content-type: text/html\n")
    conn.send("Connection: close\n\n")
    conn.sendall(response)
    
    #Socket Close
    conn.close()
    
    
    