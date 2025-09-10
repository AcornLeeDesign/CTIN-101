import py5

particles = []
bnd = (0, 0, 200, 200)
particles_layer = None
monster_layer = None

class Particle:
    def __init__(self, x, y, size=5):
        self.pos = py5.Py5Vector(x, y)
        self.vel = py5.Py5Vector(py5.random(-2, 2), py5.random(-2, 2))
        self.size = size

    def move(self):
        self.pos += self.vel

    def edges(self, x_min, y_min, x_max, y_max):
        r = self.size / 2
        if self.pos.x - r < x_min or self.pos.x + r > x_max:
            self.vel.x *= -1
            self.pos.x = max(x_min + r, min(self.pos.x, x_max - r))
        if self.pos.y - r < y_min or self.pos.y + r > y_max:
            self.vel.y *= -1
            self.pos.y = max(y_min + r, min(self.pos.y, y_max - r))

    def display(self, layer):
        layer.fill(255)
        layer.no_stroke()
        layer.ellipse(self.pos.x, self.pos.y, self.size, self.size)


def settings():
    py5.size(200, 200)


def setup():
    global particles_layer, monster_layer, monster

    for _ in range(300):
        x = py5.random(bnd[0], bnd[2])
        y = py5.random(bnd[1], bnd[3])
        particles.append(Particle(x, y))

    particles_layer = py5.create_graphics(py5.width, py5.height)
    monster_layer = py5.create_graphics(py5.width, py5.height)

    monster = Particle(py5.width / 2, py5.height / 2, size = 80)
    monster.vel = py5.Py5Vector(py5.random(-2, 2), py5.random(-2, 2))


def draw():
    py5.background(30)

    py5.no_fill()
    py5.stroke(30)
    py5.rect(bnd[0], bnd[1], bnd[2] - bnd[0], bnd[3] - bnd[1])

    particles_layer.begin_draw()
    particles_layer.clear()
    for p in particles:
        p.move()
        p.edges(*bnd)
        p.display(particles_layer)
    particles_layer.end_draw()

    py5.image(particles_layer, 0, 0)

    monster.move()
    monster.edges(*bnd)

    monster_layer.begin_draw()
    monster_layer.clear()
    monster_layer.fill(255)
    monster_layer.no_stroke()
    monster_layer.ellipse(monster.pos.x, monster.pos.y, monster.size, monster.size)

    eye_offset_x = 15
    eye_offset_y = -20
    eye_size = 15
    monster_layer.fill(0)
    monster_layer.ellipse(monster.pos.x - eye_offset_x, monster.pos.y + eye_offset_y, eye_size, eye_size)
    monster_layer.ellipse(monster.pos.x + eye_offset_x, monster.pos.y + eye_offset_y, eye_size, eye_size)

    mouth_width = 20
    mouth_height = 10
    mouth_pos_x = monster.pos.x
    mouth_pos_y = monster.pos.y
    monster_layer.triangle(
        mouth_pos_x - mouth_width/2, 
        mouth_pos_y, 
        mouth_pos_x + mouth_width/2, 
        mouth_pos_y, 
        mouth_pos_x, 
        mouth_pos_y + mouth_height)

    body_width = 40
    body_height = 40
    body_pos_x = monster.pos.x - 20
    body_pos_y = monster.pos.y + 42
    monster_layer.fill(255)
    monster_layer.rect(
        body_pos_x, 
        body_pos_y, 
        body_width,
        body_height
        )

    arm_L_width = 20
    arm_L_height = 60
    arm_L_pos_x = monster.pos.x - 42
    arm_L_pos_y = monster.pos.y + 42
    monster_layer.fill(255)
    monster_layer.rect(
        arm_L_pos_x, 
        arm_L_pos_y, 
        arm_L_width,
        arm_L_height
        )

    arm_R_width = 20
    arm_R_height = 60
    arm_R_pos_x = monster.pos.x + 22
    arm_R_pos_y = monster.pos.y + 42
    monster_layer.fill(255)
    monster_layer.rect(
        arm_R_pos_x, 
        arm_R_pos_y, 
        arm_R_width,
        arm_R_height
        )

    leg_L_width = 19
    leg_L_height = 30
    leg_L_pos_x = monster.pos.x - 20
    leg_L_pos_y = monster.pos.y + 85
    monster_layer.fill(255)
    monster_layer.rect(
        leg_L_pos_x, 
        leg_L_pos_y, 
        leg_L_width,
        leg_L_height
        )

    leg_R_width = 19
    leg_R_height = 30
    leg_R_pos_x = monster.pos.x
    leg_R_pos_y = monster.pos.y + 85
    monster_layer.fill(255)
    monster_layer.rect(
        leg_R_pos_x, 
        leg_R_pos_y, 
        leg_R_width,
        leg_R_height
        )

    monster_layer.end_draw()

    py5.image(monster_layer, 0, 0)


py5.run_sketch()
