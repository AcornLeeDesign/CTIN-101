import py5

# Global variables
rotation_angle = 0
interest = None
velocity = 0

class Interest:
    def __init__(self, size=10):
        self.size = size

    def move(self):
        global rotation_angle, velocity
        tension = 0.1    # How much the spring pulls
        damping = 0.9    # Reduces velocity over time (0 < damping < 1)

        # Apply spring mechanics
        target_angle = rotation_angle + 0.02  # Modify target for constant motion
        force = (target_angle - rotation_angle) * tension
        velocity = (velocity + force) * damping
        rotation_angle += velocity

        # Apply transformations
        py5.push_matrix()
        py5.translate(py5.width / 2, py5.height / 2)
        py5.rotate_y(rotation_angle)

        self.display(50)  # Draw within the rotated matrix

        py5.pop_matrix()

    def display(self, radius):
        total_circles = 10
        for i in range(total_circles):
            angle = i * (py5.PI * 2) / total_circles
            x = radius * py5.cos(angle)
            y = radius * py5.sin(angle)

            # Ellipse 1
            py5.ellipse(x, y, self.size, self.size)

            # Ellipse 2
            py5.push_matrix()
            py5.translate(x, y)
            py5.rotate_y(py5.PI / 2)
            py5.ellipse(0, 0, self.size, self.size)
            py5.pop_matrix()

def setup():
    global interest, rotation_angle
    py5.size(800, 800, py5.P3D)  # Use P3D for 3D transformations
    interest = Interest()

def draw():
    py5.background(0)
    interest.move()  # Move now encapsulates drawing

py5.run_sketch()