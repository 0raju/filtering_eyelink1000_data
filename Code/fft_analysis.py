# This work is licensed under a "Creative Commons Attribution-NonCommercial-
# ShareAlike 4.0 International License"
# (https://creativecommons.org/licenses/by-nc-sa/4.0/).
#
# Author: Mehedi Hasan Raju (m.raju@txstate.edu)
# Property of Texas State University.


import paths
import matplotlib.pyplot as plt 
import os, glob, numpy as np, pandas as pd
import matplotlib
matplotlib.use("Agg")

from fast_fourier_transform import fast_fourier_transform


def average_amplitude_spectrum(input_path):
    
    """
    Computes the average amplitude spectrum of a set of signals in a directory.
    
    Parameters:
    input_path (str): the path to the directory containing the signals (CSV files).
    
    Returns:
    average_amplitude_spectrum (ndarray): the average amplitude spectrum.

    """

    # Change working directory to input_path
    os.chdir(input_path)
    
    # Initialize a list to store the amplitude spectra
    amplitude_spectra = []
    
    # Iterate over each CSV file in the directory
    for file_name in sorted(glob.glob('*.csv')):
        # Load the CSV file into a pandas DataFrame
        data = pd.read_csv(file_name)
        signal_amplitude = data['x']
        
        # Compute the amplitude spectrum using fast Fourier transform
        signal_amplitude_spectrum = fast_fourier_transform(signal_amplitude)
        
        # Take the absolute value of the amplitude spectrum
        signal_amplitude_spectrum = np.abs(signal_amplitude_spectrum)
        
        # Add the amplitude spectrum to the list
        amplitude_spectra.append(signal_amplitude_spectrum)

    # Compute the average amplitude spectrum across all signals in the directory
    average_amplitude_spectrum = np.average(amplitude_spectra, axis=0)
    
    return average_amplitude_spectrum



def plot_fft_amplitude_spectrum(): 
    sampling_frequnecy = 1000
    dataLength = 256 
    N = int(dataLength / 2)
    frequency = np.fft.fftfreq(256, 1/sampling_frequnecy)[0:N]

    # All data directories
    unfiltered_dir = f'{paths.DATA_DIR}UnFiltered_Data'
    std_dir = f'{paths.DATA_DIR}STD_Filtered_Data'
    extra_dir = f'{paths.DATA_DIR}EXTRA_Filtered_Data'
    savgol_dir = f'{paths.DATA_DIR}SG_Filtered_Data'
    fir_dir = f'{paths.DATA_DIR}FIR_Filtered_Data'    
    iir_dir = f'{paths.DATA_DIR}IIR_Filtered_Data'

    # Create a list of all the directories to loop through. 
    directories_list = [unfiltered_dir, std_dir, extra_dir, savgol_dir, fir_dir, iir_dir]

    # Create an empty list to store the results of the average_amplitude_spectrum function. 
    results_list= []

    # Loop through each directory in the directories list and append the results of average_amplitude_spectrum to the results list. 
    for directory in directories_list: 
        result= average_amplitude_spectrum(directory)   # Store result of segments average in a variable.  
        results_list.append(result)                     # Append result to results list. 

    (
        amplitude_spectrum_unf, 
        amplitude_spectrum_std, 
        amplitude_spectrum_ext, 
        amplitude_spectrum_sg , 
        amplitude_spectrum_fir, 
        amplitude_spectrum_iir 
    ) = results_list
    
    fig = plt.figure(figsize=(16,9))
    
    plt.plot(frequency[1:N], amplitude_spectrum_unf[1:N], 'k-', linewidth=2, label='Unfiltered')
    plt.plot(frequency[1:N], amplitude_spectrum_std[1:N], 'r-', linewidth=2, label='STD')
    plt.plot(frequency[1:N], amplitude_spectrum_ext[1:N], 'b', linewidth=2, label='EXT')
    plt.plot(frequency[1:N], amplitude_spectrum_sg[1:N], 'm', linewidth=2, label='SG')
    plt.plot(frequency[1:N], amplitude_spectrum_iir[1:N], 'g--', linewidth=2, label='IIR')
    plt.plot(frequency[1:N], amplitude_spectrum_fir[1:N], 'tab:purple', linewidth=2, label='FIR')

    plt.xlabel('Frequency (Hz)', fontsize=22)
    plt.ylabel('Amplitude Spectrum',fontsize=22)
    plt.xticks(np.arange(0, 501, step=100), fontsize=22)
    plt.yticks(np.arange(0, 1.4, step=0.2), fontsize=22)
    plt.gca().xaxis.grid(True)
    plt.xlim(0, 500)
    plt.tight_layout()
    plt.legend(fontsize=18)

    fig.savefig(f'{paths.FIGURES_DIR}Figure_2.png', dpi=300, bbox_inches='tight')
