# NACA 2412 Airfoil CFD Analysis
# Mach 0.6; AoA = 0, 2, 4, 6, 8, 10, 12 degrees
# NOTE: These are approximate values used in our earlier plotting session.
# Replace them with exact Fluent report values before publishing.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. CFD data
aoa = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
CL = np.array([0.252, 0.500, 0.720, 0.920, 1.040, 1.040, 0.990])
CD = np.array([0.0105, 0.0123, 0.0188, 0.0290, 0.0500, 0.0770, 0.1080])

# 2. Lift-to-drag ratio
LD = CL / CD

# 3. Results table and CSV export
results = pd.DataFrame({
    "Angle of Attack (deg)": aoa,
    "Lift Coefficient (CL)": CL,
    "Drag Coefficient (CD)": CD,
    "Lift-to-Drag Ratio (L/D)": LD
})
print("\nCFD RESULTS TABLE")
print(results.to_string(index=False))
results.to_csv("NACA2412_M0p6_AoA_results.csv", index=False)

# 4. CL vs angle of attack
plt.figure()
plt.plot(aoa, CL, marker="o")
plt.xlabel("Angle of Attack (degrees)")
plt.ylabel("Lift Coefficient (CL)")
plt.title("NACA 2412: CL vs Angle of Attack")
plt.grid(True)
plt.savefig("CL_vs_AoA.png", dpi=300, bbox_inches="tight")
plt.show()

# 5. CD vs angle of attack
plt.figure()
plt.plot(aoa, CD, marker="o")
plt.xlabel("Angle of Attack (degrees)")
plt.ylabel("Drag Coefficient (CD)")
plt.title("NACA 2412: CD vs Angle of Attack")
plt.grid(True)
plt.savefig("CD_vs_AoA.png", dpi=300, bbox_inches="tight")
plt.show()

# 6. Drag polar
plt.figure()
plt.plot(CL, CD, marker="o")
plt.xlabel("Lift Coefficient (CL)")
plt.ylabel("Drag Coefficient (CD)")
plt.title("NACA 2412: Drag Polar")
plt.grid(True)
plt.savefig("drag_polar.png", dpi=300, bbox_inches="tight")
plt.show()

# 7. L/D vs angle of attack
plt.figure()
plt.plot(aoa, LD, marker="o")
plt.xlabel("Angle of Attack (degrees)")
plt.ylabel("Lift-to-Drag Ratio (L/D)")
plt.title("NACA 2412: L/D vs Angle of Attack")
plt.grid(True)
plt.savefig("L_D_vs_AoA.png", dpi=300, bbox_inches="tight")
plt.show()

# 8. Lift curve slope and zero-lift angle (using 0 to 6 degrees)
linear_mask = aoa <= 6
slope_deg, intercept = np.polyfit(aoa[linear_mask], CL[linear_mask], 1)
slope_rad = slope_deg * (180.0 / np.pi)
zero_lift_aoa = -intercept / slope_deg

print("\nLIFT CURVE ANALYSIS")
print(f"Lift curve slope = {slope_deg:.4f} per degree")
print(f"Lift curve slope = {slope_rad:.4f} per radian")
print(f"Estimated zero-lift AoA = {zero_lift_aoa:.3f} degrees")

# 9. Maximum lift coefficient and indicative lift reduction
max_index = np.argmax(CL)
max_CL = CL[max_index]
max_CL_aoa = aoa[max_index]
lift_drop = (max_CL - CL[-1]) / max_CL * 100.0

print("\nMAXIMUM LIFT ANALYSIS")
print(f"Maximum CL = {max_CL:.3f}")
print(f"First AoA at maximum CL = {max_CL_aoa:.1f} degrees")
print(f"CL reduction at {aoa[-1]:.1f} degrees = {lift_drop:.2f}%")
# A reliable stall angle needs finer AoA increments and convergence checks.

# 10. Drag polar fit: CD = CD0 + k*CL^2 (all points)
CL2 = CL ** 2
k_all, CD0_all = np.polyfit(CL2, CD, 1)
CD_fit_all = CD0_all + k_all * CL2
ss_res = np.sum((CD - CD_fit_all) ** 2)
ss_tot = np.sum((CD - np.mean(CD)) ** 2)
r2_all = 1 - ss_res / ss_tot

print("\nDRAG POLAR FIT - ALL DATA")
print(f"CD0 = {CD0_all:.5f}")
print(f"k = {k_all:.5f}")
print(f"R-squared = {r2_all:.4f}")

# 11. Pre-stall fit (0 to 8 degrees)
pre = aoa <= 8
k_pre, CD0_pre = np.polyfit(CL2[pre], CD[pre], 1)
CD_fit_pre = CD0_pre + k_pre * CL2[pre]
ss_res_pre = np.sum((CD[pre] - CD_fit_pre) ** 2)
ss_tot_pre = np.sum((CD[pre] - np.mean(CD[pre])) ** 2)
r2_pre = 1 - ss_res_pre / ss_tot_pre

print("\nPRE-STALL DRAG POLAR FIT (0 TO 8 DEGREES)")
print(f"CD0 = {CD0_pre:.5f}")
print(f"k = {k_pre:.5f}")
print(f"R-squared = {r2_pre:.4f}")

CL_line = np.linspace(CL[pre].min(), CL[pre].max(), 100)
CD_line = CD0_pre + k_pre * CL_line
plt.figure()
plt.scatter(CL[pre], CD[pre], label="CFD data")
plt.plot(CL_line, CD_line, label="Pre-stall quadratic fit")
plt.xlabel("Lift Coefficient (CL)")
plt.ylabel("Drag Coefficient (CD)")
plt.title("Pre-stall Drag Polar Fit")
plt.grid(True)
plt.legend()
plt.savefig("pre_stall_drag_polar_fit.png", dpi=300, bbox_inches="tight")
plt.show()

# 12. Oswald efficiency demonstration only.
# AR=6 was a placeholder. This is NOT physically valid for a 2D airfoil.
AR_placeholder = 6.0
if k_pre > 0:
    e_placeholder = 1 / (np.pi * AR_placeholder * k_pre)
    print("\nOPTIONAL DEMONSTRATION ONLY")
    print(f"Placeholder AR = {AR_placeholder:.1f}; calculated e = {e_placeholder:.3f}")
    print("Do not report this as a physical Oswald efficiency factor for 2D CFD.")

# 13. Compare with thin-airfoil theory
theory_slope = 2 * np.pi
difference = abs(slope_rad - theory_slope) / theory_slope * 100

print("\nTHIN-AIRFOIL THEORY COMPARISON")
print(f"Theoretical slope (2*pi) = {theory_slope:.4f} per radian")
print(f"Estimated CFD slope = {slope_rad:.4f} per radian")
print(f"Percentage difference = {difference:.2f}%")
# Thin-airfoil theory is idealized and incompressible; Mach 0.6 CFD is
# compressible and viscous, so this is a qualitative comparison.

print("\nAnalysis complete. CSV and plots saved in the same folder as this script.")
