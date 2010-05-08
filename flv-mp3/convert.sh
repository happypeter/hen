#!/bin/bash

inputFile=$1
outputFile=$1".wav"
finalOutput=$1".mp3"
ffmpeg -i $inputFile $outputFile
lame $outputFile $finalOutput
exit 0
