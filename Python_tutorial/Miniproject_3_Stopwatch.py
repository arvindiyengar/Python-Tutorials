# template for "Stopwatch: The Game"
import simplegui


flag=0
var=0
display_string="0:00.0"
total_stop=0
success_stop=0
attempt=str(success_stop)+"/"+str(total_stop)


def formt(t):
    global flag
    
    mints=t//600
    msec=t%10
    #msec value is saved in flag for checking positive game outcome
    flag=msec
    sec1=t-(mints*600)
    sec1=sec1//10
    seca=sec1//10
    secb=sec1%10
      
    return str(mints)+":"+str(seca)+str(secb)+"."+str(msec)
    

def tick():
    global var,display_string
    var=var+1
    display_string=formt(var)
    

def start():
    timer.start()
    
def reset():
   
    global attempt,var,display_string,success_stop,total_stop
    timer.stop()
    var=0
    display_string=formt(var)
    success_stop=0
    total_stop=0
    attempt=str(success_stop)+"/"+str(total_stop)
  
    
    
def stop():
    global success_stop,total_stop,attempt
    if(timer.is_running()):  
        timer.stop()
        total_stop=total_stop+1
        if(flag==0):
            success_stop=success_stop+1
        attempt=str(success_stop)+"/"+str(total_stop)




def draw_handler(canvas):
    
    canvas.draw_text(display_string,[100, 100], 24, "White")
    
    canvas.draw_text(attempt,[200, 40], 10, "White")
    

frame=simplegui.create_frame("StopWatch",300,300);
frame.add_button("Start",start)
frame.add_button("Stop",stop)
frame.add_button("Reset",reset)
frame.set_draw_handler(draw_handler)

timer = simplegui.create_timer(100, tick)



frame.start()


