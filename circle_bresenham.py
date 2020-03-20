from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)
    glPointSize(5)


def set_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def bresenham_circle_drawing(r):

    # posisi lingkaran

    x_position = -1
    y_position = -1

    r = 12
    x = 0
    y = r

    # decision parameter
    d = 3 - 2 * r

    set_pixel(x + x_position, y + y_position)

    while y > x:

        if d < 0:
            x += 1
            d += 4 * x + 6
        else:
            x += 1
            y -= 1
            d += (4 * (x - y)) + 10

        # Untuk pixel (x, y)

        # Quadrant 1
        set_pixel(x + x_position, y + y_position)

        # Quadrant 2
        set_pixel(x + x_position, -y + y_position)

        # Quadrant 3
        set_pixel(-x + x_position, -y + y_position)

        # Quadrant 4
        set_pixel(-x + x_position, y + y_position)

        # Untuk pixel (y, x)

        # Quadrant 1
        set_pixel(y + x_position, x + y_position)

        # Quadrant 2
        set_pixel(-y + x_position, x + y_position)

        # Quadrant 3
        set_pixel(-y + x_position, -x + y_position)

        # Quadrant 4
        set_pixel(y + x_position, -x + y_position)


def plotpoints():

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1.0, 1.0)

    glBegin(GL_LINES)

    glVertex2f(-100, 0)
    glVertex2f(100, 0)

    glVertex2f(0, -100)
    glVertex2f(0, 100)

    glEnd()

    bresenham_circle_drawing(40)

    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Bresenham Circle Drawing Algorithm")
    glutDisplayFunc(plotpoints)

    init()
    glutMainLoop()
    

main()