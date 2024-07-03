# This work is licensed under a "Creative Commons Attribution-NonCommercial-
# ShareAlike 4.0 International License"
# (https://creativecommons.org/licenses/by-nc-sa/4.0/).
#
# Author: Mehedi Hasan Raju (m.raju@txstate.edu)
# Property of Texas State University.


import paths
import glob, os, numpy as np, pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import matplotlib
matplotlib.use("Agg")

def autocorelation_function(directories_list):

    """
    Calculates the autocorrelation function of time series data in each directory in the list of directories provided.

    Args:
    directories_list (list): A list of directories containing the time series data as .csv files.

    Returns:
    result_list (list): A list of lists containing the autocorrelation function of each time series in each directory.
    
    """

    
    nlags = 5    # Set the number of lags to be calculated

    result_list = []

    for directory in directories_list:
        acorr_list = []
        os.chdir(directory)
        for fileName in sorted(glob.glob("*.csv")):
            df = pd.read_csv(fileName)
            data = df["x"].to_numpy()
            
            acorr = sm.tsa.acf(data, nlags=nlags)      # Calculate the autocorrelation function of the data up to the specified number of lags         
            acorr[0:1] = np.nan                        # Set the first lag to be NaN to avoid division by zero errors

            acorr_list.append(acorr)

        result_list.append(acorr_list)
    
    return result_list


def plot_autocorrelation():
    unfiltered_dir = f'{paths.DATA_DIR}UnFiltered_Data'
    std_dir = f'{paths.DATA_DIR}STD_Filtered_Data'
    extra_dir = f'{paths.DATA_DIR}EXTRA_Filtered_Data'
    savgol_dir = f'{paths.DATA_DIR}SG_Filtered_Data'
    fir_dir = f'{paths.DATA_DIR}FIR_Filtered_Data'    
    iir_dir = f'{paths.DATA_DIR}IIR_Filtered_Data'

    directories_list = [
        unfiltered_dir,
        std_dir,
        extra_dir,
        savgol_dir,
        fir_dir,
        iir_dir
    ]
    result_list = autocorelation_function(directories_list)

    (
        unfiltered_acorr,
        std_acorr,
        extra_acorr,
        savgol_acorr,
        fir_acorr,
        iir_acorr
    ) = result_list

    fig, ax = plt.subplots(figsize=(10, 8))

    ax.set_xlim(0.5, 5.5)
    ax.set_ylim(0.55, 1)
    ax.set_xlabel("Lags", fontsize=22)
    ax.set_ylabel("Autocorrelation", fontsize=22)
    ax.set_xticks([ 1, 2, 3, 4, 5])
    ax.set_yticks([ 0.6, 0.7, 0.8, 0.9, 1])
    ax.tick_params(axis="both", which="major", labelsize=22, width=2)


    ax.plot(np.median(unfiltered_acorr, axis=0), "r-", label="Unfiltered", linewidth=2)
    ax.plot(np.median(std_acorr, axis=0), "g-", label="STD", linewidth=2)
    ax.plot(np.median(extra_acorr, axis=0), "b-", label="EXTRA", linewidth=3)
    ax.plot(np.median(savgol_acorr, axis=0), "c-", label="SG", linewidth=2)
    ax.plot(np.median(iir_acorr, axis=0), "k", label="IIR", linewidth=2, markersize=10)
    ax.plot(np.median(fir_acorr, axis=0), "m-", label="FIR", linewidth=2)

    ax.plot(np.median(unfiltered_acorr, axis=0), "r.", linewidth=9, markersize=14)
    ax.plot(np.median(std_acorr, axis=0), "g.", linewidth=9, markersize=14)
    ax.plot(np.median(extra_acorr, axis=0), "b.", linewidth=9, markersize=14)
    ax.plot(np.median(savgol_acorr, axis=0), "c.", linewidth=9, markersize=14)
    ax.plot(np.median(iir_acorr, axis=0), "k.", linewidth=9, markersize=14)
    ax.plot(np.median(fir_acorr, axis=0), "m.", linewidth=9, markersize=14)

    ax.legend(prop={"size": 18})
    
    fig.savefig(f'{paths.FIGURES_DIR}Figure_3.png', dpi=300, bbox_inches='tight')
