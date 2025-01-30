<h1>DriveSafe - AI-Powered Driver Safety App</h1>
Introduction
We are excited to present DriveSafe, an AI-powered application designed to enhance road safety by combating driver fatigue, an issue that is particularly significant in Alberta with its long highways and harsh winters. DriveSafe continuously monitors driver alertness using cutting-edge neurotechnology and AI, helping drivers stay focused and prevent accidents caused by fatigue.

Features
AI-Powered Fatigue Detection: DriveSafe utilizes EEG data from the Muse S device and real-time facial analysis through OpenCV to detect fatigue. We assess concentration and alertness by analyzing brain activity and facial landmarks such as eye closure and yawning.
Real-Time Alerts: When decreased alertness is detected, DriveSafe provides immediate voice alerts to help drivers refocus and stay safe.
Weather Integration: DriveSafe integrates with a weather API to monitor external conditions that may impact driver alertness, adding an additional layer of safety.
Historical Data Analysis: DriveSafe stores driving data in an SQLite database and offers weekly trend analysis, which is visualized using Matplotlib. This helps drivers understand their driving habits and improve over time.
Future Integration with Electric Vehicles: We plan to integrate DriveSafe with electric vehicles like Tesla, enabling the vehicle to switch to self-driving mode when critical fatigue levels are detected, guiding the car to a safe stop.
Built With
brainflow – for collecting EEG data from the Muse S device
css – for styling the front end
dlib – for facial landmark detection
flask – for backend development
flask-cors – for enabling cross-origin resource sharing
html5 – for front-end structure
math – for signal processing
muse – for EEG signal processing from the Muse S device
numpy – for numerical calculations
opencv – for facial recognition and analysis
python – for backend development
react – for front-end development
scipy – for scientific computing
Demo
You can check out the demo of DriveSafe here: Demo Link
