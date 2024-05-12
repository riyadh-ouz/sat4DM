#!/bin/bash

echo "=========== cp4ar =============="
./run_tests_cp4ar_conf=75.sh

echo "=========== psat4ARM =============="
./run_tests_psat4ARM_conf=75.sh

echo "=========== spmf =============="
./run_tests_spmf_conf=75.sh

echo "=========== satar =============="
./run_tests_satar_conf=75.sh
