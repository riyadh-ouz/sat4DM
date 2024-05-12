#!/bin/bash

# Nom du fichier de sortie
log_file_sat4FSGM="./logs/output_sat4FSGM.log"
log_file_sat4FSGM_nodec="./logs/output_sat4FSGM-nodec.log"
log_file_sat4FSGM_nocbase_8="./logs/output_sat4FSGM-nocbase8.log" 
log_file_sat4FSGM_star_graphs="./logs/output_sat4FSGM_star.log"
log_file_spmf="./logs/output_spmf.log"

# Exécuter la commande pour chaque combinaison de dataset_name et min_supp
datasets=("Chemical_340.txt" "imdb_binary_graph.txt" "nci109_graph.txt")
min_supps=(15 30 45 60 75 90)

for dataset in "${datasets[@]}"; do

  
  for min_supp in "${min_supps[@]}"; do
    echo "sat4FSGM ==> Dataset: $dataset, min-supp: $min_supp"
    timeout 1000s ./sat4FSGM ./datasets/$dataset $min_supp 1 1000000 0 0 0 1000000 >> $log_file_sat4FSGM
  done
  
  for min_supp in "${min_supps[@]}"; do
    echo "sat4FSGM ==> Dataset: $dataset, min-supp: $min_supp, star_graphs"
    timeout 1000s ./sat4FSGM ./datasets/$dataset $min_supp 1 1000000 1 0 0 1000000 >> $log_file_sat4FSGM_star_graphs
  done
  
  
  
  for min_supp in "${min_supps[@]}"; do
    echo "GSPAN ==> Dataset: $dataset, min-supp: $min_supp"
    timeout 1000s java -jar spmf.jar run GSPAN ./datasets/$dataset output.txt $min_supp% >> $log_file_spmf
  done
  
  
  
  # Pour le Master
  
  for min_supp in "${min_supps[@]}"; do
    echo "sat4FSGM ==> Dataset: $dataset, min-supp: $min_supp, no-c_base_8"
    timeout 1000s ./sat4FSGM-2 ./datasets/$dataset $min_supp 1 1000000 0 0 0 1000000 >> $log_file_sat4FSGM_nocbase_8
  done
  
  for min_supp in "${min_supps[@]}"; do
    echo "sat4FSGM ==> Dataset: $dataset, min-supp: $min_supp, no-decomposition"
    timeout 1000s ./sat4FSGM-1 ./datasets/$dataset $min_supp 1 1000000 0 0 0 1000000 >> $log_file_sat4FSGM_nodec
  done
  
done



