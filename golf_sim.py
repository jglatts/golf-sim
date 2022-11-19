"""
    Python program to demonstarate realtionship between
    the club face, path, and golf ball during the golf swing. 
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

class GolfSim:

    # Flags for club face position
    FACE_OPEN = 1 << 1
    FACE_CLOSED = 1 << 2
    FACE_SQUARE = 1 << 3

    """
        Golfsim Constructor
    """
    def __init__(self, swing_length=130, club_face=0):
        if swing_length > 130:
            return

        self.club_face = club_face
        self.x_center = 10
        self.x_ball = 10
        self.y_center = 6
        self.y_ball = 6
        self.fig, self.ax = plt.subplots()
        self.initPlot()

    """
        Setup the matplot graph
    """
    def initPlot(self):
        self.ax.set_title('Golf Path Sim')
        self.ax.set_xlim(-160,180)
        self.ax.set_ylim(-20,110)

    """
        Draw the center lines for the golf swing 
    """
    def drawCenterLines(self):
        y_line_len = 180    
        v_line_len = 100     
        y_line_center = (360 - y_line_len)/2
        v_line_center = (130 - v_line_len)/2

        self.ax.hlines(y=self.y_center, xmin=y_line_center-160, xmax=180-y_line_center, linewidth=2, color='g')
        self.ax.vlines(x=self.x_center, ymin=self.y_center, ymax=110-v_line_center, linewidth=2, color='b')

    """
        Draw the golf ball and update pos based on club face\path 
    """
    def drawBall(self, frame_number):
        y_ball = (self.y_ball) * frame_number 
        x_ball = (self.x_ball) * frame_number 

        new_pos = self.computeBallPath(x_pos=x_ball)
        if (self.club_face & GolfSim.FACE_OPEN):
            y_ball = new_pos
        elif (self.club_face & GolfSim.FACE_CLOSED):
            # somewhat working abit hacky thoy 
            x_ball = -x_ball
            y_ball = new_pos

        if frame_number == 0 or x_ball == 0:
            y_ball = self.y_ball
            x_ball = self.x_ball

        plt.scatter(x_ball, y_ball, s=2000, facecolor='none', edgecolor='peru')

    """
        Draw a ref line
    """
    def drawLine(self, deg=0):
        if (deg == 0): return 
        line_len = 100
        theta = (deg * np.pi) / 180

        x = np.cos(theta) * line_len
        y = np.sin(theta) * line_len
        start_points = [self.x_center, x]
        end_points = [self.y_center, y]
        plt.plot(start_points, end_points, 'bo', linestyle="--")

    """
        Compute the new ball pos 
    """
    def computeBallPath(self, x_pos):
        if (self.club_face & GolfSim.FACE_OPEN):
            theta = (30 * np.pi) / 180    # 30deg open club face
            print(f'New ball pos: {np.sin(theta) * x_pos}')
        elif (self.club_face & GolfSim.FACE_CLOSED):
            theta = (150 * np.pi) / 180    # 30deg closed club face
            print(f'New ball pos: {np.sin(theta) * x_pos}')

        return np.sin(theta) * x_pos            

    """
        Draws the full golf swing scene
        Will call the fn's to draw centerlines, draw ball, and draw club face 

        This methods gets directly called during matplot animation callback 
    """
    def drawScene(self, frame_number):
        self.ax.clear()
        self.initPlot()

        if (self.club_face & GolfSim.FACE_CLOSED):
            self.drawLine(deg=150)
        elif (self.club_face & GolfSim.FACE_OPEN):
            self.drawLine(deg=30)
        
        self.drawCenterLines()
        self.drawBall(frame_number)

    """
        Setup the animaton for matplotlib
    """
    def animate(self):
        anim = animation.FuncAnimation(self.fig, self.drawScene, frames=10, blit=False, repeat=True, interval=50)    
        plt.show()


