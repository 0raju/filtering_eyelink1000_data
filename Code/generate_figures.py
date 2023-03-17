# This work is licensed under a "Creative Commons Attribution-NonCommercial-
# ShareAlike 4.0 International License"
# (https://creativecommons.org/licenses/by-nc-sa/4.0/).
#
# Author: Mehedi Hasan Raju (m.raju@txstate.edu)
# Property of Texas State University.


import paths
import argparse
import glob
import os

import pandas as pd
from tqdm import tqdm

from data_conversion import data_filtering
from frequency_response import plot_frequency_response
from fft_analysis import plot_fft_amplitude_spectrum
from autocorrelation import plot_autocorrelation
from boxplots import plot_boxplots
from filter_comparison_on_exemplar import plot_exemplar_analysis


def prepare_data(data_directory):

    """

    Prepares the data by filtering out NaN values and calling the data filtering function from data_conversion.py.

    Args:
        data_directory (str): The path to the directory containing the CSV files.

    Returns:
        None

    """

    os.chdir(data_directory)
    list_of_files = sorted(glob.glob("*.csv"))

    print("Preparing Data...")
    for file_name in tqdm(list_of_files):
        df = pd.read_csv(file_name)

        # Dropping NaN values from the dataframe
        df.dropna(inplace=True)

        # Converting the dataframe columns to numpy arrays
        time_stamp, hor_pos = df['t'].to_numpy(), df['x'].to_numpy()

        # Calling the data filtering function
        data_filtering(time_stamp, hor_pos, file_name)


def create_figures(fig):

    """
    Creates figures based on user input.

    Args:
        fig(int): The choice of specific figure number to create. By deafult, it will generate all figures. 

    Returns:
        None

    """


    if fig == 0:
        print("Creating Figure-1 :: Frequency Response")
        plot_frequency_response()

        print("Creating Figure-2 :: FFT Analysis Amplitude Spectrum")
        plot_fft_amplitude_spectrum()

        print("Creating Figure-3 :: Temporal Autocorrelation")
        plot_autocorrelation()

        print("Creating Figure-4 :: Fisher-Z Box Plots")
        plot_boxplots()

        print("Creating Figure-5 :: Exemplar Analysis")
        plot_exemplar_analysis()
    else:
        if fig == 1:
            print("Creating Figure-1 :: Frequency Response")
            plot_frequency_response()

        elif fig == 2:
            print("Creating Figure-2 :: FFT Analysis Amplitude Spectrum")
            plot_fft_amplitude_spectrum()

        elif fig == 3:
            print("Creating Figure-3 :: Temporal Autocorrelation")
            plot_autocorrelation()

        elif fig == 4:
            print("Creating Figure-4 :: Fisher-Z Box Plots")
            plot_boxplots()

        elif fig == 5:
            print("Creating Figure-5 :: Exemplar Analysis")
            plot_exemplar_analysis()


if __name__ == "__main__":
    
    # Dataset Preparation
    data_directory = f"{paths.DATA_DIR}UnFiltered_Data/"
    prepare_data(data_directory)

    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--fig', type=int, required=False, help='Figure (1-5) (default: all)', choices=[0, 1, 2, 3, 4, 5], default=0)
    args = parser.parse_args()

    # Create the specified figures
    create_figures(args.fig)
