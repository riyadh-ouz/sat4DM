#!/bin/bash

# Définir le timeout
timeout_value=1000

# Nom du fichier de sortie
output_file="./logs/output_satar.log"

# Exécuter la commande pour chaque combinaison de dataset_name et min_supp
datasets=("anneal" "chess" "connect" "mushroom")

for dataset in "${datasets[@]}"; do
  case $dataset in
    "anneal")
      min_supp=488
      ;;
    "chess")
      min_supp=2078
      ;;
    "connect")
      min_supp=60802
      ;;
    "mushroom")
      min_supp=813
      ;;
    *)
      echo "Dataset not recognized: $dataset"
      continue
      ;;
  esac

  min_confs=(10 20 30 40 50 60 70 80 90 100)
  for min_conf in "${min_confs[@]}"; do
    echo "Dataset: $dataset Minsupp: $min_supp Minconf: $min_conf"
    echo "Dataset: $dataset Minsupp: $min_supp Minconf: $min_conf" >> $output_file
    timeout 1000s ./satar -mnr -min-conf=$min_conf -min-supp=$min_supp ../FIM/datasets/$dataset.cnf >> $output_file
  done
done

