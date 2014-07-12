# Implementation of classic arcade game Pong

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos=[WIDTH/2,HEIGHT/2]
ball_vel=[0,4]
paddle1_vel=0
paddle2_vel=0
paddle1_pos=[0,0]
paddle2_pos=[0,0]
paddle1_pos[0]=(HEIGHT/2)-HALF_PAD_HEIGHT
paddle1_pos[1]=HEIGHT/2-HALF_PAD_HEIGHT+PAD_HEIGHT
score1=0
score2=0
paddle2_pos[0]=(HEIGHT/2)-HALF_PAD_HEIGHT
paddle2_pos[1]=HEIGHT/2-HALF_PAD_HEIGHT+PAD_HEIGHT
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    if(direction==False):
        ball_vel[0]=-random.randrange(1,5)
        ball_vel[1]=-random.randrange(1,5)
    if(direction==True):
        ball_vel[0]=random.randrange(1,5)
        ball_vel[1]=-random.randrange(1,5)
           
      

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(RIGHT)

def draw(canvas):
    
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    
    
    
    
    
    
    
   
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    
     
    if ball_pos[1] <= 0:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1]>=(HEIGHT):
        ball_vel[1]= - ball_vel[1]
    
    if ball_pos[0] <= BALL_RADIUS+PAD_WIDTH:
        if(ball_pos[0]<=paddle1_pos[0] & ball_pos[0]>paddle1_pos[1]):
            ball_vel[1] = - ball_vel[1]
        else:
            score2+=1
            spawn_ball(RIGHT)
    elif ball_pos[0]>=((WIDTH-1)-BALL_RADIUS+PAD_WIDTH):
        if(ball_pos[0]<=paddle2_pos[0] & ball_pos[0]>paddle2_pos[1]):
             ball_vel[1] = - ball_vel[1]
        else:
            score1+=1
            spawn_ball(LEFT)
    
    
    
   # if ball_pos[0] <= BALL_RADIUS:
    #    spawn_ball(RIGHT)
    #elif ball_pos[0]>=((WIDTH-1)-BALL_RADIUS):
     #   spawn_ball(LEFT)
     
   
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    # update paddle's vertical position, keep paddle on the screen
    temp1=paddle1_pos[0]
    paddle1_pos[0]+=paddle1_vel
    temp2=paddle1_pos[1]
    paddle1_pos[1]+=paddle1_vel
    if(paddle1_pos[0]<0):
        paddle_pos[0]=temp1
    elif(paddle1_pos[1]>HEIGHT-1):
        paddle_pos[1]=temp2
        
  
    paddle2_pos[0]+=paddle2_vel
    paddle2_pos[1]+=paddle2_vel
    if(paddle1_pos[0]<0):
        paddle2_pos[0]-=paddle2_vel
    elif(paddle1_pos[1]>HEIGHT-1):
        paddle2_pos[1]-=paddle2_vel
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos[0]],[PAD_WIDTH, paddle1_pos[0]],[PAD_WIDTH, paddle1_pos[1]],[0, paddle1_pos[1]]], 1, 'Yellow', 'Orange')
    canvas.draw_polygon([[WIDTH-1,paddle2_pos[0]],[WIDTH-1-PAD_WIDTH,paddle2_pos[0]],[WIDTH-1-PAD_WIDTH,paddle2_pos[1]],[WIDTH-1,paddle2_pos[1]]], 1, 'Yellow', 'Orange')
    # draw scores
        
def keydown(key):
    acc=4
    global paddle1_vel, paddle2_vel
    
    
    if key == simplegui.KEY_MAP["down"]:
        
        
        paddle1_vel += acc
        #print paddle1_vel
    elif key == simplegui.KEY_MAP["up"]:
       
       
        paddle1_vel -=acc
        
    if key == simplegui.KEY_MAP["w"]:
        paddle2_vel -= paddle2_vel
    elif key == simplegui.KEY_MAP["s"]:
        paddle2_vel += paddle2_vel     
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["down"]:
       paddle1_vel -= 4
    elif key == simplegui.KEY_MAP["up"]:
        paddle1_vel += 4
    if key == simplegui.KEY_MAP["w"]:
        paddle2_vel += 4
    elif key == simplegui.KEY_MAP["s"]:
        paddle2_vel -= 4 

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
