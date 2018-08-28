# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import sys,os,select
import serial
import time
ser = serial.Serial(sys.argv[1],int(sys.argv[2]))

last_print=time.time()
#pad=b'\x00\xff'*2
pad=b'\x00\xff\x00\xff'

data_len=0
pad_len=0
tic=time.time()
while 1:
    if sys.argv[3]=='out':
        bs=128
        reader=sys.stdin.buffer
        if len(select.select([sys.stdin],[],[],0)[0])>0:
            data=reader.read(bs)
            ser.write(data)
            data_len+=len(data)
        while ser.out_waiting==0 and 1:
            pad_chunk=pad*1
            ser.write(pad_chunk)
            pad_len+=len(pad_chunk)
    else:
        bs=1
        writer=sys.stdout.buffer
        data=ser.read(bs)
        for i in range(len(pad)):
            if data[-1]==pad[i] and len(data)<len(pad):
                data+=ser.read(bs)
            else:
                break
        if data==pad: #skipping pad
            pad_len+=len(pad)
        else:
            data_len+=len(data)
            writer.write(data)

    if time.time()-tic>3:
        to_rate=1.0/3.0/1e3*8
        print('data sent rate: {:5.1f}Kbit/s pad: {:5.1f} total: {:5.1f} '\
                .format(data_len*to_rate, pad_len*to_rate, (pad_len+data_len)*to_rate),file=sys.stderr)
        tic=time.time()
        data_len=0
        pad_len=0

