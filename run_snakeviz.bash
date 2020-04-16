#!/bin/bash
mkdir prof_out
python -m cProfile -o prof_out/temp.dat profiling.py
snakeviz prof_out/temp.dat