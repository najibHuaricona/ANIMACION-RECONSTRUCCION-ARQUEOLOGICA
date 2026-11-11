@echo off
cd /d "%~dp0"
py servidor.py
if errorlevel 1 python servidor.py
pause
