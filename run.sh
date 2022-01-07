cd arduino
sh arduinoUpload.sh
cd ../arduinoClient/requestBasedModel
# pauses the program for 2s to make sure the arduino is ready
sleep 5
python main.py
