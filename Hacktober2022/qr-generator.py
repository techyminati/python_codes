#!/usr/bin/env python3
import qrcode
img = qrcode.make("https://github.com/techyminati/python_codes")
img.save("output.jpg")
