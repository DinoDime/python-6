count = 0
total = 0
filename = input("Enter file name: ")
filehandle = open(filename)
for line in filehandle:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        number = line[20:]
        number = float(number)
        total = total + number
        count = count + 1
average = total/count
print("Average spam confidence:", average)
