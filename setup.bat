rem Installing Dependencies...
pip install -r requirements.txt
rem Starting API...
start python scripts/api.py
rem Starting Ngrok Redirect
ngrok
ngrok authtoken 20ymmOF25HaU34Ivcfyu3kTDWi9_67ecS3yLFzmwf21pTGo2C
ngrok http 7777
pause