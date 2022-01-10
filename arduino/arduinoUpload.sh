
#arduino code upload and compile script
#i dont wanna 50 commands every time so yeah this exists
#run sh arduinoUload.sh in this dir and it works

#arduino Front compile and upload
echo "front compile"
arduino-cli compile --fqbn arduino:avr:uno ardFront
echo "front upload"
arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno ardFront

#arduino Back compile and upload
echo "back compile"
arduino-cli compile --fqbn arduino:avr:uno ardBack
echo "back upload"
arduino-cli upload -p /dev/ttyACM1 --fqbn arduino:avr:uno ardBack

#arduino power compile and upload
#echo "power compile"
#arduino-cli compile --fqbn arduino:avr:uno ardPow
#echo "back upload"
#arduino-cli upload -p /dev/ttyACM1 --fqbn arduino:avr:uno ardPow
