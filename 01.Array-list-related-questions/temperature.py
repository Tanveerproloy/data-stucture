#finding number of days with temperature above a average temperature

numDays = int(input("Enter How many days of temperature data you have: "))
total = 0
temp = [] 

for i in range(numDays):
    nextDay =int(input("Day" + str(i+1) +"_ 's high temperature: "))
    temp.append(nextDay)
    total += temp[i]
     

avg = round(total/numDays,2)
print(f"\nAverage = {avg}")

above = 0
for i in temp:
    if i > avg:
        above += 1

print(f"{above} days temperature was above average.")