from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

def animate(i):
    df = pd.read_csv("temp_log.csv")
    x = df["time"]
    y_core_0 = df["core_0"]
    y_core_1 = df["core_1"]
    y_core_2 = df["core_2"]
    y_ram = df["ram"]
    plt.cla()
    plt.plot(x, y_core_0, label="core_0")
    plt.plot(x, y_core_1, label="core_1")
    plt.plot(x, y_core_2, label="core_2")
    plt.plot(x, y_ram, label="ram")
    plt.xticks(rotation="vertical")
    plt.xlabel("Time")
    plt.ylabel("Temp in C / RAM %")
    plt.grid()
    plt.tight_layout()
    plt.legend(loc="upper left")
    ax = plt.gca()
    ax.set_ylim(bottom=0, top=100)

ani = FuncAnimation(plt.gcf(), animate, interval=5000)

plt.show()