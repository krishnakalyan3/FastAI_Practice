#!/usr/bin/env bash
sudo apt-get update

pip install gpustat
pip install kaggle-cli
sudo apt-get install python-lxml

kg config -g -u krishnakalyan3 -p kkalyan3#
kg download -c dog-breed-identification