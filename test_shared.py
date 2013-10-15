from pyplant import *

usr = 'dalanders'
psw = 'Shadow@3876'

token = ListTokens(usr,psw,True)

ListSharedDir(usr,token,'data/Syngenta/PEDMAP','kamichels')