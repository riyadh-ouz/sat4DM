#!/bin/bash

echo "---------------------------------- ARM (conf=75) ------------------------------------"
cd ./ARM-fixed_conf
./all_in_one_arm_conf=75.sh

echo "---------------------------------- ARM (fixed_supp) ------------------------------------"
cd ../ARM-fixed_supp
./all_in_one_arm_fixed_supp.sh

echo "---------------------------------- FIM ------------------------------------"
cd ../FIM
./all_in_one_fim.sh

echo "---------------------------------- HUIM ------------------------------------"
cd ../HUIM
./all_in_one_huim.sh

echo "---------------------------------- FSGM -----------------------------------"
cd ../FSGM
./all_in_one_fsgm.sh
