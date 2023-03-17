# This work is licensed under a "Creative Commons Attribution-NonCommercial-
# ShareAlike 4.0 International License"
# (https://creativecommons.org/licenses/by-nc-sa/4.0/).
#
# Author: Mehedi Hasan Raju (m.raju@txstate.edu)
# Property of Texas State University.


import numpy as np, pandas as pd

def fast_fourier_transform(segment):

    """
    Computes the fast Fourier transform (FFT) of a given signal segment after detrending the signal and applying hanning window.

    Parameters:
        segment (array-like): A 1-D array containing the signal segment to be transformed.

    Returns:
        my_ffft (array-like): A 1-D array containing the FFT of the given signal segment.

    """

    signal_time = [i for i in range(0,len(segment))]                            # Create a time index for the signal
    p2 = np.polyfit(signal_time, segment, deg = 2)                              # Fit a second-degree polynomial to detrend the signal
    detrended_signal = segment - np.polyval(p2, signal_time)                    # Detrend the signal using the fitted polynomial
    signal_hanning_window = np.hanning(len(detrended_signal)) * detrended_signal # Apply a Hanning window to the detrended signal
    my_fft = np.fft.fft(signal_hanning_window)                                  # Compute the FFT of the windowed signal
    return my_fft