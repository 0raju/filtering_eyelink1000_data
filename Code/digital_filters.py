# This work is licensed under a "Creative Commons Attribution-NonCommercial-
# ShareAlike 4.0 International License"
# (https://creativecommons.org/licenses/by-nc-sa/4.0/).
#
# Author: Mehedi Hasan Raju (m.raju@txstate.edu)
# Property of Texas State University.


from scipy.signal import butter, filtfilt, firwin

def zero_phase_digital_filter(data, type):

    """
    Applies a zero-phase digital filter of the specified type and cutoff frequency to the input data.

    Parameters:
        data (array-like): A 1-D array containing the signal to be filtered.
        cutoff (float): The cutoff frequency of the filter in Hz.
        type (str): The type of filter to use, either 'iir' for an infinite impulse response (IIR) filter or 'fir' for a finite impulse response (FIR) filter.

    Returns:
        filtered_data (array-like): A 1-D array containing the filtered signal with zero-phase distortion.

    """
    sampling_frequnecy = 1000
    nyquist_frequency = 0.5 * sampling_frequnecy      # Compute the Nyquist frequency of the signal
    order = 7                               # The order of the filter, only used for IIR filters
    btype='low'                             # The type of filter to design, either 'low' for lowpass or 'high' for highpass, only used for IIR filters
    ntaps = 80                              # The number of filter taps, only used for FIR filters

    if type == 'iir': # Design an IIR filter
        cutoff = 106 / nyquist_frequency        # The cutoff frequency of the filter depending on the value of `nyquist_frequency`
        b, a = butter(order, cutoff, btype=btype) # Compute the filter coefficients using a Butterworth filter design
        filtered_data = filtfilt(b, a, data) # Apply the filter to the data using zero-phase filtering

    elif type == 'fir': # Design an FIR filter
        cutoff = 109 / nyquist_frequency
        b = firwin(ntaps, cutoff, pass_zero=btype == 'low') # Compute the filter coefficients using a window-based FIR filter design
        filtered_data = filtfilt(b, 1, data) # Apply the filter to the data using zero-phase filtering
        
    return filtered_data