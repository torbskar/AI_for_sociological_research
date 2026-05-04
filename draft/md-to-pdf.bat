@echo off
if "%~1"=="" (
    echo Usage: Drag and drop a .md file onto this script.
    pause
    exit /b 1
)

pandoc "%~1" -o "%~dpn1.pdf" --pdf-engine=lualatex -V geometry:margin=2.5cm -V fontsize=12pt -V papersize=a4 -V documentclass=article -V colorlinks=true -V monofont="Consolas"

if %errorlevel%==0 (
    echo Done: %~dpn1.pdf
) else (
    echo Conversion failed.
)
pause
