import matplotlib.pyplot as plt

# Données

# Chess_utility
X1 = [200000.0, 250000.0, 300000.0, 350000.0, 400000.0, 450000.0, 500000.0, 550000.0, 600000.0, 650000.0]
y1 = [1.77861, 1.66125, 1.67216, 1.51012, 1.29751, 0.998516, 0.767791, 0.58701, 0.508216, 0.434303]

# Connect_utility
X2 = [12000000.0, 13000000.0, 14000000.0, 15000000.0, 16000000.0, 17000000.0, 18000000.0]
y2 = [24.57, 22.0693, 19.4723, 16.8807, 15.8446, 14.4384, 14.1397]

# Accidents_utility
X3 = [30000000, 27500000, 25000000, 22500000, 20000000, 17500000]
y3 = [31.1564, 31.1344, 32.6841, 33.9473, 34.7566, 35.2364]

# Mushroom_utility
X4 = [100000, 95000, 95000, 85000, 80000, 75000, 70000]
y4 = [0.076913, 0.077505, 0.072307, 0.073761, 0.077325, 0.075105, 0.083302]


# Création des subplots
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Tracer les courbes avec des marqueurs dans chaque subplot
axs[0, 0].plot(X1, y1, marker='s', label='PSAT4HUIM')

axs[0, 0].set_title('Dataset: Chess, Support=50%')
axs[0, 0].set_xlabel('Utilité')
axs[0, 0].set_ylabel('Temps (s)')
axs[0, 0].legend()

axs[0, 1].plot(X2, y2, marker='s', label='PSAT4HUIM')

axs[0, 1].set_title('Dataset: Connect, Support=50%')
axs[0, 1].set_xlabel('Utilité')
axs[0, 1].set_ylabel('Temps (s)')
axs[0, 1].legend()

axs[1, 0].plot(X3, y3, marker='s', label='PSAT4HUIM')

axs[1, 0].set_title('Dataset: Accidents, Support=50%')
axs[1, 0].set_xlabel('Utilité')
axs[1, 0].set_ylabel('Temps (s)')
axs[1, 0].legend()

axs[1, 1].plot(X4, y4, marker='s', label='PSAT4HUIM')

axs[1, 1].set_title('Dataset: Mushroom, Support=50%')
axs[1, 1].set_xlabel('Utilité')
axs[1, 1].set_ylabel('Temps (s)')
axs[1, 1].legend()

# Ajuster l'espacement entre les subplots
plt.tight_layout()
plt.tight_layout(pad=1.0)

# Afficher le graphique
plt.savefig("closed_frequent_high_utility_itemsets.svg", format='svg', bbox_inches='tight', pad_inches=0.0)
#plt.show()
