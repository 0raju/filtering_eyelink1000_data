**Overview**
---------------------------------------------------------------------------

This is the source code for our research titled - 
Filtering Eye-Tracking Data From an EyeLink 1000: Comparing Heuristic, Savitzky-Golay, IIR and FIR Digital Filters.
Paper is published in JEMR -https://bop.unibe.ch/JEMR/article/view/9888
Everything needed to recreate the analysis and regenerate the figures is included.

**Cite**
---------------------------------------------------------------------------
Raju, M. H., Friedman, L., Bouman, T., & Komogortsev, O. (2023). Filtering eye-tracking data from an EyeLink 1000: Comparing heuristic, savitzky-golay, IIR and FIR digital filters. Journal of Eye Movement Research, 14(3). https://doi.org/10.16910/jemr.14.3.6


**License**
----------------------------------------------------------------------------
This work is licensed under a "Creative Commons Attribution-NonCommercial- 
ShareAlike 4.0 International License" (https://creativecommons.org/licenses/by-nc-sa/4.0/).

Property of Texas State University.



**Contact**
----------------------------------------------------------------------------
If you have any questions or difficulties regarding the use of this code, 
please feel free to email the author, Mehedi Hasan Raju (m.raju@txstate.edu)



**Folder/File Description**
----------------------------------------------------------------------------
The project directory has the following structure:

`Code` : Contains the Python code required to generate the figures. 

`DataForFigures` : All the data required to re-generate the figures. We have shared all the collected data required to recreate all the experiments here. It contains seven sub-folders. Four sub-folder is already given,  three more folders will be created here with filtered data when generate_figures.py will be run.

	1. `UnFiltered_Data`: All 216 segments of Unfiltered data (collected with EyeLink 1000 with filter level OFF)
	2. `STD_Filtered_Data`: All 216 segments of STD_filtered data (collected with EyeLink 1000 with filter level STD)
	3. `EXTRA_Filtered_Data`: All 216 segments of EXTRA_filtered data (collected with EyeLink 1000 with filter level EXTRA)
	4. `Exemplar_Data` - Contain a noisy exemplar of Random saccade data for generating Figure 5.
	5. `SG_Filtered_Data` - All 216 segments of Savitzky Golay filtered version of the UnFiltered Data.
	6. `IIR_Filtered_Data` - All 216 segments of IIR Butterworth filtered version of the UnFiltered Data.
	7. `FIR_Filtered_Data` - All 216 segments of FIR filtered version of the UnFiltered Data.
	

`ManuscriptFigures` -- This folder is left empty intentionally, and the generated figures will be saved here after running the code.

`filtering.yml` -- Compatible environemnt to run the code.



**Steps to run the code and Replicate the Figures**
----------------------------------------------------------------------------

1. Create a virtual environment from given `filtering.yml` file (for example: `filtering`)
``` bash
	$ conda env create -f filtering.yml
	$ conda activate filtering
```
2. Change the `MAIN_DIR` in paths.py to your SupplementaryMaterials folder location. You will find paths.py in the ``Code`` subfolder.
3. To generate all five figures, run the following command.
``` bash
	$ cd Code
	$ python generate_figures.py
```
4. To recreate a particular figure, add the --fig parser. For example, to generate Figure 1 only, run the following command.
``` bash
	$ python generate_figures.py --fig=1
```


