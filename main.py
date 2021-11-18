import pandas as pd
import psutil
import time

def temp_logger():
	d = psutil.sensors_temperatures()
	t1 = d["coretemp"][0][1]
	t2 = d["coretemp"][1][1]
	t3 = d["coretemp"][2][1]
	time_lst.append(time.ctime())
	temperature_package_id.append(t1)
	temperature_core_0.append(t2)
	temperature_core_1.append(t3)
	print("Logged")
	time.sleep(2)

print(f"[INFO] Start {time.ctime()}")
global time_lst
global temperature_package_id
global temperature_core_0
global temperature_core_1
time_lst = []
temperature_package_id = []
temperature_core_0 = []
temperature_core_1 = []
print("[INFO] Press Ctrl+c to stop")
while True:
	try:
		temp_logger(temperature_package_id, temperature_core_0, temperature_core_1)
	except KeyboardInterrupt:
		print(f"\n[INFO] Stop {time.ctime()}")
		break
df = pd.DataFrame(
	{
		"time": time_lst,
		"package_id": temperature_package_id,
		"core_0": temperature_core_0,
		"core_1": temperature_core_1
	}
)
print(f"Start: {time_lst[0]}	Stop: {time_lst[-1]}")
df.to_csv("temp_log.csv")
print("[INFO] Data saved as temp_log.csv")