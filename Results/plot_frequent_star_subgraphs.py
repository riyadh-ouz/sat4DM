import matplotlib.pyplot as plt

# Données

# Chemical_340
X1 = list(range(15, 100, 15))
y1 = [342.0, 88.0, 27.0, 8.0, 0.0, 0.0]

# imdb_binary_graph
X2 = list(range(15, 100, 15))
y2 = [75.0, 9.0, 0.0, 0.0, 1.0, 0.0]

# nci109_graph
X3 = list(range(15, 100, 15))
y3 = [None, None, None, None, None, None]




# Création des subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 4))

# Tracer les courbes avec des marqueurs dans chaque subplot

axs[0].plot(X1, y1, marker='+', label='SAT4FSGM')

axs[0].set_title('Dataset: Chemical_340')
axs[0].set_xlabel('Support')
axs[0].set_ylabel('Temps (s)')
axs[0].legend()




axs[1].plot(X2, y2, marker='+', label='SAT4FSGM')

axs[1].set_title('Dataset: imdb_binary_graph')
axs[1].set_xlabel('Support')
axs[1].set_ylabel('Temps (s)')
axs[1].legend()




axs[2].plot(X3, y3, marker='+', label='SAT4FSGM')

axs[2].set_title('Dataset: nci109_graph')
axs[2].set_xlabel('Support')
axs[2].set_ylabel('Temps (s)')
axs[2].legend()



# Ajuster l'espacement entre les subplots
plt.tight_layout()
plt.tight_layout(pad=1.0)

# Afficher le graphique
plt.savefig("frequent_star_subgraphs.svg", format='svg', bbox_inches='tight', pad_inches=0.0)
#plt.show()
