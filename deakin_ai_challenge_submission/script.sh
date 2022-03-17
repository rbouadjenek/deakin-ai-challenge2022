#!/bin/bash

cd program/
# CONDA
conda create -n mypython3 python=3.8
source activate mypython3 2> /dev/null > /dev/null
conda install numpy  2> /dev/null > /dev/null
conda install tensorflow 2> /dev/null > /dev/null
conda install keras 2> /dev/null > /dev/null
conda install pillow 2> /dev/null > /dev/null
conda install h5py 2> /dev/null > /dev/null
echo $1
ls -lhR $1
echo $2
ls -lhR $2

python3 deakin_ai_challenge_submission.py $1 $2 
