hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
start_time = hour * 60 + mins
end_time = start_time + dura
end_hours = (end_time // 60) % 24
end_mins = end_time % 60

end_time_str = str(end_hours) + ":" + str(end_mins)
print(end_time_str)
