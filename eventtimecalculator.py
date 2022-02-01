hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

minutes = (mins+dura) % 60
hours = int((hour + (mins + dura)/60)) %24

print("the event starts at" ,hour,":",mins,"and ends at",hours,":",minutes)
input()