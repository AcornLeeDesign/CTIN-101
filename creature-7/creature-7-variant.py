import py5

# Global variables
rotation_angle = 0
interest = None
velocity = 0
total_rings = 20

class Interest:
    def __init__(self, y_init_rotate, radius, total_balls, size=2):
        self.radius = radius
        self.total_balls = total_balls
        self.y_init_rotate = y_init_rotate
        self.size = size

    def make(self):
        global rotation_angle, velocity
        tension = 0.1    # How much the spring pulls
        damping = 0.9    # Reduces velocity over time (0 < damping < 1)

        # Calculate Speed
        distance_x = py5.mouse_x - py5.width / 2
        distance_y = py5.mouse_y - py5.height / 2
        speed_x = distance_x / 100000
        speed_y = distance_y / 100000

        # Determine which speed to use
        if abs(speed_x) > abs(speed_y):
            speed = speed_x
            rotation_axis = py5.rotate_y
        else:
            speed = speed_y
            rotation_axis = py5.rotate_x

        # Spring Effect
        target_angle = rotation_angle + speed
        force = (target_angle - rotation_angle) * tension
        velocity = (velocity + force) * damping
        rotation_angle += velocity

        # Transformation
        py5.push_matrix()
        py5.translate(py5.width / 2, py5.height / 2)
        rotation_axis(rotation_angle + self.y_init_rotate)

        self.display(self.radius, self.total_balls)

        py5.pop_matrix()

    def display(self, radius, total_balls):
        py5.no_stroke()
        for i in range(total_balls):
            angle = i * (py5.PI * 2) / total_balls
            x = radius * py5.cos(angle)
            y = radius * py5.sin(angle)

            # Ellipse 2
            py5.push_matrix()
            py5.translate(x, y)
            py5.rotate_y(py5.PI / 2)
            py5.fill(255)
            py5.sphere(self.size)
            py5.pop_matrix()

def setup():
    global interest, rotation_angle
    py5.size(800, 800, py5.P3D)

def draw():
    py5.background(0)
    y_init_rotate = 0
    radius = 50

    for i in range(total_rings):
        interest = Interest(y_init_rotate, radius, int(py5.random(8, 16)), py5.random(2, 3))
        interest.make()
        radius = radius + 30
        y_init_rotate += py5.PI / total_rings

    py5.fill(255)
    py5.ellipse(py5.width / 2, py5.height / 2, 40, 40)
        

py5.run_sketch()