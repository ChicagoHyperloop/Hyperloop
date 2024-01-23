#!/bin/bash
#somn bout doing a computery temperature
#measures GPU and CPU temp for rpi in Celsius
cpu=$(</sys/class/thermal/thermal_zone0/temp)
echo "$(date) @ $(hostname)"
echo "-------------------------------------------"

while true
do echo "GPU => $(/opt/vc/bin/vcgencmd measure_temp)"
echo "CPU => $((cpu/1000))'C"
sleep 1
done
