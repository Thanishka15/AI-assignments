# AI Assignments

This repository contains implementations of various Artificial Intelligence concepts such as intelligent agents, search algorithms, and human verification systems.

---

# 1. AQI Intelligent Agent

## Description
This project implements an **Air Quality Index (AQI) intelligent agent** that evaluates the air quality of different locations. The agent retrieves real-time air pollution data using the OpenWeather Air Pollution API, computes AQI sub-indices for different pollutants, and determines the overall AQI category.

By processing environmental data, the system classifies air quality into standard AQI categories such as **Good, Moderate, Poor**, and other defined levels.

## Data Source
The system uses the **OpenWeather Air Pollution API** to obtain real-time pollutant concentration data for specific geographic locations using their **latitude and longitude coordinates**.

The API provides concentration levels for several major pollutants, including **PM2.5, PM10, NO₂, O₃, CO, SO₂, and NH₃**.

These pollutant values are then used together with **standard AQI breakpoint tables** to calculate the final AQI value.

## Components
- `code.py` – Main implementation of the AQI intelligent agent  
- `config.py` – Contains configuration details such as API key and location data  
- `aqi_categories.csv` – Defines AQI categories and their ranges  
- `aqi_checkpoints.csv` – Dataset used for AQI calculations and testing  

## Agent Architecture
The AQI system follows a **Simple Reflex Agent architecture**:

1. The **sensor** collects pollutant concentration data from the API.  
2. The **agent** processes this data using predefined AQI classification rules.  
3. The **actuator** outputs the corresponding air quality category.

-------
# 2. Turing test and Captcha

## Turing test

### Description
It is a test to differentiate between humans and computers 

### Architecture
1. Judge Interface
2. Conversation Manager
3. Human Agent
4. AI Agent
5. Evaluator

### Implementation
- `turingtest.py`

The system displays responses in a random order, and the judge must determine whether the response was produced by a machine or a human.

---

## CAPTCHA System

### Description
This project implements a basic CAPTCHA generator that produces distorted text images and checks the user’s input to differentiate between human users and automated bots.


### Features
- Generates random CAPTCHA strings
- Creates CAPTCHA images from the generated text
- Adds noise lines and distortions to make automated recognition difficult
- Verifies user input against the generated CAPTCHA

### Architecture

1. **CAPTCHA Generator** – Generates a random text string.  
2. **Image Renderer** – Converts the text into a CAPTCHA image.  
3. **User Input Module** – Accepts the user’s entered CAPTCHA value.  
4. **Verification Engine** – Compares user input with the generated text.  
5. **Human/Bot Decision** – Determines whether the user is likely human or a bot.


### Implementation
- `captcha.py`

-----

# 3. Water Jug Problem (Search Algorithms)

## Description
This project implements **Uninformed Search Algorithms** to solve the classic **Water Jug Problem**, a well-known problem used to demonstrate state-space search techniques in Artificial Intelligence.

The objective is to determine the sequence of actions needed to obtain a specific amount of water using two jugs of fixed capacities.

Jugs:
- Jug 1 = 4 liters  
- Jug 2 = 3 liters  

Goal:  
Measure exactly **2 liters** of water.

---

## Algorithms Implemented

### Breadth First Search (BFS)
- Explores the state space level by level  
- Ensures the shortest (optimal) solution is found  

### Depth First Search (DFS)
- Explores one path deeply before backtracking  
- Uses less memory but may not always produce the optimal solution

---

