import csv
import psutil
import time

print(f"[INFO] Start {time.ctime()[11:19]}")

print("[INFO] Press Ctrl+c to stop")

fieldnames = []
fieldnames.append("time")
dic = psutil.sensors_temperatures()
for i in range(len(dic["coretemp"])):
	fieldnames.append(f"core_{i}")
fieldnames.append("ram")
fieldnames.append("fan")

with open("temp_log.csv", "w") as f:
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

	try:
		temperatures = []
		for i in range(len(dic["coretemp"])):
			temperatures.append(dic["coretemp"][i][1])
		ram = round(abs((psutil.virtual_memory().available * 100 / psutil.virtual_memory().total) - 100), 2)
		fan = list(psutil.sensors_fans().values())[0][0][1]
		current_time = time.ctime()[11:19]
		
		info = dict()
		info.update(
			{
				"time": current_time
			}
		)
		for i in range(len(temperatures)):
			info.update(
				{
					f"core_{i}": temperatures[i]
				}
			)
		info.update(
			{
				"ram": ram,
				"fan": fan
			}
		)

		with open("temp_log.csv", "a") as f:
			csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
			csv_writer.writerow(info)

		print(f"Logged {time.ctime()[11:19]}")

	except KeyboardInterrupt:
		print(f"\n[INFO] Stop {time.ctime()[11:19]}")
		break
	
	time.sleep(5)

f.close()

print("[INFO] Data saved as temp_log.csv")