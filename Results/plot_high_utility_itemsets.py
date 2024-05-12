import matplotlib.pyplot as plt

# Données

# Chess_utility
X1 = [200000.0, 250000.0, 300000.0, 350000.0, 400000.0, 450000.0, 500000.0, 550000.0, 600000.0, 650000.0]

y1 = [78.2558, 31.3089, 13.4969, 6.59274, 3.65065, 2.25553, 1.70111, 1.45551, 1.31346, 1.23531]
y2 = [144.889, 41.969, 12.938, 4.176, 2.106, 0.857, 0.766, 0.449, 0.313, 0.286]

# Connect_utility
X2 = [12000000.0, 13000000.0, 14000000.0, 15000000.0, 16000000.0, 17000000.0, 18000000.0]

y3 = [68.9398, 58.7839, 52.1584, 48.2519, 46.4387, 45.2081, 44.6158]
y4 = [7.424, 4.187, 2.839, 2.172, 2.221, 1.947, 1.815]

# Accidents_utility
X3 = [30000000, 27500000, 25000000, 22500000, 20000000, 17500000]

y5 = [598.761, 612.882, 630.115, 660.713, 711.592, 795.197]
y6 = [12.818, 14.402, 15.799, 18.814, 18.73, 21.629]

# Mushroom_utility
X4 = [100000, 95000, 90000, 85000, 80000, 75000, 70000]

y7 = [2.58825, 2.66619, 2.78731, 2.95227, 3.08028, 3.30007, 3.55428]
y8 = [2.355, 2.038, 2.318, 2.647, 4.012, 3.621, 5.236]


# Création des subplots
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Tracer les courbes avec des marqueurs dans chaque subplot
axs[0, 0].plot(X1, y1, marker='s', label='PSAT4HUIM')
axs[0, 0].plot(X1, y2, marker='+', label='EFIM (SPMF)')

axs[0, 0].set_title('Dataset: Chess, Support=50%')
axs[0, 0].set_xlabel('Utilité')
axs[0, 0].set_ylabel('Temps (s)')
axs[0, 0].legend()

axs[0, 1].plot(X2, y3, marker='s', label='PSAT4HUIM')
axs[0, 1].plot(X2, y4, marker='+', label='EFIM (SPMF)')

axs[0, 1].set_title('Dataset: Connect, Support=50%')
axs[0, 1].set_xlabel('Utilité')
axs[0, 1].set_ylabel('Temps (s)')
axs[0, 1].legend()

axs[1, 0].plot(X3, y5, marker='s', label='PSAT4HUIM')
axs[1, 0].plot(X3, y6, marker='+', label='EFIM (SPMF)')

axs[1, 0].set_title('Dataset: Accidents, Support=50%')
axs[1, 0].set_xlabel('Utilité')
axs[1, 0].set_ylabel('Temps (s)')
axs[1, 0].legend()

axs[1, 1].plot(X4, y7, marker='s', label='PSAT4HUIM')
axs[1, 1].plot(X4, y8, marker='+', label='EFIM (SPMF)')

axs[1, 1].set_title('Dataset: Mushroom, Support=50%')
axs[1, 1].set_xlabel('Utilité')
axs[1, 1].set_ylabel('Temps (s)')
axs[1, 1].legend()

# Ajuster l'espacement entre les subplots
plt.tight_layout()
plt.tight_layout(pad=1.0)

# Afficher le graphique
plt.savefig("high_utility_itemsets.svg", format='svg', bbox_inches='tight', pad_inches=0.0)
#plt.show()
