import matplotlib.pyplot as plt

# Données

# Anneal, conf=75
X1 = list(range(10, 101, 10))

y1 = [None, None, 369.641, 158.947, 56.158, 17.094, 4.055, 0.656, 0.1, 0.003]
y2 = [None, None, None, None, None, None, None, None, 0.937+0.037, 0.021]
y3 = [None, 393.268, 168.926, 69.3741, 22.3739, 5.96582, 1.55446, 0.385914, 0.101041, 0.002427]
y4 = [None, 502.254, 221.111, 82.1677, 25.7606, 6.68914, 1.65015, 0.427718, 0.122712, 0.005292]

# Chess, conf=75
X2 = list(range(40, 101, 5))

y5 = [None, None, 532.143, 254.017, 117.1, 51.554, 21.166, 7.803, 2.336, 0.659, 0.202, 0.058, 0.05]
y6 = [None, None, None, None, None, None, None, 39.445+71.924, 8.995+9.855, 2.080+1.028, 0.419+0.094, 0.120, 0.038]
y7 = [415.599, 196.696, 91.969, 42.4504, 19.1824, 8.53702, 3.94139, 1.80429, 0.76522, 0.387318, 0.197376, 0.070969, 0.011782]
y8 = [466.808, 218.959, 103.042, 47.1652, 21.1203, 9.63003, 4.35036, 2.00051, 0.867522, 0.436703, 0.230693, 0.088985, 0.009924]

# Connect, conf=75
X3 = list(range(75, 101, 5))

y9 = [None, 271.249, 90.545, 21.15, 1.767, 0.500]
y10 = [None, None, None, 346.191+14.642, 23.114+0.329, 0.237]
y11 = [255.619, 119.396, 51.8296, 21.4535, 9.14431, 0.067632]
y12 = [286.586, 134.634, 58.9823, 24.1623, 10.7274, 0.092557]

# Mushroom, conf=75
X4 = list(range(5, 41, 5))

y13 = [1.629, 0.609, 0.313, 0.206, 0.151, 0.12, 0.099, 0.071]
y14 = [None, None, 80.904+0.883, 23.286+0.251, 4.357+0.095, 2.276+0.058, 1.155+0.036, 0.743+0.017]
y15 = [16.132, 5.93516, 3.29098, 2.14338, 1.26164, 0.827555, 0.608754, 0.403133]
y16 = [21.2436, 6.6391, 3.42717, 2.257, 1.31311, 0.815386, 0.625005, 0.437151]

# Pumsb, conf=75
X5 = list(range(80, 101, 10))

y17 = [768.581, 3.968, 0.0331]
y18 = [None, 0.27662 + 0.668, 0.401]
y19 = [289.442, 15.9693, 0.108475]
y20 = [None] * 3




# Création des subplots
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Tracer les courbes avec des marqueurs dans chaque subplot
axs[0, 0].plot(X1, y1, marker='s', label='CP4AR')
axs[0, 0].plot(X1, y2, marker='o', label='MNR (SPMF)')
axs[0, 0].plot(X1, y3, marker='+', label='SATAR (optimisé)')
axs[0, 0].plot(X1, y4, marker='^', label='SATAR')

axs[0, 0].set_title('Dataset: Anneal, confiance=75%')
axs[0, 0].set_xlabel('Support')
axs[0, 0].set_ylabel('Temps (s)')
axs[0, 0].legend()

axs[0, 1].plot(X2, y5, marker='s', label='CP4AR')
axs[0, 1].plot(X2, y6, marker='o', label='MNR (SPMF)')
axs[0, 1].plot(X2, y7, marker='+', label='SATAR (optimisé)')
axs[0, 1].plot(X2, y8, marker='^', label='SATAR')

axs[0, 1].set_title('Dataset: Chess, confiance=75%')
axs[0, 1].set_xlabel('Support')
axs[0, 1].set_ylabel('Temps (s)')
axs[0, 1].legend()


axs[1, 0].plot(X3, y9, marker='s', label='CP4AR')
axs[1, 0].plot(X3, y10, marker='o', label='MNR (SPMF)')
axs[1, 0].plot(X3, y11, marker='+', label='SATAR (optimisé)')
axs[1, 0].plot(X3, y12, marker='^', label='SATAR')

axs[1, 0].set_title('Dataset: Connect, confiance=75%')
axs[1, 0].set_xlabel('Support')
axs[1, 0].set_ylabel('Temps (s)')
axs[1, 0].legend()
"""
axs[1, 1].plot(X4, y13, marker='s', label='CP4AR')
axs[1, 1].plot(X4, y14, marker='o', label='MNR (SPMF)')
axs[1, 1].plot(X4, y15, marker='+', label='SATAR (optimisé)')
axs[1, 1].plot(X4, y16, marker='^', label='SATAR')

axs[1, 1].set_title('Dataset: Mushroom, confiance=75%')
axs[1, 1].set_xlabel('Support')
axs[1, 1].set_ylabel('Temps (s)')
axs[1, 1].legend()
"""
axs[1, 1].plot(X5, y17, marker='s', label='CP4AR')
axs[1, 1].plot(X5, y18, marker='o', label='MNR (SPMF)')
axs[1, 1].plot(X5, y19, marker='+', label='SATAR (optimisé)')
axs[1, 1].plot(X5, y20, marker='^', label='SATAR')

axs[1, 1].set_title('Dataset: Pumsb, confiance=75%')
axs[1, 1].set_xlabel('Support')
axs[1, 1].set_ylabel('Temps (s)')
axs[1, 1].legend()


# Ajuster l'espacement entre les subplots
plt.tight_layout()
plt.tight_layout(pad=1.0)

# Afficher le graphique
plt.savefig("mnr_conf=75.svg", format='svg', bbox_inches='tight', pad_inches=0.0)
#plt.show()
