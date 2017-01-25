#!/usr/bin/env python3

import json

data = json.load( open( "linmasks4.log", 'r' ) )
masks = [e["masks"] for e in data[:-1]]
flat = [hex(item) for sublist in masks for item in sublist]
print( ", ".join( flat ) )

