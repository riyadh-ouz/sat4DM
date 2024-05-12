import matplotlib.pyplot as plt

# Données

X1 = list(range(10, 101, 10))

# Anneal, Support=60%


y1 = [23.786, 23.527, 23.584, 23.732, 23.863, 23.755, 21.313, 12.446, 4.711, 0.59]
y2 = [None, None, None, None, None, None, None, None, None, None]
y3 = [7.39676, 7.41648, 7.46461, 7.58472, 7.51166, 7.3851, 6.88562, 4.94248, 2.68979, 1.03435]
y4 = [None, None, None, None, None, None, None, None, None, None]

# Chess, Support=65%
y5 = [63.013, 63.084, 62.897, 63.215, 62.646, 62.854, 59.678, 39.847, 15.474, 2.234]
y6 = [None, None, None, None, None, None, None, None, None, None]
y7 = [10.4289, 10.5404, 10.3996, 10.4155, 10.5657, 10.4751, 9.83316, 7.16985, 3.83772, 1.65244]
y8 = [None, None, None, None, None, None, None, None, None, None]

# Connect, Support=90%
y9 = [21.019, 21.247, 20.747, 21.46, 21.146, 21.131, 20.632, 21.128, 20.969, 1.469]
y10 = [363.207, 359.217, 359.054, 364.504, 359.0359, 363.1459, 366.998, 359.211, 363.805, 362.4190]
y10 = [x - 200 for x in y10]
y11 = [21.6427, 21.0299, 21.0328, 21.5506, 21.0716, 21.6055, 21.0677, 21.4939, 21.0143, 15.6819]
y12 = [None, None, None, None, None, None, None, None, None, None]

# Mushroom, Support=10%
y13 = [2.191, 1.848, 1.469, 1.137, 0.89, 0.77, 0.652, 0.568, 0.517, 0.438]
y14 = [None, None, None, None, None, None, None, None, None, None]
y15 = [18.2521, 14.0139, 10.4412, 8.63105, 7.20224, 6.48313, 6.09462, 5.86207, 5.56867, 5.44163]
y16 = [None, None, None, None, None, None, None, None, None, None]




# Création des subplots
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Tracer les courbes avec des marqueurs dans chaque subplot
axs[0, 0].plot(X1, y1, marker='s', label='CP4AR')
axs[0, 0].plot(X1, y2, marker='o', label='MNR (SPMF)')
axs[0, 0].plot(X1, y3, marker='+', label='SATAR (optimisé)')
axs[0, 0].plot(X1, y4, marker='^', label='SATAR')

axs[0, 0].set_title('Dataset: Anneal, Support=60%')
axs[0, 0].set_xlabel('Confiance')
axs[0, 0].set_ylabel('Temps (s)')
axs[0, 0].legend()

axs[0, 1].plot(X1, y5, marker='s', label='CP4AR')
axs[0, 1].plot(X1, y6, marker='o', label='MNR (SPMF)')
axs[0, 1].plot(X1, y7, marker='+', label='SATAR (optimisé)')
axs[0, 1].plot(X1, y8, marker='^', label='SATAR')

axs[0, 1].set_title('Dataset: Chess, Support=65%')
axs[0, 1].set_xlabel('Confiance')
axs[0, 1].set_ylabel('Temps (s)')
axs[0, 1].legend()


axs[1, 0].plot(X1, y9, marker='s', label='CP4AR')
axs[1, 0].plot(X1, y10, marker='o', label='MNR (SPMF)')
axs[1, 0].plot(X1, y11, marker='+', label='SATAR (optimisé)')
axs[1, 0].plot(X1, y12, marker='^', label='SATAR')

axs[1, 0].set_title('Dataset: Connect, Support=90%')
axs[1, 0].set_xlabel('Confiance')
axs[1, 0].set_ylabel('Temps (s)')
axs[1, 0].legend()

axs[1, 1].plot(X1, y13, marker='s', label='CP4AR')
axs[1, 1].plot(X1, y14, marker='o', label='MNR (SPMF)')
axs[1, 1].plot(X1, y15, marker='+', label='SATAR (optimisé)')
axs[1, 1].plot(X1, y16, marker='^', label='SATAR')

axs[1, 1].set_title('Dataset: Mushroom, Support=10%')
axs[1, 1].set_xlabel('Confiance')
axs[1, 1].set_ylabel('Temps (s)')
axs[1, 1].legend()


# Ajuster l'espacement entre les subplots
plt.tight_layout()
plt.tight_layout(pad=1.0)

# Afficher le graphique
plt.savefig("mnr_fixed_supp.svg", format='svg', bbox_inches='tight', pad_inches=0.0)
#plt.show()
