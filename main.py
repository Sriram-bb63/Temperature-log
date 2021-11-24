import csv
import psutil
import time

print(f"[INFO] Start {time.ctime()[11:19]}")

print("[INFO] Press Ctrl+c to stop")

fieldnames = ["time", "package_id", "core_0", "core_1", "ram", "fan"]

with open("temp_log.csv", "w") as f:
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

	try:
		d = psutil.sensors_temperatures()
		temperature_package_id = d["coretemp"][0][1]
		temperature_core_0 = d["coretemp"][1][1]
		temperature_core_1 = d["coretemp"][2][1]
		ram = abs((psutil.virtual_memory().available * 100 / psutil.virtual_memory().total) - 100)
		fan = list(psutil.sensors_fans().values())[0][0][1]
		current_time = time.ctime()[11:19]

		with open("temp_log.csv", "a") as f:
			csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
			info = {
				"time": current_time,
				"package_id": temperature_package_id,
				"core_0": temperature_core_0,
				"core_1": temperature_core_1,
				"ram": ram,
				"fan": fan
			}
			csv_writer.writerow(info)

		print(f"Logged {time.ctime()[11:19]}")

	except KeyboardInterrupt:
		print(f"\n[INFO] Stop {time.ctime()[11:19]}")
		break
	
	time.sleep(5)

f.close()

print("[INFO] Data saved as temp_log.csv")

# TO DO
# Full scale gui version?
# Full scale cli version?
# Name?
# Full time logger from boot to shutdown
# Save in html
# Graph using js