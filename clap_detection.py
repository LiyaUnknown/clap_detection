import numpy as np 
import pyaudio as pa 
import struct 
import matplotlib.pyplot as plt
import os 
def clap_detection() : 
   CHUNK = 2024 * 2
   FORMAT = pa.paInt16
   CHANNELS = 1
   RATE = 44100 
   p = pa.PyAudio()
   stream = p.open(
       format = FORMAT,
       channels = CHANNELS,
       rate = RATE,
       input=True,
       output=True,
       frames_per_buffer=CHUNK
   )
   tab_num = 0
   j = 0
   tl = []
   num = 0 
   while True :  
       data = stream.read(CHUNK)
       dataInt = struct.unpack(str(CHUNK) + 'h', data)
       for i in enumerate(dataInt) : 
           if i[1] > 25000 :
               num , j = 0 , 0
               for i in (dataInt) : 
                   if i > 25000 :
                       j = 1
                       num =  num + 1
       if num < 10 and num != 0 and j == 1 :
           os.system('cls')
           tab_num = tab_num + 1
           tl.append('+')
           print(f'Tab Detection {tab_num}')
           j , num = 0 , 0
       if tab_num == 1 : 
           tl.append('*')
       if tab_num > 1 : 
           if (tl.count('*')) < 11 : 
               print('two tab detection')
               clap_detection()
           else : 
               clap_detection()
clap_detection()