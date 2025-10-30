'''
By Aaron Lee

Description:
The creature is named Simon. This program creates however many Simons you want and makes them float around the canvas like butterflies. 
As you make more Simons, they appear further and further from the camera, floating in deep space. All physical traits of Simon is dynamic,
so the size and position of the arms and eyes change proportionally with the body, and the Simons' movement changes proportionally to
the canvas size.

Use of AI:
I used AI minimally to ask general questions about P3D. The expression "y = self.initial_y + self.amplitude * py5.sin(self.frequency * x)"
was created with te help of AI. Also I had to troubleshoot the movement constraints and direction reversing here ->
if x >= py5.width or x <= 0:
            self.speed *= -1  # Reverse speed direction
            x += self.speed
I had tried a lot of if-else and if-elif statements to get it to work and I would use AI to double check the math logic.
Everything else was written manually by me. Referencing my past code helped a lot. No help from peers this time.

Topics Mastery:
· Objects: Simon is an object!
· Loops: used to make multiple Simons and make them move
· Functions: Using them to display the Simons and make them move 
· Canvas Operations: Had to translate each 3D shape individually with push and pop matrix

Why Simon?:
I was inspired by a three.js website where butterflies fluttered over a grass plain. Instead of butterflies, I was inspired by Eve from
Wall-e and my previous creatures. Want to make cute creatures that seems alive. (Wish I had allocated more time to the project because
I could've made them interactive)

Basic Goals at this point in the semester:
· Write, run, and debug a simple Python script independently, without advanced IDE or AI aid. 
· Demonstrate a solid understanding of basic syntax and execution of Python/py5 
· Be comfortable with and perform simple operations with some core data types such as lists, strings, integers, Booleans 
· Use control flow statements like if-else and loops to solve small, contained problems 
· Write and call simple functions with parameters and return values 
· Showcase grasp of scope and reusability 
· Ensure code runs without syntax errors 
· Fix common mistakes such as indentation and type mismatches 
· Break down a small problem into steps and implement it in Python 
· Develop a procedural based problem solving way of thinking. 
I can comfortably say that I've hit all of these goals and can demonstrate mastery of them
'''

import py5
import random

# Global
total_simons = 20

class Simon:
    def __init__(self, x=None, y=None, z=0, speed=None, amplitude=(py5.height * 0.15), frequency=0.05, color=255, body_size=5):
        if y is None:
            y = py5.random(0.3 * py5.height, 0.8 * py5.height)  # randomize the starting y a bit
        self.initial_y = y
        if x is None:
            x = py5.width / 2 + py5.random(0, 0.4 * py5.width) # randomize the starting y a bit
        self.pos = py5.Py5Vector(x, y, z)
        if speed is None:
            speed = random.choice([-4, 4])  # randomize if it moves left or right at the start
        self.speed = speed
        self.amplitude = amplitude
        self.frequency = frequency
        self.color = color
        self.body_size = body_size

    def move(self):
        x = self.pos.x

        # Oscillate around the initial y position
        y = self.initial_y + self.amplitude * py5.sin(self.frequency * x)

        if x >= py5.width or x <= 0:
            self.speed *= -1  # Reverse speed direction
            x += self.speed
        
        x += self.speed  # Update position based on new speed

        # Update Simon's position
        self.pos.x = x
        self.pos.y = y

        # Display the Simon
        self.display()
            
    def display(self):
        # Overall styling
        py5.no_stroke()
        body_size = self.body_size

        # translate
        py5.push_matrix()
        py5.translate(self.pos.x, self.pos.y, self.pos.z)

        # BODY
        py5.fill(self.color)
        py5.sphere(body_size / 2)

        py5.pop_matrix()

        # --- EYES ---
        py5.fill(20)
        # Size
        eye_size = body_size * 0.1
        # Position
        eye_y = self.pos.y
        eye_z = self.pos.z + body_size * 0.5
        r_eye_x = -0.3 * body_size + self.pos.x
        l_eye_x = 0.3 * body_size + self.pos.x

        py5.push_matrix()
        py5.translate(r_eye_x, eye_y, eye_z)
        py5.sphere(eye_size)     # right eye
        py5.pop_matrix()

        py5.push_matrix()
        py5.translate(l_eye_x, eye_y, eye_z)
        py5.sphere(eye_size)     # left eye
        py5.pop_matrix()

        # ARMS
        py5.fill(self.color)
        # Size
        arm_length = body_size * 0.5
        arm_width = body_size * 0.35
        arm_depth = body_size * 0.1
        # Position
        r_arm_x = -arm_width - (body_size * 0.4) + self.pos.x        
        l_arm_x = self.pos.x + body_size * 0.7
        arm_y = self.pos.y + body_size * 0.4
        arm_z = self.pos.z
        
        py5.push_matrix()
        py5.translate(r_arm_x, arm_y, arm_z)
        py5.box(arm_width, arm_length, arm_depth)      # right arm
        py5.pop_matrix()

        py5.push_matrix()
        py5.translate(l_arm_x, arm_y, arm_z)
        py5.box(arm_width, arm_length, arm_depth)      # left arm
        py5.pop_matrix()

        
simons = []

def setup():
    py5.size(1600, 800, py5.P3D)
    
    z = 0
    body_size = 100
    amplitude = py5.height * 0.15
    frequency = 0.02
    color = 255

    for i in range(total_simons):
        # Update z position to be further from camera per simon
        z = -i * 3 * body_size

        simon = Simon(z=z, body_size=body_size, amplitude=amplitude, frequency=frequency, color=color)
        simons.append(simon)    # store simons into array

        # Update flight path for the different simons 
        amplitude -= 0.1 * amplitude
        frequency -= 0.1 * frequency

        # Update color to be darker as z position increases for fake depth
        color -= color / total_simons

def draw():
    py5.background(0)
    for simon in simons:
        simon.move()        # make them float around!!

py5.run_sketch()