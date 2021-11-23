import psutil
import time	

print(f"[INFO] Start {time.ctime()[11:19]}")

print("[INFO] Press Ctrl+c to stop")

f = open("temp_log_1.csv", "w")
f.write("time,package_id,core_0,core_1,ram,fan")

while True:

	try:
		d = psutil.sensors_temperatures()
		temperature_package_id = d["coretemp"][0][1]
		temperature_core_0 = d["coretemp"][1][1]
		temperature_core_1 = d["coretemp"][2][1]
		ram = abs((psutil.virtual_memory().available * 100 / psutil.virtual_memory().total) - 100)
		fan = list(psutil.sensors_fans().values())[0][0][1]
		current_time = time.ctime()[11:19]

		f.write(f"\n{current_time},{temperature_package_id},{temperature_core_0},{temperature_core_1},{ram},{fan}")

		print(f"Logged {time.ctime()[11:19]}")
		time.sleep(5)

	except KeyboardInterrupt:
		print(f"\n[INFO] Stop {time.ctime()[11:19]}")
		break

f.close()

print("[INFO] Data saved as temp_log.csv")

# TO DO
# gitignore templog
# Full scale gui version?
# Full scale cli version?
# Name?
# Avoid ipynb?
# Full time logger from boot to shutdown
# Save in html
# Graph using js