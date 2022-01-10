cd arduino
sh arduinoUpload.sh
# pauses the program for 2s to make sure the arduino is ready
sleep 5

#logging
cd ~/Hyperloop/logs
CURRENTDATE=`date +"%Y-%m-%d-%T"`
mkdir ${CURRENTDATE}
echo "logging in "+${CURRENTDATE}

cd ~/Hyperloop/arduinoClient/requestBasedModel

python main.py ${CURRENTDATE}
