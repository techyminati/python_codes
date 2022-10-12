#!/usr/bin/env python3
# pip install platform
import platform as pf

my_system = pf.uname()

print(f"System: {my_system.system}") 
print(f"Node Name: {my_system.node}") 
print(f"Release: {my_system.release}") 
print(f"Version: {my_system.version}") 
print(f"Machine: {my_system.machine}") 
print(f"Processor: {my_system.processor}")
