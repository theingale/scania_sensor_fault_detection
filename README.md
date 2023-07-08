# Scania Truck Failures Detection from Sensor Data

### Problem Statement
The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.

This is a Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class
indicates that the failure was caused by something else.

### Solution Proposed 
In this project, the system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.

The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.
## Tech Stack Used
1. Python 
2. FastAPI 
3. Machine learning algorithms
4. XGBoost
5. MongoDB
6. Uvicorn

## Project Workflow
![image](https://github.com/theingale/scania_truck_failures/assets/98829449/a352f627-c562-42b1-9d51-7dfc9e61764b)

## Project Deployment
### Training Pipeline Flow
![image](https://github.com/theingale/scania_truck_failures/assets/98829449/1765b7cb-96b1-44ee-9a43-4b2b49b853a0)

### Prediction Pipeline Flow
![image](https://github.com/theingale/scania_truck_failures/assets/98829449/ba3d51de-cd3f-4e28-9382-1dae4c86a3fe)

## How to Run Locally?
### Step 1: Clone the repository
```bash
git clone https://github.com/theingale/scania_truck_failures.git
```

### Step 2- Create a conda environment after opening the repository

```bash
conda create -n sensor python=3.8.0 -y
```

```bash
conda activate sensor
```

### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```

### Step 4 - Set the environment variable
Create a file env_variables.py at path <b>sensor\constant\env_variables.py</b> and enter following line of code
```bash
MONGODB_URL = "<YOUR MONGO DB URL>"
```
### Step 5 - Run the Uvicorn application server 
```bash
uvicorn main:app
```

### Step 6. Train api
```bash
http://localhost:8080/train

```

### Step 7. Prediction api
```bash
http://localhost:8080/predict
```
## Future Scope
The APIs can be containerized using Docker and can be deployed in any cloud service like Aws, Azure or GCP.


