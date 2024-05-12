#!/bin/bash

# Définir le timeout
timeout_value=1000

# Nom du fichier de sortie
output_file="./logs/output_psat4ARM.log"

# Exécuter la commande pour chaque combinaison de dataset_name et min_supp
datasets=("anneal" "chess" "connect" "mushroom" "BMS1" "BMS2" "retail" "pumsb")

for dataset in "${datasets[@]}"; do
  case $dataset in
    "anneal")
      min_supp=60
      ;;
    "chess")
      min_supp=65
      ;;
    "connect")
      min_supp=90
      ;;
    "mushroom")
      min_supp=10
      ;;
    *)
      #echo "Dataset not recognized: $dataset"
      #continue
      min_supp=50
      ;;
  esac

  min_confs=(10 20 30 40 50 60 70 80 90 100)
  for min_conf in "${min_confs[@]}"; do
    echo "Dataset: $dataset Minsupp: $min_supp Minconf: $min_conf"
    echo "Dataset: $dataset Minsupp: $min_supp Minconf: $min_conf" >> $output_file
    timeout 1000s ./psat4ARM -mnr -min-conf=$min_conf -min-supp=$min_supp ../FIM/datasets/$dataset.cnf >> $output_file
  done
done

