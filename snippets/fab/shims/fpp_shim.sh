#!/bin/bash

gfortran -cpp -E -P $1 -o $2
