# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import sys,os,select
import serial
import time
ser = serial.Serial(sys.argv[1],int(sys.argv[2]))

last_print=time.time()
#pad=b'\x00\xff'*2
pad=b'\x00\xff\x00\xff'
prem=b'\x0A\x0B\x0C'
prem1=prem+b'\x01'
prem2=prem+b'\x02'

data_len=0
pad_len=0
tic=time.time()
bs=1024
while 1:
    if sys.argv[3]=='out':
        reader=sys.stdin.buffer
        if len(select.select([sys.stdin],[],[],0)[0])>0:
            data=reader.read(bs)
            ser.write(prem1+data)
            data_len+=len(data)
        while ser.out_waiting==0 and 1:
            pad_chunk=prem2+pad*(bs//len(pad))
            ser.write(pad_chunk)
            pad_len+=len(pad_chunk)
    else:
        writer=sys.stdout.buffer
        data=ser.read(1)
        for i in range(len(prem)):
            if data[-1]==prem[i] and len(data)<len(prem):
                data+=ser.read(1)
            else:
                break
        if data==prem: #skipping pad
            #pad_len+=len(pad)
            data=ser.read(1)
            #print('----',data,prem1[-1],file=sys.stderr)
            if ord(data)==prem1[-1]:
                data=ser.read(bs)
                data_len+=len(data)
                writer.write(data)
            elif ord(data)==prem2[-1]:
                ser.read(bs)
                pad_len+=bs

    if time.time()-tic>3:
        to_rate=1.0/3.0/1e3*8
        print('data sent rate: {:5.1f}Kbit/s pad: {:5.1f} total: {:5.1f} '\
                .format(data_len*to_rate, pad_len*to_rate, (pad_len+data_len)*to_rate),file=sys.stderr)
        tic=time.time()
        data_len=0
        pad_len=0

