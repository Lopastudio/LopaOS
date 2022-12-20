@echo off
echo register launcher for LOPAOS
echo [C] Lopastudio 2021
echo [C] LopaOS 2021

cd programs
py reg.py
cd pip
pip install send2trash
pause