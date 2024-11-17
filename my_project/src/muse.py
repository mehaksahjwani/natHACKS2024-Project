from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from brainflow.data_filter import DataFilter, FilterTypes
import numpy as np
import matplotlib.pyplot as plt
import time
from brainflow.data_filter import WindowOperations
from datetime import datetime
from circular import WhileTrue, concentrationCall, fatigueCall
# from database import MuseData, Session  # Import from database.py

def muse():
    print(2)
    params = BrainFlowInputParams()
    params.serial_port = 'COM6' #Change this depending on your device and OS
    board_id = 39 #Change this depending on your device
    beta=[]
    theta=[]
    countMuse =0


    #Prepares the board for reading data
    try:
        board_id = 39
        board = BoardShim(board_id, params)
        board.prepare_session()
        print("Successfully prepared physical board.")
    except Exception as e:
        print(e)
        #If the device cannot be found or is being used elsewhere, creates a synthetic board instead
        print("Device could not be found or is being used by another program, creating synthetic board.")
        board_id = BoardIds.SYNTHETIC_BOARD
        board = BoardShim(board_id, params)
        board.prepare_session()
    
    # start_time = datetime.now()
    # fatigue_values = []
    # concentration_values = []
    # timeval = []
    # dayval = []
    # timeval.append(start_time.strftime("%H:%M:%S"))
    # day = start_time.strftime("%A")


    print("Starting Stream")
    board.start_stream()
    eeg_channels = board.get_eeg_channels(board_id)
    sampling_rate = BoardShim.get_sampling_rate(board_id)
    time.sleep(2)
    print(3)
    while (WhileTrue):
        print(4)
        time.sleep(0.5)
        current_data = board.get_current_board_data(128)
        current_eeg_data = current_data[eeg_channels] 
        theta_total, beta_total = 0, 0

        for channel_data in current_eeg_data:
            if len(channel_data) > 0:

                # if (datetime.now() - start_time).seconds > 3600:
                #     concentration_values.append(concentrationaddition/1800)
                #     fatigue_values.append(fatigueaddition/1800)
                #     day = start_time.strftime("%A")
                #     dayval.append(day)
                #     concentrationaddition = 0
                #     fatigueaddition = 0
                #     start_time = datetime.now()
                #     timeval.append(start_time.strftime("%H:%M:%S"))

            # Apply filters to clean the signal
                DataFilter.perform_lowpass(channel_data, BoardShim.get_sampling_rate(board_id), 40.0, 5,
                                        FilterTypes.CHEBYSHEV_TYPE_1, 0.5)
                DataFilter.perform_highpass(channel_data, BoardShim.get_sampling_rate(board_id), 2.0, 4,
                                            FilterTypes.CHEBYSHEV_TYPE_1, 0.5)
            # Compute PSD
                psd = DataFilter.get_psd(channel_data, sampling_rate, WindowOperations.HANNING)
                #print(psd)
            # Extract band powers
                theta_power = DataFilter.get_band_power(psd, 4, 8)
                beta_power = DataFilter.get_band_power(psd, 13, 32)

                theta_total += theta_power
                beta_total += beta_power

        if countMuse < 50:
            beta.append(beta_total)
            theta.append(theta_total)
        if countMuse == 50:
            beta = np.array(beta)
            #mean_beta = np.mean(beta, axis=0)
            Q1_beta = np.percentile(beta, 25, method ='midpoint')
            Q3_beta = np.percentile(beta, 75, method ='midpoint')
            IQR_beta = Q3_beta - Q1_beta
            lower_bound_beta = Q1_beta - 1.5 * IQR_beta
            upper_bound_beta = Q3_beta + 1.5 * IQR_beta
            beta = [x for x in beta if x > lower_bound_beta and x < upper_bound_beta]
            beta_threshold = np.mean(beta, axis = 0)
            std_beta = np.std(beta)

            theta = np.array(theta)
            #mean_theta = np.mean(theta, axis = 0)
            Q1_theta = np.percentile(theta, 25, method ='midpoint')
            Q3_theta = np.percentile(theta, 75, method ='midpoint')
            IQR_theta = Q3_theta - Q1_theta
            lower_bound_theta = Q1_theta - 1.5 * IQR_theta
            upper_bound_theta = Q3_theta + 1.5 * IQR_theta
            theta = [x for x in theta if x > lower_bound_theta and x < upper_bound_theta]
            theta_threshold = np.mean(theta, axis = 0)
            std_theta = np.std(theta)
        
        #beta.append(beta_total)
        #theta.append(theta_total)
        #countMuse +=1
        if countMuse >= 50:
            if concentration > beta_threshold + std_beta :
                concentrationCall()
            elif fatigue > theta_threshold + std_theta:
                fatigueCall()
        # concentrationaddition += concentration 
        # fatigueaddition += fatigue
        countMuse +=1
        concentration = beta_total
        fatigue = theta_total
        print(concentration)
        print(fatigue)

    data = board.get_board_data()
    # print(data.shape)
    # print("Ending stream")
    board.stop_stream()
    board.release_session()

    # timeval.pop()
    # session = Session()
    # try:
    #     k = len(dayval)
    #     for i in range(k):  # Example: Generate 100 entries
    #         day = dayval[i]
    #         time = timeval[i]
    #         concentrate = concentration_values[i]
    #         tired = fatigue_values[i]
    #         entry = MuseData(
    #             day=day,
    #             start_time=datetime.strptime(time, "%H:%M:%S").time(),
    #             concentration=concentrate,
    #             fatigue= tired
    #         )
    #         session.add(entry)  # Add to the session
    #     session.commit()  # Commit all entries to the database
    #     print("Data added successfully!")

    # except Exception as e:
    #     session.rollback()  # Rollback in case of error
    #     print(f"Error: {e}")

    # finally:
    #     session.close()  # Close the session
