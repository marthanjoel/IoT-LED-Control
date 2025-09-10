# IoT LED Control (Tkinter Simulation)

A simple IoT project with a **Tkinter GUI** to simulate controlling an LED (ON/OFF).  
Can run in **Simulation Mode** (no Arduino) or connect to a real Arduino via serial.

---

## Objective
Provide an easy-to-use graphical interface for LED control to learn IoT concepts via Python and Tkinter, regardless of hardware availability.

---

## Tools & Technologies
- **Programming Language**: Python 3.x  
- **Framework**: Tkinter (GUI)  
- **Simulation Mode**: Runs without hardware  
- **Optional Dependency**: `pyserial` (for real Arduino support)

---

## Setup Instructions

### 1. Clone the Repository
 git clone https://github.com/marthanjoel/IoT-LED-Control.git  
cd IoT-LED-Control  

### 2. (Optional) Virtual Environment
python3 -m venv venv  
source venv/bin/activate  

### 3. Install Dependencies
pip install pyserial  

### 4. Run the Application
python3 app.py  

---

## Simulation Mode
- If no Arduino is connected, the app defaults to simulation.
- GUI displays:
  - **LED Indicator**: Green (OFF) and Yellow (ON).
  - **Buttons**: "Turn LED ON" and "Turn LED OFF."

---

## Future Improvements
- Add support for multiple LEDs or IoT sensors.
- Integrate MQTT for remote/IoT communication.
- Save and log LED state data to file or cloud.

---

## Screenshot

<img width="1158" height="740" alt="Screenshot from 2025-09-10 04-45-59" src="https://github.com/user-attachments/assets/706efd10-3624-435a-b3bf-c7803bcb32e9" />

---

## License
MIT
