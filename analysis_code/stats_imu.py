import pandas as pd

df = pd.read_csv("imu.csv")

cols = [
    "angular_velocity_x",
    "angular_velocity_y",
    "angular_velocity_z",
    "linear_acceleration_x",
    "linear_acceleration_y",
    "linear_acceleration_z"
]

stats = df[cols].agg(["mean", "std", "min", "max"])

print("\nStatistiche IMU:\n")
print(stats)

stats.to_csv("stats_imu.csv")

print("\nSalvato in stats_imu.csv")
