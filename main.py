import pandas as pd
import psutil
import time

def temp_logger(temperature_package_id, temperature_core_0, temperature_core_1):
	d = psutil.sensors_temperatures()
	t1 = d["coretemp"][0][1]
	t2 = d["coretemp"][1][1]
	t3 = d["coretemp"][2][1]
	temperature_package_id.append(t1)
	temperature_core_0.append(t2)
	temperature_core_1.append(t3)
	print("Logged")
	time.sleep(2)

print(f"[INFO] Start {time.ctime()}")
run_time=[]
run_time.append(time.ctime())
global temperature_package_id
global temperature_core_0
global temperature_core_1
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
run_time.append(time.ctime()) 

df = pd.DataFrame(
	{
		"package_id": temperature_package_id,
		"core_0": temperature_core_0,
		"core_1": temperature_core_1
	}
)
df.to_csv("temp_log.csv")
print("[INFO] Data saved as temp_log.csv")