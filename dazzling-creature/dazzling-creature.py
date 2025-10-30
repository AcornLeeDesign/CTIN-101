from turtle import right
import py5

# Global
total_simons = 2

class Simon:
    def __init__(self, x=0, y=(py5.height / 2), speed=1, amplitude=(py5.height * 0.15), frequency=0.05, body_size=5):
        self.pos = py5.Py5Vector(x, y)  # Original
        self.pos.x = x
        self.pos.y = y
        self.speed = speed
        self.amplitude = amplitude
        self.frequency = frequency
        self.body_size = body_size

    def move(self):
        x = self.pos.x
        speed = self.speed

        # Calculate the new y position using sine wave logic
        y = py5.height / 2 + self.amplitude * py5.sin(self.frequency * x)

        if x >= 0 and x < py5.width:
            x += speed      # Move to the right
        else:
            x = 0           # reset position to the left edge
        
        # Update Simon position
        self.pos.x = x
        self.pos.y = y

        # Display the Simon
        self.display()
            
    def display(self):
        # Overall styling
        py5.no_stroke()
        corner_radius = 8
        body_size = self.body_size

        # translate
        py5.push_matrix()
        py5.translate(self.pos.x, self.pos.y)

        # BODY
        py5.fill(255)
        py5.sphere(body_size / 2)

        # EYES
        py5.fill(0)
        # Size
        eye_size = body_size * 0.2
        # Position
        eye_y = -0.1 * body_size
        r_eye_x = -0.38 * body_size
        l_eye_x = 0.38 * body_size - eye_size

        py5.rect(r_eye_x, eye_y, eye_size, eye_size, corner_radius)     # right eye
        py5.rect(l_eye_x, eye_y, eye_size, eye_size, corner_radius)     # left eye

        # ARMS
        py5.fill(255)
        # Size
        arm_length = body_size * 0.5
        arm_width = body_size * 0.35
        # Position
        r_arm_x = -arm_width - (body_size * 0.4)        
        l_arm_x = body_size * 0.4
        arm_y = body_size * 0.4
        
        py5.rect(r_arm_x, arm_y, arm_width, arm_length, corner_radius)      # right arm
        py5.rect(l_arm_x, arm_y, arm_width, arm_length, corner_radius)      # left arm

        py5.pop_matrix()

simons = []

def setup():
    py5.size(800, 800, py5.P3D)

    amplitude = py5.height * 0.15
    frequency = 0.05

    for i in range(total_simons):
        simon = Simon(body_size=60, amplitude=amplitude, frequency=frequency)
        simons.append(simon)

        # Update flight path for the different simons 
        amplitude -= 0.1 * amplitude
        frequency -= 0.1 * frequency

def draw():
    py5.background(0)
    for simon in simons:
        simon.move()

py5.run_sketch()