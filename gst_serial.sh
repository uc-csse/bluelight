#gst-launch-1.0 videotestsrc horizontal-speed=01 ! video/x-raw,width=320,height=240,framerate=10/1 ! x264enc threads=1 bitrate=40 ! filesink location=/dev/stdout | pv | python stdpipe.py /dev/ttyUSB0 500000 out


#python stdpipe.py /dev/ttyUSB2 500000 in | pv | gst-launch-1.0  filesrc location=/dev/stdin ! h264parse ! avdec_h264 ! autovideosink sync=False


#### tested on laptop with pattern
gst-launch-1.0 videotestsrc horizontal-speed=01 ! video/x-raw,width=320,height=240,framerate=10/1 ! x264enc threads=1 bitrate=40 ! filesink location=/dev/stdout | pv | python stdpipe.py /dev/ttyUSB0 1000000 out

python stdpipe.py /dev/ttyUSB1 1000000 in | pv | gst-launch-1.0  filesrc location=/dev/stdin ! h264parse ! avdec_h264 ! autovideosink sync=False

#### 
gst-launch-1.0 v4l2src ! image/jpeg,width=320,height=240,framerate=15/1 ! x264enc threads=1 bitrate=40 ! filesink location=/dev/stdout | pv | python stdpipe.py /dev/ttyUSB0 1000000 out

