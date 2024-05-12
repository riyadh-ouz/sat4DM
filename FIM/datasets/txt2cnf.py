
dataset = "pumsb"

with open(dataset, 'r') as txt_file:
	with open(dataset + '.cnf', 'w') as cnf_file:
		for line in txt_file:
			
			cnf_file.write(line[:-1] + ' 0\n')
