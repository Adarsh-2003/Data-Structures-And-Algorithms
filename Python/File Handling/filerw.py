from datetime import datetime

timestamp = str(datetime.now())
filename = input("Enter file name: ")
file = open(filename + ".txt", "w")
file.write(timestamp + "\n")
file.close()

print("Timestamp here :", timestamp)