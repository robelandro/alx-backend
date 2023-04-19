#!/bin/bash

pycodestyle **/*.py
if [ $? -ne 0 ]
then
	echo "PEP8 style check FAILED"
	exit 1
else
	echo "PEP8 style check PASSED"
	exit 0
fi
