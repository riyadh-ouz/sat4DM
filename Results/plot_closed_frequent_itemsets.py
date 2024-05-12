import matplotlib.pyplot as plt

# Données

# Anneal, (y1 = COVERSIZE), (y2=NEclatClosed (SPMF)), (y3=PSAT4FIM)
X1 = list(range(10, 101, 10))

y1 = [5.548, 2.385, 1.106, 0.531, 0.267, 0.14, 0.082, 0.037, 0.02, 0.001]
y2 = [15.811, 4.597, 1.38, 0.53, 0.196, 0.101, 0.07, 0.054, 0.045, 0.037]
y3 = [2.68192, 1.33107, 0.654955, 0.347194, 0.213249, 0.132118, 0.097963, 0.062685, 0.03391, 0.02]

# Chess, (y4 = COVERSIZE), (y5=NEclatClosed (SPMF)), (y6=PSAT4FIM)
X2 = list(range(10, 101, 10))

y4 = [128.615, 28.545, 7.274, 2.033, 0.646, 0.202, 0.082, 0.033, 0.002, None]
y5 = [None, None, 148.327, 7.508, 0.982, 0.294, 0.157, 0.119, 0.101, 0.095]
y6 = [131.993, 24.222, 5.94257, 1.81017, 0.752164, 0.394016, 0.203822, 0.125426, 0.066663, 0.014099]

# Connect, (y7 = COVERSIZE), (y8=NEclatClosed (SPMF)), (y9=PSAT4FIM)
X3 = list(range(10, 101, 10))

y7 = [160.81, 55.472, 26.668, 13.671, 7.527, 3.651, 1.319, 0.325, 0.001, None]
y8 = [54.49, 9.676, 3.631, 2.43, 1.617, 1.341, 0.969, 0.919, 0.843, 0.58]
y9 = [158.576, 57.9276, 31.8137, 21.4959, 15.7039, 11.6942, 8.66147, 6.24234, 3.48848, 0.232758]

# Pumsb, (y10 = COVERSIZE), (y11=NEclatClosed (SPMF)), (y12=PSAT4FIM)
X4 = list(range(40, 101, 10))

y10 = [None, None, 97.126, 20.27, 2.598, 0.152, 0.003]
y11 = [None, 180.091, 12.465, 4.048, 1.33, 1.06, 0.832]
y12 = [897.96, 172.006, 42.7071, 23.0579, 14.9397, 10.9049, 7.99746]




# Création des subplots
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Tracer les courbes avec des marqueurs dans chaque subplot
axs[0, 0].plot(X1, y1, marker='s', label='COVERSIZE')
axs[0, 0].plot(X1, y2, marker='o', label='NEclatClosed (SPMF)')
axs[0, 0].plot(X1, y3, marker='+', label='PSAT4FIM')

axs[0, 0].set_title('Dataset: Anneal')
axs[0, 0].set_xlabel('Support')
axs[0, 0].set_ylabel('Temps (s)')
axs[0, 0].legend()

axs[0, 1].plot(X2, y4, marker='s', label='COVERSIZE')
axs[0, 1].plot(X2, y5, marker='o', label='NEclatClosed (SPMF)')
axs[0, 1].plot(X2, y6, marker='+', label='PSAT4FIM')

axs[0, 1].set_title('Dataset: Chess')
axs[0, 1].set_xlabel('Support')
axs[0, 1].set_ylabel('Temps (s)')
axs[0, 1].legend()

axs[1, 0].plot(X3, y7, marker='s', label='COVERSIZE')
axs[1, 0].plot(X3, y8, marker='o', label='NEclatClosed (SPMF)')
axs[1, 0].plot(X3, y9, marker='+', label='PSAT4FIM')

axs[1, 0].set_title('Dataset: Connect')
axs[1, 0].set_xlabel('Support')
axs[1, 0].set_ylabel('Temps (s)')
axs[1, 0].legend()

axs[1, 1].plot(X4, y10, marker='s', label='COVERSIZE')
axs[1, 1].plot(X4, y11, marker='o', label='NEclatClosed (SPMF)')
axs[1, 1].plot(X4, y12, marker='+', label='PSAT4FIM')

axs[1, 1].set_title('Dataset: Pumsb')
axs[1, 1].set_xlabel('Support')
axs[1, 1].set_ylabel('Temps (s)')
axs[1, 1].legend()

# Ajuster l'espacement entre les subplots
plt.tight_layout()
plt.tight_layout(pad=1.0)

# Afficher le graphique
plt.savefig("closed_frequent_itemsets.svg", format='svg', bbox_inches='tight', pad_inches=0.0)
#plt.show()
