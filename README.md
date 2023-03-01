# Closeest Pair of Points in 3D space
> Second mini-project for Algorithm Strategies (IF2211) course from School of Electrical Engineering and Informatics, Bandung Institute of Technology

## Table of Contents
* [General Information](#general-information)
* [Prerequisites](#prerequisites)
* [Libraries Used](#libraries-used)
* [Local Setup](#local-setup)
* [Features](#features)
* [Project Structure](#project-structure)
* [Author](#author)

## General Information
A program made in python which searches the closest pair of random points. This program applies and compares Brute-Force Algorithm and Divide & Conquer Algorithm. It will show the time difference and the amount of euclidean distance calculated. It will also show that both algorithm is still applicable for this problem despite different algorithm and complexity by returning the shortest distance and the pair's coordinates.

## Prerequisites
- Python
- Matplotlib

## Libraries Used
- math
- platform
- pyplot
- random
- time

## Local Setup
1. Clone this repository (first-time use only)
<br>```git clone https://github.com/kennypanjaitan/Tucil2_13521023.git```<p>
2. Run the program
<br>```./run.bat```<p>

## Features
- User can input amount of points inside the space and dimension of the space
- Program will generate random points
- Program will show the closest pair of points and the distance between them by using Brute-Force Algorithm and Divide & Conquer Algorithm

## Project Structure
```bash
.
├── bin ------------------------------------------ Folder containing executable binary files
├── docs ----------------------------------------- Folder containing documents for this project
├── src ------------------------------------------ Folder containing source code files
│   ├── algorithms.py
│   ├── functions.py
│   ├── main.py
│   ├── plot.py
│ 
├── README.md
├── run.bat -------------------------------------- Executable batch file (main program)
```

## Author
Created by Kenny Benaya Nathan (13521023)