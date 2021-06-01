#!/bin/bash
# SPDX-License-Identifier: GPL-3.0-or-later
# (c) TechyMinati ( Aryan Sinha ) <sinha.aryan03@gmail.com>

ROM_URL=""
ROM_NAME=""

echo "Type ROM URL (Direct Link)"
read ROM_URL

echo "Type ROM_NAME (eg, Generic, OxygenOS, MIUI, Flyme, ColorOS,Pixel etc)"
read ROM_NAME

echo "Building GSI"

sudo ./ErfanGSIs/url2GSI.sh $ROM_URL $ROM_NAME
