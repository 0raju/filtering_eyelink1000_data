# This work is licensed under a "Creative Commons Attribution-NonCommercial-
# ShareAlike 4.0 International License"
# (https://creativecommons.org/licenses/by-nc-sa/4.0/).
#
# Author: Mehedi Hasan Raju (m.raju@txstate.edu)
# Property of Texas State University.


import paths
import  numpy as np, pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

from autocorrelation import autocorelation_function

def plot_boxplots():
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


    # Convert the autocorrelation data to Fisher z-scores
    
    unfiltered_acf_transform = np.arctanh(unfiltered_acorr)
    std_acf_transform = np.arctanh(std_acorr)
    extra_acf_transform = np.arctanh(extra_acorr)
    sg_acf_transform = np.arctanh(savgol_acorr)
    iir_acf_transform = np.arctanh(iir_acorr)
    fir_acf_transform = np.arctanh(fir_acorr)


    columns = ['Unfilt', 'STD', 'EXT', 'SG', 'IIR', 'FIR' ]

    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(21, 7))


    # Boxplot of Fisher z-scores for ACF1

    acf_box1 = list(zip(unfiltered_acf_transform[:,1], std_acf_transform[:,1], extra_acf_transform[:,1], sg_acf_transform[:,1], iir_acf_transform[:,1], fir_acf_transform[:,1]))
    acf_box1 = [list(elem) for elem in acf_box1]
    acf_1 = pd.DataFrame(acf_box1, columns=columns)
    acf_1.boxplot(column=['Unfilt', 'STD', 'EXT', 'SG', 'IIR', 'FIR'], 
                         grid=False, fontsize=16, ax=axes[0] )
    
    axes[0].set_ylabel('Fisher Z (ACF1)', fontsize=16)
    axes[0].set_title('Autocorrelation Lag 1', fontsize=18)
    axes[0].set_ylim([-0.5, 3.5])
    axes[0].text(0.8, 3.1, '(A)', fontsize=24, fontweight='bold')



    # Boxplot of Fisher z-scores for ACF2

    acf_box2 = list(zip(unfiltered_acf_transform[:,2], std_acf_transform[:,2], extra_acf_transform[:,2], sg_acf_transform[:,2], iir_acf_transform[:,2], fir_acf_transform[:,2]))
    acf_box2 = [list(elem) for elem in acf_box2]
    acf_2 = pd.DataFrame(acf_box2, columns=columns)
    acf_2.boxplot(column=['Unfilt', 'STD', 'EXT', 'SG', 'IIR', 'FIR'], 
                         grid=False, fontsize=16, ax=axes[1] )
    
    axes[1].set_ylabel('Fisher Z (ACF2)', fontsize=16)
    axes[1].set_title('Autocorrelation Lag 2', fontsize=18)
    axes[1].set_ylim([-0.5, 3.5])
    axes[1].text(0.8, 3.1, '(B)', fontsize=24, fontweight='bold')



    # Boxplot of Fisher z-scores for ACF3

    acf_box3 = list(zip(unfiltered_acf_transform[:,3], std_acf_transform[:,3], extra_acf_transform[:,3], sg_acf_transform[:,3], iir_acf_transform[:,3], fir_acf_transform[:,3]))
    acf_box3 = [list(elem) for elem in acf_box3]
    acf_3 = pd.DataFrame(acf_box3, columns=columns)
    acf_3.boxplot(column=['Unfilt', 'STD', 'EXT', 'SG', 'IIR', 'FIR'], 
                         grid=False, fontsize=16, ax=axes[2] )
    
    axes[2].set_ylabel('Fisher Z (ACF3)', fontsize=16)
    axes[2].set_title('Autocorrelation Lag 3', fontsize=18)
    axes[2].set_ylim([-0.5, 3.5])
    axes[2].text(0.8, 3.1, '(C)', fontsize=24, fontweight='bold')


    fig.savefig(f'{paths.FIGURES_DIR}Figure_4.png', dpi=300, bbox_inches='tight')



