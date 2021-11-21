import pandas as pd
import psutil
import time

def temp_logger():
	d = psutil.sensors_temperatures()
	temperature_package_id = d["coretemp"][0][1]
	temperature_core_0 = d["coretemp"][1][1]
	temperature_core_1 = d["coretemp"][2][1]
	ram = (psutil.virtual_memory().available * 100 / psutil.virtual_memory().total) - 100
	time_lst.append(time.ctime())
	temperature_package_id_lst.append(temperature_package_id)
	temperature_core_0_lst.append(temperature_core_0)
	temperature_core_1_lst.append(temperature_core_1)
	ram_lst.append(ram)
	print("Logged")
	time.sleep(5)

print(f"[INFO] Start {time.ctime()}")
global time_lst
global temperature_package_id_lst
global temperature_core_0_lst
global temperature_core_1_lst
global ram_lst
time_lst = []
temperature_package_id_lst = []
temperature_core_0_lst = []
temperature_core_1_lst = []
ram_lst = []
print("[INFO] Press Ctrl+c to stop")
while True:
	try:
		temp_logger()
	except KeyboardInterrupt:
		print(f"\n[INFO] Stop {time.ctime()}")
		break
df = pd.DataFrame(
	{
		"time": time_lst,
		"package_id": temperature_package_id_lst,
		"core_0": temperature_core_0_lst,
		"core_1": temperature_core_1_lst,
		"ram": ram_lst
	}
)
print(f"Start: {time_lst[0]}	Stop: {time_lst[-1]}")
df.to_csv("temp_log.csv")
print("[INFO] Data saved as temp_log.csv")