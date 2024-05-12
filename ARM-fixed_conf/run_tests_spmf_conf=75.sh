#!/bin/bash

# Définir min_conf à 75
min_conf=75

# Définir le timeout
timeout_value=1000

# Nom du fichier de sortie
output_file="./logs/output_spmf.log"

# Exécuter la commande pour chaque combinaison de dataset_name et min_supp
datasets=("anneal" "chess" "connect" "mushroom" "BMS1" "BMS2" "retail" "pumsb")

for dataset in "${datasets[@]}"; do
  case $dataset in
    "anneal")
      min_supps=("0.10" "0.20" "0.30" "0.40" "0.50" "0.60" "0.70" "0.80" "0.90" "1.00")
      ;;
    "chess")
      min_supps=("0.40" "0.45" "0.50" "0.55" "0.60" "0.65" "0.70" "0.75" "0.80" "0.85" "0.90" "0.95" "1.00")
      ;;
    "connect")
      min_supps=("0.75" "0.80" "0.85" "0.90" "0.95" "1.00")
      ;;
    "mushroom")
      min_supps=("0.05" "0.10" "0.15" "0.20" "0.25" "0.30" "0.35" "0.40")
      ;;
    *)
      #echo "Dataset not recognized: $dataset"
      #continue
      min_supps=("0.10" "0.20" "0.30" "0.40" "0.50" "0.60" "0.70" "0.80" "0.90" "1.00")
      ;;
  esac

  for min_supp in "${min_supps[@]}"; do
    echo "Dataset: $dataset Minsupp: $min_supp"
    echo "Dataset: $dataset Minsupp: $min_supp" >> $output_file
    timeout 1000s java -jar spmf.jar run MNR ../FIM/datasets/$dataset.spmf output.txt $min_supp $min_conf% >> $output_file
  done
done

