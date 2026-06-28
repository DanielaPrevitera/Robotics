import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("imu.csv")

# Tempo in secondi
t = df["stamp_sec"].to_numpy(dtype=float) + df["stamp_nanosec"].to_numpy(dtype=float) * 1e-9
t = t - t[0]

# Converto anche i dati in numpy array
ax = df["linear_acceleration_x"].to_numpy(dtype=float)
ay = df["linear_acceleration_y"].to_numpy(dtype=float)
az = df["linear_acceleration_z"].to_numpy(dtype=float)

wx = df["angular_velocity_x"].to_numpy(dtype=float)
wy = df["angular_velocity_y"].to_numpy(dtype=float)
wz = df["angular_velocity_z"].to_numpy(dtype=float)

# Plot accelerazioni
plt.figure()
plt.plot(t, ax, label="ax")
plt.plot(t, ay, label="ay")
plt.plot(t, az, label="az")
plt.xlabel("Tempo [s]")
plt.ylabel("Accelerazione [m/s²]")
plt.title("Accelerazioni IMU")
plt.grid(True)
plt.legend()

# Plot velocità angolari
plt.figure()
plt.plot(t, wx, label="wx")
plt.plot(t, wy, label="wy")
plt.plot(t, wz, label="wz")
plt.xlabel("Tempo [s]")
plt.ylabel("Velocità angolare [rad/s]")
plt.title("Velocità angolari IMU")
plt.grid(True)
plt.legend()

plt.show()
