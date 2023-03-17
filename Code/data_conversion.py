# This work is licensed under a "Creative Commons Attribution-NonCommercial-
# ShareAlike 4.0 International License"
# (https://creativecommons.org/licenses/by-nc-sa/4.0/).
#
# Author: Mehedi Hasan Raju (m.raju@txstate.edu)
# Property of Texas State University.


import paths
from scipy.signal import savgol_filter
import os, pandas as pd
from digital_filters import zero_phase_digital_filter

def data_filtering(timestamp, raw_data, file_name):

    """

    Applies Savitzky-Golay, IIR, and FIR filters to the `raw_data` and saves the results in separate CSV files in their respective directories.

    Args:
        timestamp (list or numpy array): List or array of timestamps corresponding to the `raw_data`.
        raw_data (list or numpy array): List or array of raw data to be filtered.
        fileName (str): Name of the CSV file to save the filtered data.

    Returns:
        None
    
    """

    sg_data_df =pd.DataFrame(timestamp, columns=['t'])
    sg_filtered_data = savgol_filter(raw_data, window_length=11, polyorder=2)
    sg_data_df['x'] = sg_filtered_data
    sg_data_df = sg_data_df.round(4)

    sg_path = f'{paths.DATA_DIR}SG_Filtered_Data/'
    if not os.path.exists(sg_path):
        os.makedirs(sg_path)
    sg_data_df.to_csv(sg_path+ file_name, index = False)

     
    iir_data_df =pd.DataFrame(timestamp, columns=['t'])
    iir_filtered_data = zero_phase_digital_filter(raw_data, 'iir')
    iir_data_df['x'] = iir_filtered_data
    iir_data_df = iir_data_df.round(4)

    iir_path = f'{paths.DATA_DIR}IIR_Filtered_Data/'
    if not os.path.exists(iir_path):
        os.makedirs(iir_path)
    iir_data_df.to_csv(iir_path+ file_name, index = False)  

     
    fir_data_df =pd.DataFrame(timestamp, columns=['t'])
    fir_filtered_data = zero_phase_digital_filter(raw_data, 'fir')
    fir_data_df['x'] = fir_filtered_data
    fir_data_df = fir_data_df.round(4)

    fir_path = f'{paths.DATA_DIR}FIR_Filtered_Data/'
    if not os.path.exists(fir_path):
        os.makedirs(fir_path)
    fir_data_df.to_csv(fir_path+ file_name, index = False)
