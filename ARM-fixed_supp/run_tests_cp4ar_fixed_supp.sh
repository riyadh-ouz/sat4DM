#!/bin/bash

# Fonction pour exécuter la commande avec les arguments fournis
run_command() {
  java -cp CP4AR-v1.1.jar:oscar.coversize.1.0.0.jar org.eclipse.jdt.internal.jarinjarloader.JarRsrcLoader MNR "$@"
}


# Définir le timeout
timeout_value=1000

# Nom du fichier de sortie
output_file="./logs/output_cp4ar.log"

# Exécuter la commande pour chaque combinaison de dataset_name et min_supp
datasets=("anneal" "chess" "connect" "mushroom" "BMS1" "BMS2" "retail" "pumsb")

for dataset in "${datasets[@]}"; do
  case $dataset in
    "anneal")
      min_supp=0.60
      ;;
    "chess")
      min_supp=0.65
      ;;
    "connect")
      min_supp=0.90
      ;;
    "mushroom")
      min_supp=0.10
      ;;
    *)
      #echo "Dataset not recognized: $dataset"
      #continue
      min_supp=0.50
      ;;
  esac

  min_confs=(10 20 30 40 50 60 70 80 90 100)
  for min_conf in "${min_confs[@]}"; do
    echo "Dataset: $dataset Minsupp: $min_supp Minconf: $min_conf"
    echo "Dataset: $dataset Minsupp: $min_supp Minconf: $min_conf" >> $output_file
    run_command -to $timeout_value ../FIM/datasets/$dataset $min_supp $min_conf >> $output_file
  done
done


