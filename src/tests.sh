#!/bin/bash

printf 'Please enter the number of tests repetitions you want to do:\n> '
read REP

I=1
while [ $I -le $REP ]
do
    make execute_tests SUITE=tests_$I
    (( I++ ))
done
