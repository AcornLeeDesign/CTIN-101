import py5

def setup() {
    py5.size(800, 800)
    py5.rect_mode(py5.CENTER)
}

def draw() {
    py5.background(255)
    py5.fill(150)
    py5.rect()
}