import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

df = pd.read_csv("temp_log.csv")

x = iter(df["time"])
y_package_id = iter(df["package_id"])
y_core_0 = iter(df["core_0"])
y_core_1 = iter(df["core_1"])
# y_ram = iter(df["ram"])
# y_fan = iter(df["fan"])

x_plt = []
y_package_id_plt = []
y_core_0_plt = []
y_core_1_plt = []

def animate(i):
    x_plt.append(next(x))
    y_package_id_plt.append(next(y_package_id))
    y_core_0_plt.append(next(y_core_0))
    y_core_1_plt.append(next(y_core_1))
    plt.cla()
    plt.grid()
    plt.plot(x_plt, y_package_id_plt, label="package_id")
    plt.plot(x_plt, y_core_0_plt, label="core_0")
    plt.plot(x_plt, y_core_1_plt, label="core_1")
    plt.legend()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.show()