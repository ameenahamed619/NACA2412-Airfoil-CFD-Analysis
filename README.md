# NACA 2412 Airfoil – CFD Analysis

## 1. Project Overview

This project investigates the aerodynamic performance of a NACA 2412 airfoil using ANSYS Fluent.

A two-dimensional external flow simulation is performed at Mach 0.6 to study the aerodynamic characteristics at different angles of attack.

The project focuses on flow-field analysis, pressure distribution, turbulence characteristics, aerodynamic coefficients, and mesh refinement.

## 2. Simulation Setup

| Parameter | Configuration |
|---|---|
| Airfoil | NACA 2412 |
| Simulation | 2D External Flow |
| Solver | Pressure-Based |
| Flow | Steady |
| Mach Number | 0.6 |
| Turbulence Model | k-ω SST |
| Working Fluid | Air |
| Software | ANSYS Fluent 2026 R1 |

## 3. Angles of Attack

The aerodynamic performance is investigated at the following angles of attack:

0°, 2°, 4°, 6°, 8°, 10°, and 12°.

## 4. Mesh Refinement Study

A mesh refinement study is conducted to evaluate the sensitivity of predicted aerodynamic coefficients to mesh resolution.

The study includes coarse, medium, and fine mesh configurations.

## 5. Results and Post-Processing

The following quantities are investigated:

- Lift coefficient (CL)
- Drag coefficient (CD)
- Lift-to-drag ratio (L/D)
- Velocity contours and streamlines
- Pressure distribution
- Turbulent kinetic energy
- Residual convergence
- Lift and drag coefficient convergence

## 6. Repository Structure

-  figures/AoA_4deg/` – Simulation setup documentation and CFD figures for 4° angle of attack.
- `figures/` – Project plots and visual results.
- `NACA2412_complete_analysis.py` – Python-based post-processing and aerodynamic analysis.
- `NACA2412_M0p6_AoA_results.csv` – Aerodynamic results dataset.

## 7. Tools and Technologies

- ANSYS Fluent
- ANSYS Meshing
- Python
- NumPy
- Pandas
- Matplotlib

## 8. Project Status

The 4° angle-of-attack simulation and associated post-processing figures have been documented.

Further work includes completing mesh-independence verification, documenting the remaining angles of attack, and comparing aerodynamic performance across the operating conditions.

---

**Project:** NACA 2412 Airfoil CFD Analysis  
**Focus:** Computational Fluid Dynamics | External Aerodynamics | Aerodynamic Performance
