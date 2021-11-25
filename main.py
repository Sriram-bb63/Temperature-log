import os

live_graph = input("[INFO] Live graph (y/n): ")
if live_graph == "y":
    print("""
    The logger (logger.py) and the graph (graph.py) are 2 separate processes run by main.py
    Ending one will not end the other.

    ps: close the terminal and if it doesn't work, use htop
    """)
    os.system("python logger.py & python graph.py")
else:
    os.system("python logger.py")