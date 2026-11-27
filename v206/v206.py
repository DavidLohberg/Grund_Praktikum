import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Messwerte
t = np.array([
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20
])

T1 = np.array([
    21.0, 21.8, 22.6, 23.7, 25.1, 26.7, 28.3,
    30.0, 31.7, 33.2, 34.7, 36.2, 37.7, 39.1,
    40.5, 42.0, 43.2, 44.4, 45.6, 46.7, 47.7
])

T2 = np.array([
    21.0, 21.0, 21.0, 20.3, 19.0, 17.5, 15.9,
    14.2, 12.6, 11.0, 9.5, 8.2, 6.8, 5.6,
    4.6, 3.7, 3.0, 2.4, 1.9, 1.4, 1.0
])
# Temperaturenplot
fig, ax = plt.subplots()

ax.plot(t, T1, 'o-', color='red',
        label=r'$T_1$')

ax.plot(t, T2, 's-', color='blue',
        label=r'$T_2$')

# Achsenbeschriftungen
ax.set_xlabel(r'Zeit $t$ in min')
ax.set_ylabel(r'Temperatur $T$ in °C')

# Achseneinstellungen
ax.set_xticks(np.arange(0, 21, 1))

plt.grid(True)
plt.legend(loc = 'upper left')
plt.savefig ('Temperaturverlauf.pdf')
plt.show

def func_W(t, A, B, alpha, C):
    return A * t**alpha / (1 + B * t**alpha) + C

def func_K(t, A, B, alpha):
    return A / (1 + B * t**alpha)