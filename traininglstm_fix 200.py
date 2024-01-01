# -*- coding: utf-8 -*-
"""TrainingLSTM_fix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pmq67lopbDnBasnWDSWGcfgzofP3SEZB
"""

# Commented out IPython magic to ensure Python compatibility.
# %env PYTHONPATH = # /env/python
!wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Linux-x86_64.sh
!chmod +x Miniconda3-py38_4.12.0-Linux-x86_64.sh
!./Miniconda3-py38_4.12.0-Linux-x86_64.sh -b -f -p /usr/local
!conda update conda
import sys
sys.path.append('/usr/local/lib/python3.8/site-packages')
!conda create -n myenv python=3.6

# Commented out IPython magic to ensure Python compatibility.
# %%shell
# eval "$(conda shell.bash hook)"
# conda activate myenv
# git clone https://github.com/ml5js/training-charRNN
# pip install -r training-charRNN/requirements.txt
# wget https://raw.githubusercontent.com/emmevolpe/CO3104/main/alice.txt
# python3 training-charRNN/train.py --data_path alice.txt \
# --rnn_size 128 \
# --num_layers 2 \
# --seq_length 50 \
# --batch_size 50 \
# --num_epochs 200 \
# --save_checkpoints ./checkpoints \
# --save_model ./models
# zip -r model.zip models/alice