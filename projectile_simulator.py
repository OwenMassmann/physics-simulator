import math
import matplotlib.pyplot as plt
print("====================")
print("Projectile Simulator")
print("====================")
initial_velocity = float(input("Initial velocity (m/s): "))
initial_launch_angle = float(input("Initial launch angle (degrees): "))
initial_height = float(input("Initial height (m): "))
angle_radians = math.radians(initial_launch_angle)
angles = [15, 30, 45, 60, 75, initial_launch_angle]

plt.figure()
print("\nAngle Comparison:")
print("-------------------")
best_range = 0
best_angle = 0
for angle in angles:
    angle_radians = math.radians(angle)
    horizontal_velocity = initial_velocity * math.cos(angle_radians)
    vertical_velocity = initial_velocity * math.sin(angle_radians)
    gravity = 9.81
    a = -0.5 * gravity
    b = vertical_velocity
    c = initial_height
    discriminant = b**2 - 4*a*c
    time1 = (-b +math.sqrt(discriminant)) / (2*a)
    time2 = (-b - math.sqrt(discriminant)) / (2*a)
    if time1 > 0:
        flight_time = time1
    else:
        flight_time = time2
    print(f"{angle} degrees: Flight time = {flight_time:.2f} seconds")
    time_to_max_height = vertical_velocity / gravity
    maximum_height = initial_height + (vertical_velocity * time_to_max_height) - (0.5 * gravity * time_to_max_height**2)
    horizontal_range = horizontal_velocity * flight_time
    print(f"{angle} degrees: Max height = {maximum_height:.2f} m, Range = {horizontal_range:.2f} m")

    if horizontal_range > best_range:
        best_range = horizontal_range
        best_angle = angle

    times = []
    x_positions = []
    y_positions = []
    steps = 100
    time_step = flight_time / steps

    for i in range(steps + 1):
        t = i * time_step
        x = horizontal_velocity * t
        y = initial_height + (vertical_velocity * t) - (0.5 * gravity * t**2)
        times.append(t)
        x_positions.append(x)
        y_positions.append(y)

    plt.plot(x_positions, y_positions, label=f"{angle} degrees")
print(f"\nGreatest range: {best_range:.2f} m at {best_angle} degrees")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Height(m)")
plt.title("Projectile Motion")
plt.grid(True)
plt.legend()
plt.show() 
