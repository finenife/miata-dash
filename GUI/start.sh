#!/bin/bash

python GaugeClusterGUI.py &
sleep 0.5
python CAN_handler.py
