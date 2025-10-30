'''
This project creates an animated demon-like creature (which fit Halloween vibe) that moves smoothly up and down
while its wings flap, its head gently tilts, and its color pulses as if it were breathing. 
It combines motion, transformation, and procedural drawing using multiple custom functions. 
All parts of the creature—head, body, arms, legs, and wings—are drawn separately and combined 
into one figure through translate(), rotate(), and scale() operations to demonstrate control 
over hierarchical composition on the canvas. The code also implements continuous movement 
between two defined points (A and B) by using variables, conditionals, and direction reversal.

I designed this project because I wanted to explore how to bring a hand-drawn (I drew a draft of this creature), 
fantasy-inspired monster sketch to life through Python animation. The process helped me 
understand not only the visual logic of layered transformations but also how to use 
mathematical functions like sin() and cos() to create organic, life-like motion. 

I came up with this creature's idea and concept by one of my drawings. I received conceptual and structural
guidance from ChatGPT (AI) for organizing my functions and animation logic, but all final code, syntax corrections,
variable naming, and artistic choices—including the creature’s proportions, wing motion, and head rotation—were written 
and debugged by me. I also reviewed Getting Started with Processing.py online documentation pages for 
syntax references.

This program demonstrates mastery of at least five key programming topics from the book:
1. Functions and Parameters: Each body part is modularized into its own function for clarity and reuse.
2. Control Flow and Variables: Direction changes and animation updates rely on if-statements and global variables.
3. Canvas Transformations: Extensive use of translate(), rotate(), scale(), and push/pop matrix operations.
4. Mathematical Animation: Use of sine functions to simulate breathing, flapping, and head movement.
5. Scope and Reusability: Clear separation of global variables, drawing functions, and the main animation loop.

I chose this design because I enjoy creating eerie and surreal imagery. This project 
represents the transition from static drawing to animated storytelling and shows how 
Python can be used as a creative medium for procedural art and design.

Comments: 
I think I made some improvements compared to the past few creatures I did. It fit the prompt well, and I used a lot of functions here, and it fit the Halloween vibe. It is not so scary, but cute. I used AI to help with the big picture, the structure stuff, to make sure I was not deviating from the project's expective goal. Besides this, I wrote, adjusted, and debugged all the code. 
'''

import py5

pos_y = 0
direction = 1
speed = 2


def setup():
    py5.size(800, 800)
    py5.background(240)
    py5.no_stroke()
    

    
def draw_creature(wing_angle, t, head_angle):
    
    py5.translate(-380, -500)
     
    # Wings
    py5.push_matrix()
    py5.rotate(wing_angle)  # Rotation
    draw_wing(-50, -70, t, flip=False)
    py5.pop_matrix()

    py5.push_matrix()
    py5.scale(-1, 1)
    py5.rotate(wing_angle)
    draw_wing(-50, -70, t, flip=False)
    py5.pop_matrix()
    
    # Head swaying
    py5.push_matrix()
    py5.translate(0, -180)
    py5.rotate(head_angle)
    draw_head(0, 0)
    py5.pop_matrix()

    #draw_wing(-50, -70, flip=False)
    #draw_wing(50, -70, flip=True)
    
    draw_body(0, 0)#body
    
   # draw_head(0, -180)
    draw_arm(-105, -40, flip=False)
    draw_arm(105, -40, flip=True)
    draw_leg(-60, 180)
    draw_leg(60, 180)
    
def draw():
    global pos_y, direction
    
    py5.background(240)
    py5.translate(py5.width / 2, py5.height / 2 + 100)


        
    
    # update motion
    pos_y += speed * direction
    if pos_y > 70 or pos_y < -50:  # moving range
        direction *= -1
        
    # Seperate parts motion
    wing_angle = py5.sin(py5.frame_count * 0.1) * 0.3          # The rotation angle of wings
    color_shift = 120 + py5.sin(py5.frame_count * 0.05) * 60   # The changing of color
    head_angle = py5.sin(py5.frame_count * 0.03) * 0.1         # The swaying of head
    
    
    
    # Demon's motion as a whole
    py5.push_matrix()
    py5.translate(py5.width / 2, py5.height / 2 + pos_y)
    draw_creature(wing_angle, color_shift, head_angle)
    py5.pop_matrix()
    

# Head
def draw_head(x, y):
    py5.push_matrix()
    py5.translate(x, y)
    py5.fill(210, 30, 40)
    py5.rect_mode(py5.CENTER)
    py5.rect(0, 0, 120, 120, 10)
    
    # Horns
    py5.fill(120, 0, 10)
    py5.triangle(-40, -60, -20, -160, -5, -60)
    py5.triangle(40, -60, 20, -160, 5, -60)
    
    # Eyes
    py5.fill(0)
    py5.begin_shape()
    py5.vertex(-25, -10)
    py5.vertex(-10, -25)
    py5.vertex(10, -25)
    py5.vertex(25, -10)
    py5.vertex(10, 0)
    py5.vertex(-10, 0)
    py5.end_shape(py5.CLOSE)
    
    py5.begin_shape()
    py5.vertex(25, -10)
    py5.vertex(10, -25)
    py5.vertex(-10, -25)
    py5.vertex(-25, -10)
    py5.vertex(-10, 0)
    py5.vertex(10, 0)
    py5.end_shape(py5.CLOSE)
    
    # Nose
    py5.fill(0)
    py5.triangle(-10, 10, 0, 30, 10, 10)
    
    # Teeth
    py5.fill(255)
    py5.rect(0, 40, 70, 15)
    py5.fill(0)
    for i in range(-30, 35, 10):
        py5.rect(i, 40, 3, 15)
    py5.pop_matrix()


# suit
def draw_body(x, y):
    py5.push_matrix()
    py5.translate(x, y)
    
    #fill(150, 0, 0, color_shift)
    #ellipse(0, 0, 120, 180)
    py5.fill(40)
    
    py5.rect_mode(py5.CENTER)
    py5.rect(0, 0, 180, 240, 10)
    
    # tie
    py5.fill(20)
    py5.triangle(-70, -120, 0, -20, -10, -120)
    py5.triangle(70, -120, 0, -20, 10, -120)
    
    py5.fill(120, 0, 10)
    py5.triangle(-10, -120, 10, -120, 0, 40)
    py5.pop_matrix()


# Arms
def draw_arm(x, y, flip=False):
    py5.push_matrix()
    py5.translate(x, y)
    if flip:
        py5.scale(-1, 1)
    py5.fill(40)
    py5.rect(0, 0, 30, 120, 10)
    py5.fill(120, 0, 10)
    py5.rect(0, 70, 30, 40, 10)
    py5.pop_matrix()


# Legs
def draw_leg(x, y):
    py5.push_matrix()
    py5.translate(x, y)
    py5.fill(40)
    py5.rect(0, 0, 40, 120, 10)
    py5.fill(20)
    py5.ellipse(0, 70, 50, 20)
    py5.pop_matrix()


# Wings
def draw_wing(x, y, t, flip=False):
    py5.push_matrix()
    py5.translate(x, y)
    if flip:
        py5.scale(-1, 1)
    #fill(100, 0, 10)
    #fill(150, 0, 0, color_shift)
    r = 120 + py5.sin(t * 0.05) * 60  # Range of color
    py5.fill(r, 30, 30)
    
    py5.ellipse(0, 0, 120, 180)
    
    py5.begin_shape()
    py5.vertex(0, 0)
    py5.vertex(-140, -40)
    py5.vertex(-180, -80)
    py5.vertex(-120, -100)
    py5.vertex(-180, -160)
    py5.vertex(-100, -120)
    py5.vertex(-60, -60)
    py5.end_shape(py5.CLOSE)
    py5.pop_matrix()

py5.run_sketch()