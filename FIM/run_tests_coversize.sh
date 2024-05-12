#!/bin/bash

# Nom du fichier de sortie
log_file="./logs/output_coversize.log"

# Exécuter la commande pour chaque combinaison de dataset_name et min_supp
datasets=("anneal" "chess" "connect" "mushroom" "BMS1" "BMS2" "retail" "pumsb")

for dataset in "${datasets[@]}"; do

  case $dataset in
    "anneal")
      min_supps=("0.10" "0.20" "0.30" "0.40" "0.50" "0.60" "0.70" "0.80" "0.90" "1.00")
      ;;
    "chess")
      min_supps=("0.10" "0.20" "0.30" "0.40" "0.50" "0.60" "0.70" "0.80" "0.90" "1.00")
      ;;
    "connect")
      min_supps=("0.10" "0.20" "0.30" "0.40" "0.50" "0.60" "0.70" "0.80" "0.90" "1.00")
      ;;
    *)
      #echo "Dataset not recognized: $dataset"
      #continue
      min_supps=("0.10" "0.20" "0.30" "0.40" "0.50" "0.60" "0.70" "0.80" "0.90" "1.00")
      ;;
  esac
  
  echo "=============================== Closed Frequent Itmesets ============================" >> $log_file

  for min_supp in "${min_supps[@]}"; do
    echo "Dataset: $dataset, min-supp: $min_supp, closed"
    timeout 1000s java -jar oscar.coversize.1.0.0.jar C ./datasets/$dataset $min_supp >> $log_file
  done
    
done

