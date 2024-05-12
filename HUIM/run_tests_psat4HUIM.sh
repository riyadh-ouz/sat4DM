#!/bin/bash

# Nom du fichier de sortie
log_file="./logs/output_psat4HUIM.log"

# Exécuter la commande pour chaque combinaison de dataset_name et min_supp
datasets=("chess_utility" "connect_utility" "accidents_utility" "BMS_utility" "foodmart" "mushroom_utility")

for dataset in "${datasets[@]}"; do

  case $dataset in
    
    "chess_utility")
      min_utils=("200000" "250000" "300000" "350000" "400000" "450000" "500000" "550000" "600000" "650000")
      ;;
    "connect_utility")
      min_utils=("12000000" "13000000" "14000000" "15000000" "16000000" "17000000" "18000000")
      ;;
    "accidents_utility")
      min_utils=("30000000" "27500000" "25000000" "22500000" "20000000" "17500000")
      ;;
    "BMS_utility")
      min_utils=("2280000" "2270000" "2260000" "2250000" "2240000" "2230000" "2220000")
      ;;
    "foodmart")
      min_utils=("3000" "2000" "1000" "500" "100" "1")
      ;;
    "mushroom_utility")
      min_utils=("100000" "90000" "95000" "85000" "80000" "75000" "70000")
      ;;

    *)
      echo "Dataset not recognized: $dataset"
      continue
      ;;
  esac
  
  echo "=============================== High-Utility Itmesets ============================" >> $log_file

  for min_util in "${min_utils[@]}"; do
    echo "Dataset: $dataset, min-util: $min_util"
    timeout 1000s ./psat4HUIM -min-util=$min_util ./datasets/$dataset.cnf >> $log_file
  done
  
  echo "=============================== Closed High-Utility Itmesets ============================" >> $log_file
  
  for min_util in "${min_utils[@]}"; do
    echo "Dataset: $dataset, min-util: $min_util, closed"
    timeout 1000s ./psat4HUIM -min-util=$min_util -closed ./datasets/$dataset.cnf >> $log_file
  done
  
  echo "=============================== Frequent High-Utility Itmesets ============================" >> $log_file
  
  for min_util in "${min_utils[@]}"; do
    echo "Dataset: $dataset, min-util: $min_util, min-supp=50%"
    timeout 1000s ./psat4HUIM -min-util=$min_util -min-supp=50 ./datasets/$dataset.cnf >> $log_file
  done
  
  echo "=============================== Frequent Closed High-Utility Itmesets ============================" >> $log_file
  
  for min_util in "${min_utils[@]}"; do
    echo "Dataset: $dataset, min-util: $min_util, min-supp=50%, closed"
    timeout 1000s ./psat4HUIM -min-util=$min_util -min-supp=50 -closed ./datasets/$dataset.cnf >> $log_file
  done
  
done

