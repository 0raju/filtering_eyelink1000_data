# This work is licensed under a "Creative Commons Attribution-NonCommercial-
# ShareAlike 4.0 International License"
# (https://creativecommons.org/licenses/by-nc-sa/4.0/).
#
# Author: Mehedi Hasan Raju (m.raju@txstate.edu)
# Property of Texas State University.


import paths
import matplotlib.pyplot as plt 
import  numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")

from scipy.signal import savgol_filter
from digital_filters import zero_phase_digital_filter


def plot_exemplar_analysis():

    DataDir = f'{paths.DATA_DIR}Exemplar_Data/RAN_Unfiltered.csv'
    data = pd.read_csv(DataDir)
    start = 1800
    end = 2100

    X = data.loc[start:end, 'x'].to_numpy()
    t = data.loc[start:end, 't'].to_numpy()
            
    fig = plt.figure(figsize=(16,21))

    plt.subplot(3, 1, 1)
    plt.plot(X, 'k', label = 'Unfiltered')

    sg_filtered = savgol_filter(X, polyorder=2, window_length=11)
    plt.plot(sg_filtered +.5 , 'r', label = 'SG (offset 0.5)')

    iir_filtered = zero_phase_digital_filter(X, 'iir')
    plt.plot(iir_filtered +1, 'g', label = 'IIR (offset 1.0)')

    fir_filtered = zero_phase_digital_filter(X, 'fir')
    plt.plot(fir_filtered+1.5,  'b', label = 'FIR (offset 1.5)')

    plt.title('(A)', fontsize=32)
    plt.xlabel('Time (ms)', fontsize=22)
    plt.ylabel('Hor. Position (dva)', fontsize=22)
    plt.xticks(np.arange(0, 251, step=50), fontsize=18)
    plt.yticks(np.arange(11, 16.1, step=1), fontsize=18)
    plt.xlim(0, 250)
    plt.tight_layout()
    plt.legend(fontsize=18)
    plt.gca().xaxis.grid(True)


    plt.subplot(3, 1, 2)
    plt.title('(B)', fontsize=32)
    velocity = np.diff(X)/np.diff(t)*1000
    plt.plot(abs(velocity), 'k', label = 'Unfiltered')
    plt.xlabel('Time (ms)', fontsize=22)
    plt.ylabel('Velocity (d/s)', fontsize=22)
    plt.xticks(np.arange(0, 251, step=50), fontsize=18)
    plt.yticks(np.arange(-10, 401, step=100), fontsize=18)
    plt.xlim(0, 250)
    plt.tight_layout()
    plt.legend(fontsize=18)
    plt.gca().xaxis.grid(True)


    plt.subplot(3, 1, 3)
    plt.title('(C)', fontsize=32)
    velocity = np.diff(sg_filtered)/np.diff(t)*1000
    plt.plot(abs(velocity), 'r', label = 'SG')
    velocity = np.diff(iir_filtered)/np.diff(t)*1000
    plt.plot(abs(velocity)+50, 'g', label = 'IIR (offset 50)')
    velocity = np.diff(fir_filtered)/np.diff(t)*1000
    plt.plot(abs(velocity)+100, 'b', label = 'FIR (offset 100)')
    plt.xlabel('Time (ms)', fontsize=22)
    plt.ylabel('Velocity (d/s)', fontsize=22)
    plt.xticks(np.arange(0, 251, step=50), fontsize=18)
    plt.yticks(np.arange(0, 201, step=100), fontsize=18)
    plt.xlim(0, 250)
    plt.tight_layout()
    plt.legend(fontsize=18)
    plt.gca().xaxis.grid(True)
    
    fig.savefig(f'{paths.FIGURES_DIR}Figure_5.png', dpi=300, bbox_inches='tight')

# %%
