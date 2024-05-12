import matplotlib.pyplot as plt

# Données

# Chemical_340
X1 = list(range(15, 100, 15))

y1 = [None, None, 387.0, 11.0, 0.0, 0.0]
y2 = [2.0, 0.0, 0.0, 0.0, 0.0, 0.0]

# imdb_binary_graph
X2 = list(range(15, 100, 15))

y3 = [None, 34.0, 1.0, 0.0, 0.0, 1.0]
y4 = [407.0, 16.0, 0.0, 0.0, 0.0, 0.0]

# nci109_graph
X3 = list(range(15, 100, 15))

y5 = [None, None, None, None, None, None]
y6 = [41.0, 16.0, 8.0, 6.0, 4.0, 2.0]




# Création des subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 4))

# Tracer les courbes avec des marqueurs dans chaque subplot

axs[0].plot(X1, y2, marker='o', label='GSPAN (SPMF)')
axs[0].plot(X1, y1, marker='+', label='SAT4FSGM')

axs[0].set_title('Dataset: Chemical_340')
axs[0].set_xlabel('Support')
axs[0].set_ylabel('Temps (s)')
axs[0].legend()




axs[1].plot(X2, y4, marker='o', label='GSPAN (SPMF)')
axs[1].plot(X2, y3, marker='+', label='SAT4FSGM')

axs[1].set_title('Dataset: imdb_binary_graph')
axs[1].set_xlabel('Support')
axs[1].set_ylabel('Temps (s)')
axs[1].legend()




axs[2].plot(X3, y6, marker='o', label='GSPAN (SPMF)')
axs[2].plot(X3, y5, marker='+', label='SAT4FSGM')

axs[2].set_title('Dataset: nci109_graph')
axs[2].set_xlabel('Support')
axs[2].set_ylabel('Temps (s)')
axs[2].legend()



# Ajuster l'espacement entre les subplots
plt.tight_layout()
plt.tight_layout(pad=1.0)

# Afficher le graphique
plt.savefig("frequent_subgraphs.svg", format='svg', bbox_inches='tight', pad_inches=0.0)
#plt.show()
