# This work is licensed under a "Creative Commons Attribution-NonCommercial-
# ShareAlike 4.0 International License"
# (https://creativecommons.org/licenses/by-nc-sa/4.0/).
#
# Author: Mehedi Hasan Raju (m.raju@txstate.edu)
# Property of Texas State University.


import paths
import os, glob
import matplotlib.pyplot as plt 
import numpy as np, pandas as pd
import matplotlib
matplotlib.use("Agg")

from scipy.signal import savgol_filter
from digital_filters import zero_phase_digital_filter
from fast_fourier_transform import fast_fourier_transform


def get_frequency_response(less_filter_segment, more_filter_segment):

    """
    Computes the frequency response of a filter by taking the ratio of the FFTs of two signal segments.

    Parameters:
        less_filter_segment (array): A 1-D array containing the unfiltered signal segment used as the input to the filter.
        more_filter_segment (array): A 1-D array containing the filtered signal segment produced by the filter.

    Returns:
        db (array): A 1-D array containing the frequency response of the filter in decibels.

    """
    # Compute FFT of the two signal segments
    fft_no_filter = fast_fourier_transform(less_filter_segment)[:128] 
    fft_more_filter = fast_fourier_transform(more_filter_segment)[:128]

    # Compute the frequency response of the filter by taking the ratio of the two FFTs
    hd = fft_more_filter / fft_no_filter

    # Convert to decibels
    dB = 20 * np.log10(np.abs(hd))
    
    return dB



def average_magnitude(input_path):
    std_dir = f'{paths.DATA_DIR}STD_Filtered_Data/'
    extra_dir = f'{paths.DATA_DIR}EXTRA_Filtered_Data/'

    """
    Processes a set of CSV files containing signals and returns the average frequency response of several filters.

    Parameters:
        input_path (str): 
            The path to the directory containing the CSV files to process.

    Returns:
        average_magnitiude_dict (dict): 
            A dictionary containing the average frequency response of several filters, 
            where the keys are the names of the filters and the values are arrays of decibel values.
    """

    os.chdir(input_path)
    db_list_std, db_list_ext, db_list_sg, db_list_iir, db_list_fir = [], [], [], [], []

    for file_name in sorted(glob.glob('*FilterLevel_0*.csv')):
        std_file_name = f"{file_name.split('_0_')[0]}_1_{file_name.split('_0_')[1]}"
        ext_file_name = f"{file_name.split('_0_')[0]}_2_{file_name.split('_0_')[1]}"


        # Read unfiltered data from CSV file
        unfiltered_data = pd.read_csv(file_name)
        unfiltered_x = unfiltered_data['x'].to_numpy()


        # Apply IIR filter and compute frequency response
        filtered_IIR = zero_phase_digital_filter(unfiltered_x, 'iir')
        db_iir = get_frequency_response(unfiltered_x, filtered_IIR)
        db_list_iir.append(db_iir)


        # Apply FIR filter and compute frequency response
        filtered_FIR = zero_phase_digital_filter(unfiltered_x, 'fir')
        db_fir = get_frequency_response(unfiltered_x, filtered_FIR)
        db_list_fir.append(db_fir)


        # Apply Savitzky-Golay filter and compute frequency response
        filtered_sg = savgol_filter(unfiltered_x, polyorder=2, window_length=11)
        db_sg = get_frequency_response(unfiltered_x, filtered_sg)
        db_list_sg.append(db_sg)


        # Read and process STD filtered data and compute frequency response
        collected_std = pd.read_csv(std_dir+std_file_name)
        filtered_std = collected_std['x'].to_numpy()
        db_std = get_frequency_response(unfiltered_x, filtered_std)
        db_list_std.append(db_std)


        # Read and process EXTRA filtered data and compute frequency response
        collected_ext = pd.read_csv(extra_dir+ext_file_name)
        filtered_ext = collected_ext['x'].to_numpy()
        db_ext = get_frequency_response(unfiltered_x, filtered_ext)
        db_list_ext.append(db_ext)


    # Compute average magnitude response for each filter and store in dictionary
    average_magnitiude_dict = {
        'STD': np.average(db_list_std, axis=0),
        'EXTRA': np.average(db_list_ext, axis=0),
        'SG': np.average(db_list_sg, axis=0),
        'IIR': np.average(db_list_iir, axis=0),
        'FIR': np.average(db_list_fir, axis=0),
    }

    return average_magnitiude_dict



def plot_frequency_response():
    input_path = f'{paths.DATA_DIR}UnFiltered_Data/'
    average_magnitiude_dict = average_magnitude(input_path)
    sampling_frequnecy = 1000
    freqs = np.fft.fftfreq(256, 1/sampling_frequnecy)[0:128]

    fig = plt.figure(figsize=(14,8))

    plt.plot(freqs[1:], average_magnitiude_dict['STD'][1:], color = 'k', label = 'STD') 
    plt.plot(freqs[1:], average_magnitiude_dict['EXTRA'][1:], color = 'r', label = 'EXTRA') 
    plt.plot(freqs[1:], average_magnitiude_dict['SG'][1:], color = 'g', label = 'SG') 
    plt.plot(freqs[1:], average_magnitiude_dict['IIR'][1:], color = 'b', marker='.', label = 'IIR') 
    plt.plot(freqs[1:], average_magnitiude_dict['FIR'][1:], color = 'm', label = 'FIR') 

    plt.axhline(0, color = 'b', linestyle = ':')
    plt.axhline(-3, color = 'r',linestyle = ':', label="-3dB (50% attenuation)")
    plt.axhline(-6, color = 'k',linestyle = ':', label="-6dB (75% attenuation)")
    plt.axhline(-30, color = 'g',linestyle = ':', label="-30dB (99.9% attenuation)")
    plt.axhline(-40, color = 'm',linestyle = ':', label="-40dB (100% attenuation)")

    plt.xlabel('Frequency (Hz)', fontsize=22)
    plt.ylabel('Magnitude (dB)',fontsize=22)
    plt.xticks(np.arange(0, 501, step=50), fontsize=18)
    plt.yticks([0, -3, -6, -30, -40], fontsize=18)
    plt.gca().xaxis.grid(True)
    plt.xlim(0, sampling_frequnecy/2)
    plt.tight_layout()
    plt.legend(fontsize=14)
        
    fig.savefig(f'{paths.FIGURES_DIR}Figure_1.png', dpi=300, bbox_inches='tight')

