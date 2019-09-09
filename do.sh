#!/bin/sh

sudo python setup.py install --force
cd build/lib/vipermonkey/
cp -R core vbashell.py vmonkey.py ~/proj/emo_decode
cp -R core vbashell.py vmonkey.py ~/proj/Madeleine
cd ../../..


