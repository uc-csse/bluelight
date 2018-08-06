#/bin/bash
gst-launch-1.0 v4l2src ! image/jpeg,width=640,height=480 ! jpegdec ! x264enc threads=1 bitrate=600 tune=zerolatency ! filesink location=/dev/stdout | pv | python -u stdpipe.py /dev/ttyUSB0 1000000 out
