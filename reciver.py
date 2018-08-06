import serial
import time
ser = serial.Serial('/dev/ttyACM1')
print(ser)
fd=open('out.bin','wb')
cnt=0
tic=time.time()
while 1:
    b=ser.read(5000)
    fd.write(b)
    if cnt%1==0:
        print(b[0],5000/(time.time()-tic))
        tic=time.time()
    cnt+=1


