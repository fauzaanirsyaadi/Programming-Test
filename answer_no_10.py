import math

# input data
num_windows = 50
window_size = 1.5 # in meters
building_height = 30 # in meters
num_floors = 10
access_points = 2
cleaning_rate = 20 # in sq meters per hour
cleaning_equipment_cost = 5000 # per day

# calculate window area
window_area = window_size ** 2

# calculate total window area
total_window_area = num_windows * window_area

# calculate building surface area
building_surface_area = num_floors * building_height * 2

# calculate cleaning time in hours
cleaning_time_hours = total_window_area / cleaning_rate

# calculate cleaning time in days
cleaning_time_days = math.ceil(cleaning_time_hours / access_points / 8)

# calculate cleaning cost
cleaning_cost = cleaning_time_days * cleaning_equipment_cost

# print results
print("Number of days required to clean the windows:", cleaning_time_days)
print("Cleaning cost:", cleaning_cost)
