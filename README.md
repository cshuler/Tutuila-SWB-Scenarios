[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3466114.svg)](https://doi.org/10.5281/zenodo.3466114)


# A Participatory and Model Based Approach to Assessing Groundwater Recharge Under Contemporary and Future Climate Scenarios: Tutuila, American Samoa

### Abstract
Already shifting climates have the potential to significantly change the global availability of water resources. On most volcanic islands throughout the Pacific Basin, groundwater is the primary water source of drinking water, and its quantification is essential for well-informed management of this limited resource. In this study we apply a geospatial water budget approach using the Soil Water-Balance-2 model (SWB2) to Tutuila, the main island in the Territory of American Samoa. This approach provides a high-resolution, whole-island, spatially and temporally distributed groundwater recharge estimate using currently available data. With this recharge estimate covering present day conditions we then assess the potential future change in recharge by substituting rainfall and temperature projections from dynamically downscaled climate global climate model predictions for 2080 to 2099 under the Representative Concentration Pathways (RCPs) 4.5 and 8.5 into the SWB2 model. The resulting projections of future recharge are important to understanding the future sustainability of life on Tutuila, as recharge is a major driver of water resources availability. In addition to assessing future climate scenarios, we are also working to apply a participatory approach with multiple stakeholder groups throughout Tutuila to develop possible future land-cover scenarios to substitute into the SWB2 model. 

Present day results indicate approximately 54% of Tutuila’s rainfall infiltrates as groundwater recharge, 8% is lost to canopy evaporation, another 15% is lost to evapotranspiration from soils, and 21% is discharged as stormflow-runoff. Future climate scenarios suggest an increase in total groundwater recharge of 17% to 27% might be expected by the end of the century depending on the emissions scenario used. A key attribute of the Tutuila SWB2 model was its development as an open-source project on the world’s leading software development platform, GitHub. By providing free-access to all model input files, pre-processing scripts, and model code, the scientific reproducibility and transparency of the project are enhanced and interested users are free to apply, modify, or test the model at their discretion. 

&nbsp;

&nbsp;



## Future Land-Use Scenarios
### Stakeholders! The comment period for these scenarios is still open. Please email cshuler@hawaii.edu if you have any suggested modifications to the scenarios outlined here. Thank you for your time!

&nbsp;

&nbsp;

### Scenario 1: Economic Boom and Unchecked Growth


<p align="center">
  <img width="900" height="450" src=/Scripts_Scen1/output/Figures/Scenario_1_GIF.gif >
</p>


#### Potential Causes
- - Internet cable brings new jobs
- - Tourist industry flourishes
- - Unchecked immigration from outside

#### Potential Effects
- Expansion of roadway on Assu Plain, and additional sealing of existing dirt roads,
construction of new roads in areas where building is feasible. An increase in
population could manifest as an increase in land needed for development. The
high-elevation mountain top area of Western Tutuila contains some of the last
low-slope undeveloped land on the island. ASCC researchers spoke about past
proposals to construct a roadway from Aasu to Fagamalo Villages, thereby
opening up much of Western Tutuila for development. GIS manifestation:
Addition of roadway from Aasu to Fagamalo Villages, all areas with a slope of
less than (15%) become covered with urbanized land use, road network built
between structures. (based on ASCC researchers interview and interview with
Dr. Hattori)
- Increase in runoff from additional impervious surfaces, and channelization of
streams. GIS manifestation: If runoff to rainfall ratio method for runoff
partionioning is used, increase runoff ratios proportionally to amount of increased
urbanization and impermeable surfaces. (Based on interview with Dr. Hattori)
- Increased population may result in more land being used for agroforest
plantations. Also AS-DOA is encouraging and may subsidize cacao plantations
for exports. Most flatter areas on Tutuila have been used for plantations at some
point in history. GIS manifestation: either use slope map or orthoimage/land use
areas of coconut palms to represent areas that could again be converted to
agroforest. (based on ASCC researchers interview and stated push for large farm
agricultural exports of the Department of Agriculture)
- Increased population and economic development may encourage row crop
farmers to expand to meet market demands. GIS manifestation: since these
farms are generally located on Tafuna-Leone Plain, it would be sensible to
predict their expansion in this region. Add additional row crop farms in areas
where there is currently local agriculture (based on ASCC researchers interview)
- Due to low availability of flat land increased population would have to be
compressed into existing spaces. DOC and Public Works already note trends in
densification of urban areas. GIS manifestation: densification of existing urban
areas, especially in Tafuna-Leone Plain where much freehold land is located.
(based on interview with DOC and Public Works)
- Increased hillside urbanization and filling of wetlands. DOC notes that some
houses are being built up hillsides, though not many because land is steep.
Increased population and land prices will make currently uneconomical building
sites more appealing in the future. GIS manifestation: Only areas of moderate
slope (determine threshold) and adjacent to existing development would be
considered. Develop an algorithm to convert lands that meet some development
criteria to urban land use. Also, wetland areas in locations viable for building may
be converted to urbanized land use (based on interview with DOC and on
interview with Dr. Hattori) 



&nbsp;


&nbsp;



### Scenario 2: Population Attrition


<p align="center">
  <img width="900" height="450" src=/Scripts_Scen2/output/Figures/Scenario_2_GIF.gif >
</p>

#### Potential Causes
- - Cannery shut down.
- - Increased flooding and degraded freshwater supply drive people to other places.
- - Lack of economic opportunities reduces population.
- - External or internal political causes reduces availability of jobs in government sector.

#### Potential Effects
- Lower populations will result in less agricultural plantations, as there will be less
people to feed and less people using the land. Additionally, trends towards
westernization/modernization also generally reduce agriculture in favor of
imported foods. GIS manifestation: randomly selected set of all existing
agriculture plantation area goes to vines and or to forest? (Idea based on
interview with ASCC researchers.)
- Urban boundaries may shrink with shrinking population, existing buildings may
be abandoned and revert to natural land-use. GIS manifestation: remove outer
layer of buildings from all villages replace with secondary scrub forest (based on
forest succession ideas of ASCC researchers)
- Urban density may also be reduced with shrinking population, existing buildings
may be abandoned and revert to natural land-use. GIS manifestation: reduce
level of development classification for residential areas (based on interview with
Dr. Hattori)
- Low-lying coastal villages abandoned as communities move inland and/or
upslope. GIS: Areas experiencing historic flooding changed from urban or
developed to secondary scrub forest. 

&nbsp;


&nbsp;


### Scenario 3: Increased population with increased zoning and management

<p align="center">
  <img width="900" height="450" src=/Scripts_Scen3/output/Figures/Scenario_3.gif >
</p>

#### Potential Causes
- - Scenario predicts increase in population similar to scenario 1
- - Includes numerous best management projects that could be implemented by regulators

**Including:**
- Implementation of stricter and more specific zoning regulations
- Implementation of and regulation of existing special management areas
- Increased infrastructure and stormwater management planning
Potential Effects
- Increased densification on Tafuna Plain, GIS manifestation: same as Scenario 1.
- Hillslope development GIS manifestation: based on the same algorithm as
scenario 1, but only in Pago Harbor area as a special management area, (note
no interview reference for this)
- Addition of infiltration basins for stormwater management GIS manifestation:
based on locations provided by (Dep of Public Works)
- Malaeimi Valley becomes special management area. GIS manifestation:
Removal of all road and residential in Malaeimi valley and preservation as
special conservation area (as suggested in MMI valley planning report)
- Consolidation of agroforestry, based on DOA programs to increase agricultural
exports. GIS manifestation: Merge smaller agroforest areas into fewer larger
ones, keeping same forest land areas as in scenario 2 (based on ASCC
researchers interview)
- Removal of some urban areas from the worst flood zones GIS manifestation:
Using FEMA riverine flood maps and NOAA coastal flood hazard maps of coastal
areas. Also move all removed urbanization into equivalently densified existing
areas. (based on interview with DOC and Public Works and on interview with Dr.
Hattori)


&nbsp;


&nbsp;






### Informational handout on develpment of land use scenarios


<p align="center">
  <img width="738" height="900" src=Docs/Handout_Final2.jpg >
</p>


### Model run instructions

To run this code, the user should copy the entire repository, keeping the directory structure intact. There are multiple versions of the model for different purposes. They are detailed below: 

The model code is contained in a number of Jupyter Notebooks. These include:
- A notebook that takes raw GIS data and formats the input for use in the SWB2 model. This is where the user can change the model cell size.   Note that only cell sizes of 50 m or more will create files that will fit on GitHub (<100mb)   (\Tutuila-SWB-Scenarios\New_Model_Runs\Run\Input_data_preparation.ipynb)
- The calibrated model, run over multiple scenarios.  The base case uses the 1_Tutuila_cal_controlFile.ctl, each other scenario has a separate output workspace and a seperate control file (\Tutuila-SWB-Scenarios\New_Model_Runs\Run\SWB2_Tutuila_model_Runfinals_.ipynb
- a notebook to compare the results from different scenarios (Tutuila-SWB-Scenarios\New_Model_Runs\Run\Scenario_comparison.ipynb)
- All the files for model calibration to optimize curve numbers, includes A loopable version of the model  (Tutuila-SWB-Scenarios\Model_calibration\Run\SWB2_Tutuila_model_Calibration.ipynb)
- All the files for sensitivity testing with the calibrated model, includes A loopable version of the model  (Tutuila-SWB-Scenarios\Sensitivity testing\Run\SWB2_sensitivity_testing.ipynb)
- An older version which uses interpolation of runoff to rainfall ratios (Tutuila-SWB-Scenarios\Original_model\Run\SWB2_Tutuila_model.ipynb)

Also the developemt of new land use scenarios was done through Jupyter notebooks. These files are included in the following folders: 
- Tutuila-SWB-Scenarios\Scripts_Scen1
- Tutuila-SWB-Scenarios\Scripts_Scen2
- Tutuila-SWB-Scenarios\Scripts_Scen3

The scripts to actuall run the model are generally contained in the "Run" folder. Each version of the model generally also has an input folder where model inputs are accessed, and also an output or workspace folder where results are saved. Most scripts produce summarized output tables in .csv format from each model run in the output folder .\post_prcessed_with_MFR

When executed, the model will either create or overwrite the appropriate directory structure and will create output folders with model results in gridded and tabular summarized format, as well as figures in .tif format.

The user needs to have all of the modules specified in the first code block installed within the active python environment. If any modules are not installed, the can be either downloaded from https://anaconda.org/conda-forge, or if using anaconda, the syntax to have anaconda perform the install can be typed into the conda command prompt.  Note that this model also uses ArcPy which is a proprietary python module requireing the user has an ESRI ArcGIS license (sorry, I dislike ESRI's buisness model too).

Note also that Raw downscaled GCM datasets used to develop the climate scenarios in this model are downloadable through the GitHub release v0.1-alpha of this project as the files are too large to host in the repository


If you wish to contact the author I can be reached at cshuler@hawaii.edu
