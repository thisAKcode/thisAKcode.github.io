@echo off

REM Activate virtual environment
cd /d C:\blog_depend
call venv\Scripts\activate

REM Build Pelican site
cd /d C:\thisAKcode.github.io\Pelican
pelican content -o .. -s pelicanconf.py

REM Go to repo root
cd /d C:\thisAKcode.github.io

REM Git operations
git add .
git commit -m "some topic"
git push origin master

echo Deployment complete.
pause
