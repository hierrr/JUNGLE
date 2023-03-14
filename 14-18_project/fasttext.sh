#!/bin/bash

pip install --upgrade pip setuptools wheel
git clone https://github.com/facebookresearch/fastText.git
cd fastText
pip install .
