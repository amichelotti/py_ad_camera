# py_ad_camera
Python area detector viewer

camera example docs:
https://confluence.infn.it/display/LDCG/BASLER+CAMERA

## requirements
https://zzun.app/repo/epics-base-pvaPy-python-miscellaneous

## pvapy examples
https://github.com/epics-base/pvaPy/tree/master/examples


## environment
Remeber to set from bash shell:
export EPICS_PVA_ADDR_LIST=193.206.86.152
export EPICS_PVA_AUTO_ADDR_LIST=NO

## install & configure a conda environment
conda create -n "myenvironment" opencv
conda activate myenvironment
conda install -c epics pvapy
conda env config vars set EPICS_PVA_ADDR_LIST=193.206.86.152
conda env config vars set EPICS_PVA_AUTO_ADDR_LIST=NO



