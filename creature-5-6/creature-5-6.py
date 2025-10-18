import py5

def setup():
    py5.size(800, 800)
    global y_body, y_wings, speed, left_rotation_angle, right_rotation_angle, rotation_speed
    y_body = py5.height / 2
    y_wings = py5.height / 2
    speed = 1
    left_rotation_angle = 0
    right_rotation_angle = 0
    rotation_speed = 0.05
    py5.no_stroke()

def draw_bird(y_body, y_wings, speed):
    global left_rotation_angle, right_rotation_angle, rotation_speed
    py5.background(0)
    x = py5.width / 2

    # Lef Wing pivot point
    left_wing_x = x - 40
    wing_width, wing_height = 50, 30
    pivot_x_left = left_wing_x + wing_width / 2
    pivot_y = y_wings

    # Rotate Left Wing
    py5.push_matrix()
    py5.translate(pivot_x_left, pivot_y)
    py5.rotate(left_rotation_angle)
    py5.fill(100, 150, 200)
    py5.arc(-wing_width / 2, 0, wing_width, wing_height, py5.PI, 2 * py5.PI)
    py5.pop_matrix()

    # Right wing pivot point
    right_wing_x = x + 40
    pivot_x_right = right_wing_x - wing_width / 2

    # Rotate Right 
    py5.push_matrix()
    py5.translate(pivot_x_right, pivot_y)
    py5.rotate(-right_rotation_angle + py5.PI)
    py5.arc(-wing_width / 2, 0, wing_width, wing_height, 0, py5.PI)
    py5.pop_matrix()

    # Draw body
    body_diameter = 40
    py5.circle(x, y_body, body_diameter)

    # Update angles and positions
    left_rotation_angle += rotation_speed
    right_rotation_angle += rotation_speed
    if left_rotation_angle > py5.PI / 4 or left_rotation_angle < -py5.PI / 4:
        rotation_speed *= -1

    y_body += speed
    y_wings += speed
    if y_body > py5.height / 2 + 20 or y_body < py5.height / 2 - 20:
        speed *= -1

    return y_body, y_wings, speed

def draw():
    global y_body, y_wings, speed
    y_body, y_wings, speed = draw_bird(y_body, y_wings, speed)

py5.run_sketch()