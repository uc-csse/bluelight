import serial
import time
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-b','--baudrate', help="set baudrate", type=int, default=115200)
parser.add_argument('-d','--device', help="set device e.g /dev/ttyUSB0")
parser.add_argument('-t','--type', help="s for sender r for reciver")
parser.add_argument('-bs','--blocksize', help="set the block size", type=int, default=1024)
parser.add_argument('-p','--byte_pattern', help='byte patern to send default a5',default='a5')
args = parser.parse_args()
pattern=bytes([int(args.byte_pattern,16)]) 
ser = serial.Serial(args.device,args.baudrate)
print(ser,args.blocksize,args.baudrate)
msg_cnt=0
tic=time.time()
if args.type == 's':
    to_send = pattern*args.blocksize
    msg_fmt='Sending {:10.3f} Mb/s'
else:
    msg_fmt='Reciving {:10.3f} Mb/s Error Rate {:8.4f}%'
    err_cnt=0    

while 1:
    if args.type == 's':
        ser.write(to_send)
        if time.time()-tic>1.0:
            #import pdb;pdb.set_trace()
            print(msg_fmt.format(msg_cnt*args.blocksize/(time.time()-tic)/1.e6*8))
            tic=time.time()
            msg_cnt=0
    #    tic=time.time()
    else:
        data=ser.read(args.blocksize)
        if len(data):
            err_cnt+=len(data)-data.count(pattern)
        if time.time()-tic>1.0 and msg_cnt:
            print(msg_fmt.format(msg_cnt*args.blocksize/(time.time()-tic)/1.e6*8,err_cnt/(msg_cnt*args.blocksize)*100))
            tic=time.time()
            msg_cnt=0
            err_cnt=0
    msg_cnt+=1


