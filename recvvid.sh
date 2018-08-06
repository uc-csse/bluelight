#/bin/bash
python -u stdpipe.py /dev/ttyUSB1 1000000 in | pv | gst-launch-1.0  filesrc location=/dev/stdin ! h264parse ! avdec_h264 ! autovideosink sync=False
