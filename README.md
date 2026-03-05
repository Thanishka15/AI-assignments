# AI Assignments

This repository contains implementations of several Artificial Intelligence concepts including intelligent agents, search algorithms, and human verification systems.

---

# 1. AQI Intelligent Agent

## Description
This project implements an ***Air Quality Index (AQI) intelligent agent*** that determines the air quality level of different regions. The agent retrieves live air pollution data using the OpenWeather Air Pollution API, calculates AQI sub-indices for different pollutants, and determines the overall AQI category.

The agent processes real-time environmental data and classifies air quality into standard AQI categories such as Good, Moderate, Poor, etc.

## Data Source
The system uses the OpenWeather Air Pollution API to fetch live pollutant concentration data for specified geographic coordinates (latitude and longitude). The API provides concentrations of major pollutants such as PM2.5, PM10, NO₂, O₃, CO, SO₂, and NH₃.

These pollutant values are then used to compute AQI using standard AQI breakpoint tables.

## Components
- `code.py` – Main agent implementation
- `config.py` – Configuration settings
- `aqi_categories.csv` – AQI category definitions
- `aqi_checkpoints.csv` – AQI dataset for testing

## Agent Architecture
The AQI system follows a **Simple Reflex Agent architecture**:
1. Sensor reads AQI values.
2. Agent checks category rules.
3. Actuator outputs the air quality category.

-------
# 2. Turing test and Captcha

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

------


