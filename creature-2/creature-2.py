import py5

tinies = []

class Tiny:
    # Set the Tiny's start position, velocity, and size
    def __init__(self, pw, ph, pd, size = 20):
        self.size = size
        self.pos = py5.Py5Vector(py5.random(pd, ph-pd), py5.random(pd, ph-pd))
        self.vel = py5.Py5Vector(0, 0)

    # Move the Tiny according to the mouse movement
    def move(self, direction, speed, position):
        # the hitbox is the size of the object
        hitbox = self.size

        # If mouse detected within the hitbox, move it according to its speed and direction
        if (position[0] >= self.pos.x - hitbox and position[0] <= self.pos.x + hitbox):
            if (position[1] >= self.pos.y - hitbox and position[1] <= self.pos.y + hitbox):
                # Do not try to perform math operation or moddify speed/direction when mouse isn't moving
                if (direction[0] == 0 and direction[1] == 0):
                    self.vel = py5.Py5Vector(0, 0)
                else:
                    # Normalize if not 0 
                    self.vel = py5.Py5Vector(direction[0], direction[1]).normalize() * speed
                self.pos += self.vel
    
    # This is what will be drawn/displayed
    def display(self):
        # Save the current transform
        py5.push_matrix()

        # Move the origin of the canvas to the center of the Tiny
        py5.translate(self.pos.x, self.pos.y)

        # Apply vibration
        py5.rotate(py5.radians(py5.random(0, 5)))

        # Draw the Tiny at the new origin
        py5.fill(255)
        py5.no_stroke()
        py5.ellipse(0, 0, self.size, self.size)
        py5.arc(0, -20, self.size, self.size, 0, py5.PI)
        py5.ellipse(-15, 0, self.size - 10, self.size - 10)
        py5.ellipse(15, 0, self.size - 10, self.size - 10)
        py5.ellipse(-4, 15, self.size - 12, self.size - 12)
        py5.ellipse(4, 15, self.size - 12, self.size - 12)

        # Restore the previous transform
        py5.pop_matrix()

# The mouse movement properties are calculated and returned.
def mouse_move():
    # Find mouse direction
    mdx = py5.mouse_x - py5.prev_mouse_x
    mdy = py5.mouse_y - py5.prev_mouse_y

    # Calculate mouse speed
    ms = (mdx**2 + mdy**2)**0.5

    # Reset the previous position as the new position to run through again
    py5.prev_mouse_x = py5.mouse_x
    py5.prev_mouse_y = py5.mouse_y


    # Return as a dictionary    
    return {
        'direction': (mdx, mdy),
        'speed': ms,
        'position': (py5.mouse_x, py5.mouse_y)
    }

# Setup
def setup():
    # Canvas size and padding
    py5.size(800, 800)
    pw = py5.width
    ph = py5.height
    pd = 100
    
    # Initial mouse position for the first frame 
    py5.prev_mouse_x = py5.mouse_x
    py5.prev_mouse_y = py5.mouse_y

    # Create all the Tinies!!
    for i in range(70):
        tinies.append(Tiny(pw, ph, pd))

# Draw on Canvas
def draw():
    # Background color
    py5.background(0)
    # Set the mouse moving object thing
    m = mouse_move()

    # Display the Tinies
    for t in tinies:
        t.move(m['direction'], m['speed'], m['position'])
        t.display()

py5.run_sketch()