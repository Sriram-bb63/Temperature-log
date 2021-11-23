import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

df = pd.read_csv("temp_log.csv")

x = iter(df["time"])
y = iter(df["package_id"])

x_plt = []
y_plt = []

def animate(i):
    x_plt.append(next(x))
    y_plt.append(next(y))
    plt.cla()
    plt.grid()
    plt.plot(x_plt, y_plt)

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.show()