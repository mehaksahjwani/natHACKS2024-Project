<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DriveSafe - AI-Powered Driver Safety App</title>
</head>
<body>
    <h1>DriveSafe - AI-Powered Driver Safety App</h1>
    
    <h2>Introduction</h2>
    <p>
        We are excited to present <strong>DriveSafe</strong>, an AI-powered application designed to enhance road safety by combating driver fatigue, an issue that is particularly significant in Alberta with its long highways and harsh winters. DriveSafe continuously monitors driver alertness using cutting-edge neurotechnology and AI, helping drivers stay focused and prevent accidents caused by fatigue.
    </p>
    
    <h2>Features</h2>
    <ul>
        <li><strong>AI-Powered Fatigue Detection:</strong> DriveSafe utilizes EEG data from the Muse S device and real-time facial analysis through OpenCV to detect fatigue. We assess concentration and alertness by analyzing brain activity and facial landmarks such as eye closure and yawning.</li>
        <li><strong>Real-Time Alerts:</strong> When decreased alertness is detected, DriveSafe provides immediate voice alerts to help drivers refocus and stay safe.</li>
        <li><strong>Weather Integration:</strong> DriveSafe integrates with a weather API to monitor external conditions that may impact driver alertness, adding an additional layer of safety.</li>
        <li><strong>Historical Data Analysis:</strong> DriveSafe stores driving data in an SQLite database and offers weekly trend analysis, which is visualized using Matplotlib. This helps drivers understand their driving habits and improve over time.</li>
        <li><strong>Future Integration with Electric Vehicles:</strong> We plan to integrate DriveSafe with electric vehicles like Tesla, enabling the vehicle to switch to self-driving mode when critical fatigue levels are detected, guiding the car to a safe stop.</li>
    </ul>
    
    <h2>Built With</h2>
    <ul>
        <li>brainflow – for collecting EEG data from the Muse S device</li>
        <li>css – for styling the front end</li>
        <li>dlib – for facial landmark detection</li>
        <li>flask – for backend development</li>
        <li>flask-cors – for enabling cross-origin resource sharing</li>
        <li>html5 – for front-end structure</li>
        <li>math – for signal processing</li>
        <li>muse – for EEG signal processing from the Muse S device</li>
        <li>numpy – for numerical calculations</li>
        <li>opencv – for facial recognition and analysis</li>
        <li>python – for backend development</li>
        <li>react – for front-end development</li>
        <li>scipy – for scientific computing</li>
    </ul>
    
    <h2>Demo</h2>
    <p>
        You can check out the demo of DriveSafe here: <a href="https://lnkd.in/gBqPs9mW" target="_blank">Demo Link</a>
    </p>
</body>
</html>
