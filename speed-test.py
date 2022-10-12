#!/usr/bin/env python
# Speed Test

import speedtest
sp  = speedtest.Speedtest()
print("Your Download Speed is ", sp.download())
print("Your Upload Speed is ", sp.upload())
