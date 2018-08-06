# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import sys
import serial
import time
bs=512
ser = serial.Serial(sys.argv[1],int(sys.argv[2]))

last_print=time.time()
total_len=0
while 1:
    if sys.argv[3]=='out':
        reader=sys.stdin.buffer
        writer=ser
    else:
        reader=ser
        writer=sys.stdout.buffer
    data=reader.read(bs)
    total_len+=len(data)
    if 0 and  time.time()-last_print>2.0:
        print('{:.3f}Mbits'.format(total_len/(time.time()-last_print)*8/1e6),file=sys.stderr)
        last_print=time.time()
        total_len=0
    writer.write(data)
