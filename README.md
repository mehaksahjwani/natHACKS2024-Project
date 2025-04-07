# **DriveSafe – Your AI Co-Pilot for Safer Roads**

## **Overview**
Introducing **DriveSafe**, an advanced AI-powered safety solution designed to combat driver fatigue—an issue especially critical in regions like Alberta with its vast highways and challenging winter conditions. DriveSafe actively monitors driver alertness using cutting-edge neurotechnology and artificial intelligence, helping prevent accidents by keeping drivers focused and aware.

## **Key Features**
- **Smart Fatigue Detection:**  
  DriveSafe combines EEG signals from the Muse S headband with real-time facial analysis via OpenCV. By monitoring brainwave activity and facial cues like eye closure and yawning, it accurately gauges driver alertness and concentration.

- **Instant Voice Alerts:**  
  If signs of fatigue are detected, DriveSafe immediately issues voice alerts to help the driver regain focus, improving real-time responsiveness.

- **Integrated Weather Awareness:**  
  Using data from a weather API, DriveSafe accounts for external conditions that may affect driving performance, offering more contextual and adaptive safety monitoring.

- **Insightful Driving Analytics:**  
  All driving sessions are logged in an SQLite database, with weekly trends visualized through Matplotlib. This allows drivers to track their focus patterns and develop safer driving habits over time.

- **Future-Ready with EV Integration:**  
  We’re working towards integrating DriveSafe with electric vehicles such as Teslas. In the future, if critical fatigue levels are reached, the app could prompt the vehicle to engage autonomous driving and guide itself safely off the road.

## **Technology Stack**
- `brainflow` – EEG data acquisition from Muse S  
- `muse` – EEG signal interpretation  
- `opencv` – Real-time facial recognition  
- `dlib` – Facial landmark tracking  
- `scipy` & `math` – Signal and scientific processing  
- `numpy` – Numerical analysis  
- `flask` & `flask-cors` – Backend APIs and cross-origin communication  
- `python` – Core backend logic  
- `react` – Interactive frontend UI  
- `html5` & `css` – UI layout and styling  
- `matplotlib` – Visual analytics and trend graphs

## **Live Demo**
Check out a live demonstration of DriveSafe in action:  
👉 [**View Demo**](https://lnkd.in/gBqPs9mW)

