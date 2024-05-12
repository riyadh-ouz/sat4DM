#!/bin/bash

# Définir min_conf à 75
min_conf=75

# Définir le timeout
timeout_value=1000

# Nom du fichier de sortie
output_file="./logs/output_psat4ARM.log"

# Exécuter la commande pour chaque combinaison de dataset_name et min_supp
datasets=("anneal" "chess" "connect" "mushroom" "BMS1" "BMS2" "retail" "pumsb")

for dataset in "${datasets[@]}"; do
  case $dataset in
    "anneal")
      min_supps=("10" "20" "30" "40" "50" "60" "70" "80" "90" "100")
      ;;
    "chess")
      min_supps=("40" "45" "50" "55" "60" "65" "70" "75" "80" "85" "90" "95" "100")
      ;;
    "connect")
      min_supps=("75" "80" "85" "90" "95" "100")
      ;;
    "mushroom")
      min_supps=("5" "10" "15" "20" "25" "30" "35" "40")
      ;;
    *)
      #echo "Dataset not recognized: $dataset"
      #continue
      min_supps=("10" "20" "30" "40" "50" "60" "70" "80" "90" "100")
      ;;
  esac

  for min_supp in "${min_supps[@]}"; do
    echo "Dataset: $dataset Minsupp: $min_supp"
    timeout 1000s ./psat4ARM -mnr -min-conf=$min_conf -min-supp=$min_supp ../FIM/datasets/$dataset.cnf >> $output_file
  done
done

