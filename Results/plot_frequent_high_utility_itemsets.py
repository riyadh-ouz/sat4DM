import matplotlib.pyplot as plt

# Données

# Chess_utility
X1 = [200000.0, 250000.0, 300000.0, 350000.0, 400000.0, 450000.0, 500000.0, 550000.0, 600000.0, 650000.0]

y1 = [1.85781, 1.69182, 1.49025, 1.36649, 1.14996, 0.918913, 0.707469, 0.554707, 0.470742, 0.43195]
y2 = [342.921, 340.034, 303.298, 241.04, 172.79, 103.529, 48.042, 18.503, 6.963, 2.803]

# Connect_utility
X2 = [12000000.0, 13000000.0, 14000000.0, 15000000.0, 16000000.0, 17000000.0, 18000000.0]

y3 = [32.3028, 25.528, 20.216, 17.7353, 15.8579, 14.5432, 14.507]
y4 = [None, None, None, None, 378.111, 107.587, 46.992]

# Accidents_utility
X3 = [30000000, 27500000, 25000000, 22500000, 20000000, 17500000]

y5 = [26.6368, 27.9239, 29.7587, 30.7654, 31.4368, 31.9795]
y6 = [38.471, 58.911, 85.408, 120.795, 179.233, 222.121]

# Mushroom_utility
X4 = [100000, 95000, 90000, 85000, 80000, 75000, 70000]

y7 = [0.080061, 0.077575, 0.067406, 0.080887, 0.073326, 0.078564, 0.068529]
y8 = [0.432, 0.422, 0.44, 0.446, 0.422, 0.429, 0.423]


# Création des subplots
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Tracer les courbes avec des marqueurs dans chaque subplot
axs[0, 0].plot(X1, y1, marker='s', label='PSAT4HUIM')
axs[0, 0].plot(X1, y2, marker='+', label='FHMFreq (SPMF)')

axs[0, 0].set_title('Dataset: Chess, Support=50%')
axs[0, 0].set_xlabel('Utilité')
axs[0, 0].set_ylabel('Temps (s)')
axs[0, 0].legend()

axs[0, 1].plot(X2, y3, marker='s', label='PSAT4HUIM')
axs[0, 1].plot(X2, y4, marker='+', label='FHMFreq (SPMF)')

axs[0, 1].set_title('Dataset: Connect, Support=50%')
axs[0, 1].set_xlabel('Utilité')
axs[0, 1].set_ylabel('Temps (s)')
axs[0, 1].legend()

axs[1, 0].plot(X3, y5, marker='s', label='PSAT4HUIM')
axs[1, 0].plot(X3, y6, marker='+', label='FHMFreq (SPMF)')

axs[1, 0].set_title('Dataset: Accidents, Support=50%')
axs[1, 0].set_xlabel('Utilité')
axs[1, 0].set_ylabel('Temps (s)')
axs[1, 0].legend()

axs[1, 1].plot(X4, y7, marker='s', label='PSAT4HUIM')
axs[1, 1].plot(X4, y8, marker='+', label='FHMFreq (SPMF)')

axs[1, 1].set_title('Dataset: Mushroom, Support=50%')
axs[1, 1].set_xlabel('Utilité')
axs[1, 1].set_ylabel('Temps (s)')
axs[1, 1].legend()

# Ajuster l'espacement entre les subplots
plt.tight_layout()
plt.tight_layout(pad=1.0)

# Afficher le graphique
plt.savefig("frequent_high_utility_itemsets.svg", format='svg', bbox_inches='tight', pad_inches=0.0)
#plt.show()
