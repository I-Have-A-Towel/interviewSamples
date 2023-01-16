REM Q1: Can you summarize briefly what this script is doing?

FOR /F "tokens=* USEBACKQ" %%F IN (`gcloud config get-value project`) DO set project_name=%%F

IF /I "%project_name%" EQU "altairianproject" set branch="altairianproject"
ELSE set branch="staging"

IF EXIST "C:\gv-service" RMDIR /Q/S "C:\gv-service"

git clone --branch %branch% --recurse-submodules "https://github.com/I-Have-A-Towel/gv-service" "C:\gv-service"
cd C:\gv-service

REM Q2: Why are we using `call` before npm install but not the other lines?
call npm install

REM Q3: What do these 2 commands imply?
net start GVService
sc query GVService
