from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

def animate(i):
    df = pd.read_csv("temp_log.csv")
    x = df["time"]
    y = df["package_id"]
    plt.cla()
    plt.plot(x, y)

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.show()