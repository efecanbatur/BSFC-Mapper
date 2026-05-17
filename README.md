# BSFC Map Generator

## Overview
BFSC.py Generates a synthetic Brake Specific Fuel Consumption (BSFC) contour map, modeled for the 75 HP engine of a 2013 Opel Corsa 1.3 CDTi by default. 

## What is BSFC?
Brake Specific Fuel Consumption is a metric that evaluates the thermodynamic efficiency of an internal combustion engine. It measures how much fuel mass the engine consumes to produce one unit of mechanical energy, expressed in grams per kilowatt-hour (g/kWh). Lower numbers indicate higher efficiency. 

## What This Code Does

This Python script mathematically approximates and visualizes the engine's fuel efficiency across its entire RPM and load range. It utilizes `numpy` and `scipy.interpolate` to:
* Generate a smooth maximum torque curve based on the engine's physical limits.
* Mask out mathematically generated points that exceed the engine's real-world capabilities.
* Dynamically locate and plot the exact operating coordinate for **Best Fuel Efficiency** (minimum fuel waste).
* Dynamically calculate and plot the coordinate for **Best Acceleration** (peak mechanical power).

## Output
Below is the generated contour map demonstrating the engine's efficiency zones and physical limits:

![BSFC Contour Map](bfsc_map.png)

<img width="2440" height="1638" alt="bfsc_map" src="https://github.com/user-attachments/assets/76def27c-c18f-41cd-b803-3015ef7d8125" />
