#!/bin/sh
PID=$(ps aux | grep app.py | grep AGiXT |  grep -v grep | awk '{ print $2 }')
kill -9 $PID
PID=$(ps aux | grep Main.py | grep AGiXT |  grep -v grep | awk '{ print $2 }')
kill -9 $PID
cd /data/project/AGiXT/agixt
nohup /data/project/AGiXT/venv/bin/python app.py 2>&1 >> /data/project/AGiXT/log/backend.log &
nohup /data/project/AGiXT/venv/bin/python -m streamlit run Main.py 2>&1 >> /data/project/AGiXT/log/streamlit.log &
