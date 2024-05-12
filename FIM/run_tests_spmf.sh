#!/bin/bash

# Nom du fichier de sortie
log_file="./logs/output_spmf.log"

# Exécuter la commande pour chaque combinaison de dataset_name et min_supp
datasets=("anneal" "chess" "connect" "BMS1" "BMS2" "retail" "pumsb")

for dataset in "${datasets[@]}"; do

  case $dataset in
    "anneal")
      min_supps=("10" "20" "30" "40" "50" "60" "70" "80" "90" "100")
      ;;
    "chess")
      min_supps=("10" "20" "30" "40" "50" "60" "70" "80" "90" "100")
      ;;
    "connect")
      min_supps=("10" "20" "30" "40" "50" "60" "70" "80" "90" "100")
      ;;
    *)
      #echo "Dataset not recognized: $dataset"
      #continue
      min_supps=("10" "20" "30" "40" "50" "60" "70" "80" "90" "100")
      ;;
  esac
  
  echo "=============================== Closed Frequent Itmesets (NEclatClosed) ============================" >> $log_file

  for min_supp in "${min_supps[@]}"; do
    echo "Dataset: $dataset, min-supp: $min_supp, closed"
    timeout 1000s java -jar spmf.jar run NEclatClosed ./datasets/$dataset.spmf output.txt $min_supp% >> $log_file
  done
    
done

