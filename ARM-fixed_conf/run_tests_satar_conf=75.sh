#!/bin/bash

# Définir min_conf à 75
min_conf=75

# Définir le timeout
timeout_value=1000

# Nom du fichier de sortie
output_file="./logs/output_satar.log"

# Exécuter la commande pour chaque combinaison de dataset_name et min_supp
datasets=("anneal" "chess" "connect" "mushroom")

for dataset in "${datasets[@]}"; do
  case $dataset in
    "anneal")
      min_supps=("82" "163" "244" "325" "406" "488" "569" "650" "731" "812")
      ;;
    "chess")
      min_supps=("1279" "1439" "1598" "1758" "1918" "2078" "2238" "2397" "2557" "2717" "2877" "3037" "3196")
      ;;
    "connect")
      min_supps=("50668" "54046" "57424" "60802" "64180" "67557")
      ;;
    "mushroom")
      min_supps=("407" "813" "1219" "1625" "2031" "2438" "2844" "3250")
      ;;
    *)
      echo "Dataset not recognized: $dataset"
      continue
      ;;
  esac

  for min_supp in "${min_supps[@]}"; do
    echo "Dataset: $dataset Minsupp: $min_supp"
    timeout 1000s ./satar -mnr -min-conf=$min_conf -min-supp=$min_supp ../FIM/datasets/$dataset.cnf >> $output_file
  done
done

