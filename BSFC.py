import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# input torque - RPM curve
rpms = np.array([1000, 1250, 1500, 1750, 2000, 
                 2250, 2500, 2750, 3000, 3250, 
                 3500, 3750, 4000, 4250, 4500])

torques = np.array([
    109.8, 139.6, 165.4, 189.8, 189.8, 
    189.8, 184.4, 177.6, 165.4, 150.5, 
    139.6, 127.4, 119.3, 104.4, 94.9
])

smooth_curve_function = CubicSpline(rpms, torques)
rpm_points_50 = np.linspace(1000, 4500, 50)
max_torque_nm_50 = smooth_curve_function(rpm_points_50)

rpm_grid = np.linspace(1000, 4500, 1000) 
torque_grid = np.linspace(0, 200, 1000)
X, Y = np.meshgrid(rpm_grid, torque_grid)
Z = 205 + (((X - 2000)/1000)**2)*30 + (((Y - 170)/50)**2)*40

mask = Y > smooth_curve_function(X)
Z[mask] = np.nan 

min_index = np.unravel_index(np.nanargmin(Z), Z.shape)
eff_rpm = X[min_index]
eff_torque = Y[min_index]

power_kw = max_torque_nm_50 * rpm_points_50 * (np.pi / 30000)
max_power_idx = np.argmax(power_kw)
accel_rpm = rpm_points_50[max_power_idx]
accel_torque = max_torque_nm_50[max_power_idx]

plt.figure(figsize=(10, 6))

contour_filled = plt.contourf(X, Y, Z, levels=15, cmap='RdYlGn_r')
cbar = plt.colorbar(contour_filled)
cbar.set_label('BSFC (g/kWh)')

plt.plot(rpm_points_50, max_torque_nm_50, color='red', linewidth=3, label='Max Torque Curve')
plt.plot(eff_rpm, eff_torque, marker='o', color='blue', markersize=8, label=f'Best Fuel Efficiency\n({eff_rpm:.0f} RPM, {eff_torque:.0f} Nm)')
plt.plot(accel_rpm, accel_torque, marker='o', color='purple', markersize=8, label=f'Best Acceleration\n({accel_rpm:.0f} RPM, {accel_torque:.0f} Nm)')
plt.title('BSFC Contour Map - Opel Corsa 1.3 CDTi')
plt.xlabel('Engine Speed (RPM)')
plt.ylabel('Engine Torque (Nm)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig('bfsc_map.png', dpi=300, bbox_inches='tight')