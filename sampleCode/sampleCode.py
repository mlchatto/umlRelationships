#global variables
speed=float(input("Please input your speed in km/h: "))
dis=42.195
time=dis/speed
mins=(time%1)*60

#my function
def calcu_marathon(speed):
    #local variables
    h=dis//speed
    m=int(mins)
    print("Going ",speed, "km/h it will take approximately ",h , "hours, and ",m, " mins to finish the race.")
print(calcu_marathon(speed))
