@echo off
title Kahoot Quiz Viewer
cd /d "%~dp0"
echo.
echo ================================
echo   KAHOOT QUIZ VIEWER LAUNCHER
echo ================================
echo.
echo Khoi dong ung dung Kahoot Quiz Viewer...
echo.

REM Chạy file exe
if exist "dist\KahootQuizViewer.exe" (
    echo Tim thay file exe. Dang khoi dong...
    start "" "dist\KahootQuizViewer.exe"
    echo.
    echo Ung dung da duoc khoi dong!
    echo Ban co the dong cua so nay.
    timeout /t 3 /nobreak >nul
) else (
    echo.
    echo KHONG TIM THAY FILE EXE!
    echo Vui long dam bao file "dist\KahootQuizViewer.exe" ton tai.
    echo.
    echo Ban co the chay bang cach:
    echo 1. Double-click truc tiep file "dist\KahootQuizViewer.exe"
    echo 2. Hoac chay "python main.py" neu ban co Python
    echo.
    pause
)