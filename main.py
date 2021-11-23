import pandas as pd
import psutil
import time	

print(f"[INFO] Start {time.ctime()}")

time_lst = []
temperature_package_id_lst = []
temperature_core_0_lst = []
temperature_core_1_lst = []
ram_lst = []
fan_lst = []

print("[INFO] Press Ctrl+c to stop")

while True:

	try:
		d = psutil.sensors_temperatures()
		temperature_package_id = d["coretemp"][0][1]
		temperature_core_0 = d["coretemp"][1][1]
		temperature_core_1 = d["coretemp"][2][1]
		ram = abs((psutil.virtual_memory().available * 100 / psutil.virtual_memory().total) - 100)
		fan = list(psutil.sensors_fans().values())[0][0][1]
		current_time = time.ctime()

		time_lst.append(current_time)
		temperature_package_id_lst.append(temperature_package_id)
		temperature_core_0_lst.append(temperature_core_0)
		temperature_core_1_lst.append(temperature_core_1)
		ram_lst.append(ram)
		fan_lst.append(fan)

		print("Logged")
		time.sleep(5)

	except KeyboardInterrupt:
		print(f"\n[INFO] Stop {time.ctime()}")
		break

df = pd.DataFrame(
	{
		"time": time_lst,
		"package_id": temperature_package_id_lst,
		"core_0": temperature_core_0_lst,
		"core_1": temperature_core_1_lst,
		"ram": ram_lst,
		"fan": fan_lst
	}
)

print(f"Start: {time_lst[0]}	Stop: {time_lst[-1]}")

df = df[["time", "package_id", "core_0", "core_1", "ram", "fan"]]
df.to_csv("temp_log.csv")

print("[INFO] Data saved as temp_log.csv")

# TO DO
# Sperate graph for rpm and ram
# gitignore templog
# Live graphing?
# Full scale gui version?
# Full scale cli version?
# Name?
# Avoid ipynb?
# Full time logger from boot to shutdown
# Save in html
# Graph using js