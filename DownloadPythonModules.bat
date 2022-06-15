@echo off

:start
cls

set python_ver=36

python ./get-pip.py

cd \
cd \python%python_ver%\Scripts\
pip install cv2
pip install mediapipe
pip install time

pause
exit