from flask import Flask, jsonify, send_file
from your_script_name import muse
from io import BytesIO
import matplotlib.pyplot as plt
from database import MuseData, Session 
from datetime import datetime, date
import matplotlib.dates as mdates

app = Flask(__name__)

global concentrationCheck, fatigueCheck, WhileTrue
concentrationCheck = 0
fatigueCheck = 0
WhileTrue = 0


@app.route('/start-muse-recording', methods=['GET'])
def start_recording():
    try:
        WhileTrue = 1 
        muse()
        # return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/stop-muse-recording', methods=['GET'])
def stop_recording():
    try:
        WhileTrue = 0
        return None
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# @app.route('/concentrationSignal', methods=['GET'])
# def concentrationSignal():
#     if concentrationCheck == 1:
#         concentrationCheck = 0
#         return "FOCUS ON THE ROAD"
    
# @app.route('/fatigueSignal', methods=['GET'])
# def fatigueSignal():
#     if fatigueCheck == 1:
#         fatigueCheck = 0
#         return "TAKE A BREAK"

def concentrationCall():
    concentrationCheck = 1
    return None

def fatigueCall():
    fatigueCheck = 1
    return None

@app.route('/plot', methods=['GET'])
def generate_plot():
    session = Session()
    data = session.query(MuseData).all()
    session.close()
    my_path = "/Users/adityagupta/projects/natHACKS2024-Project/musedb"

    # Extract data for the dot plot
    start_times = [entry.start_time for entry in data]  # Assuming entry.start_time is a datetime.time object
    concentration = [entry.concentration for entry in data]
    fatigue = [entry.fatigue for entry in data]

    # Convert start_times to datetime objects for plotting
    start_times_dt = [datetime.combine(date.today(), t) for t in start_times]

    # Create the dot plot
    plt.figure(figsize=(12, 6))

    # Plot concentration
    plt.scatter(start_times_dt, concentration, color='blue', alpha=0.7, label='Concentration')

    # Plot fatigue
    plt.scatter(start_times_dt, fatigue, color='red', alpha=0.7, label='Fatigue')

    # Format the x-axis to show times
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())

    # Add labels and title
    plt.xlabel('Start Time')
    plt.ylabel('Values')
    plt.title('Dot Plot of Concentration and Fatigue Over Time')
    plt.xticks(rotation=45, fontsize=8)  # Rotate x-axis labels
    plt.legend()
    plt.tight_layout()

    # Show the plot
    plt.show()
if __name__ == '__main__':
    app.run(debug=True, port=5001)
