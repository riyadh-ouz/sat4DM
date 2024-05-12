import matplotlib.pyplot as plt

# Données

# Chess_utility
X1 = [200000.0, 250000.0, 300000.0, 350000.0, 400000.0, 450000.0, 500000.0, 550000.0, 600000.0, 650000.0]

y1 = [59.5553, 26.6861, 12.7407, 6.61296, 3.82646, 2.43835, 1.79711, 1.5194, 1.34268, 1.25208]
y2 = [None, None, 503.951, 193.975, 69.672, 24.475, 8.386, 2.863, 1.075, 0.501]
y3 = [None, None, None, 133.009, 19.531, 6.438, 3.738, 3.185, 2.553, 1.668]

# Connect_utility
X2 = [12000000.0, 13000000.0, 14000000.0, 15000000.0, 16000000.0, 17000000.0, 18000000.0]

y4 = [62.719, 58.4903, 53.9256, 50.7602, 48.7655, 47.6441, 46.877]
y5 = [None, None, 470.694, 150.57, 37.382, 16.397, 12.479]
y6 = [17.847, 15.865, 11.808, 8.843, 6.959, 5.472, 6.078]

# Mushroom_utility
X3 = [100000, 95000, 90000, 85000, 80000, 75000, 70000]

y7 = [2.61993, 2.68176, 2.79538, 2.89214, 2.99713, 3.19035, 3.35683]
y8 = [2.671, 2.664, 2.757, 3.005, 3.219, 3.149, 3.579]
y9 = [2.585, 2.79, 3.118, 3.497, 3.503, 3.604, 3.97]


# Création des subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 4))

# Tracer les courbes avec des marqueurs dans chaque subplot
axs[0].plot(X1, y1, marker='s', label='PSAT4HUIM')
axs[0].plot(X1, y2, marker='+', label='EFIM-Closed (SPMF)')
axs[0].plot(X1, y3, marker='^', label='HMinerClosed (SPMF)')

axs[0].set_title('Dataset: Chess')
axs[0].set_xlabel('Utilité')
axs[0].set_ylabel('Temps (s)')
axs[0].legend()

axs[1].plot(X2, y4, marker='s', label='PSAT4HUIM')
axs[1].plot(X2, y5, marker='+', label='EFIM-Closed (SPMF)')
axs[1].plot(X2, y6, marker='^', label='HMinerClosed (SPMF)')

axs[1].set_title('Dataset: Connect')
axs[1].set_xlabel('Utilité')
axs[1].set_ylabel('Temps (s)')
axs[1].legend()

axs[2].plot(X3, y7, marker='s', label='PSAT4HUIM')
axs[2].plot(X3, y8, marker='+', label='EFIM-Closed (SPMF)')
axs[2].plot(X3, y9, marker='^', label='HMinerClosed (SPMF)')

axs[2].set_title('Dataset: Mushroom')
axs[2].set_xlabel('Utilité')
axs[2].set_ylabel('Temps (s)')
axs[2].legend()

# Ajuster l'espacement entre les subplots
plt.tight_layout()
plt.tight_layout(pad=1.0)

# Afficher le graphique
plt.savefig("closed_high_utility_itemsets.svg", format='svg', bbox_inches='tight', pad_inches=0.0)
#plt.show()
