#!/bin/bash
python Compiler.py < $1 > output.code
python Interpreter.py < output.code
