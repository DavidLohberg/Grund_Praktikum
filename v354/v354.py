import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
def exp_func(x, a, b):
    return a * np.exp(b * x)
R = 509.5   
L = 10.11e-3    
C = 2.098e-9
U0 = 0.8
#PLot Frequenz-Spannung
def exp_func(x, a, b):
    return a * np.exp(b * x)
R = 509.5   
L = 10.11e-3    
C = 2.098e-9
U0 = 0.8
f = np.linspace(9, 59, 1000)
omega = 2 * np.pi * f *1000
UC_theorie = U0 / np.sqrt(
    (1 - L * C * omega**2)**2
    + (omega * R * C)**2
)
UC_U0 = UC_theorie/U0
fig, ax = plt.subplots()
ax.plot(f, UC_U0, label = 'Theorieplot')
mess_frequenz = np.array([
    10, 20, 27.9, 28.4, 28.9, 29.4,
    29.9, 30.4, 30.9, 31.4, 31.9, 32.4,
    32.9, 33.4, 33.9, 34.4, 34.9, 35.4,
    35.9, 36.4, 36.9, 37.4, 37.9, 50
])
mess_UC = np.array([
    1.05, 1.25, 2.05, 2.15, 2.25, 2.35,
    2.45, 2.55, 2.65, 2.75, 2.85, 2.85, 2.85,
    2.85, 2.80, 2.70, 2.55, 2.45, 2.35, 2.15, 2.10,
    1.95, 1.85, 0.95
    ])
mess_UC_U0 = mess_UC / U0
plt.scatter(
        mess_frequenz,
        mess_UC_U0,
        color="red",
        marker="x",
        label="Messwerte",
    )
plt.xlabel("f[kHz]", fontsize=12)
plt.ylabel("UC/U0", fontsize=12)
plt.grid(True)
plt.legend(loc = 'upper left')
plt.savefig ('Spannungsamplitude.pdf')
#Spannungsabfall
mess_Spannungen = np.array([
    1.24, -1.14, 1.06, -0.96, 0.86, -0.80, 0.72, -0.66, 0.6,
    -0.54, 0.46, -0.42, 0.4, -0.36, 0.32
])
mess_Spannung= mess_Spannungen / 2
mess_Zeit = np.array ([
    0, 20, 30, 50, 60, 75, 90, 105, 120, 135,
    150, 165, 180, 195, 210
])
mess_Zeit = mess_Zeit * 1e-6
norm_Spannung = np.sqrt(mess_Spannung * mess_Spannung)
(a, b), cov = curve_fit(exp_func, mess_Zeit, norm_Spannung, p0 = (1.2, 0.006))
t = np.linspace(0, 250e-6, 400)
fig, ax = plt.subplots()
plt.scatter(
        mess_Zeit,
        mess_Spannung,
        color="red",
        marker="x",
        label="Messwerte",
    )
plt.plot(t, exp_func(t, a, b), color = 'blue', label = 'fit')
plt.plot(t, - exp_func(t, a, b), color = 'blue')
plt.xlabel("t[s]", fontsize=12)
plt.ylabel("U[V]", fontsize=12)
plt.grid(True)
plt.legend()
plt.savefig ('Exp_Abfall.pdf')
#Wiederrstandsberechnung
r = 2*b *L *(-1)
print(r)
errors = np.sqrt(np.diag(cov))
print(errors)

#arctan2 
T = 1/(mess_frequenz * 1000)
a = np.array([
    0, 0, 0.3e-5, 0.3e-5, 0.3e-5,0.4e-5, 0.4e-5, 0.5e-5, 0.5e-5, 0.6e-5, 0.6e-5, 0.6e-5,
    0.7e-5, 0.7e-5, 0.8e-5, 0.8e-5, 0.8e-5, 0.9e-5, 0.9e-5, 1e-5, 1e-5, 1e-5, 1e-5, 0.9e-5
])
phi_mess = 2 * np.pi * a / T
def phi_theorie(f, R, L, C):
    omega = -2 * np.pi * f * 1000
    return np.arctan2(
        -omega * R * C,
        1 - L * C * omega**2
    )
p0 = [509.5, 10.11e-3, 2.098e-9]
popt, pcov = curve_fit(
    phi_theorie,
    mess_frequenz,
    phi_mess,
    p0=p0
)
R_fit, L_fit, C_fit = popt
f_plot = np.linspace(9, 59, 1000)
fig, ax = plt.subplots()
ax.scatter(
    mess_frequenz,
    phi_mess,
    color="red",
    marker = "x",
    label="Messwerte"
)
ax.plot(
    f_plot,
    phi_theorie(f_plot, *popt),
    color="blue",
    label="Fit"
)
theory_phi = phi_theorie(f_plot, R, L, C)
ax.plot(
    f_plot,
    theory_phi,
    color="green",
    label="Theorieplot",
    linestyle="--"
)
plt.yticks(
    [ 0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi,],
    [r"$0$", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$", r"$\frac{3\pi}{4}$", r"$\pi$"]
)
ax.set_xlabel("f [kHz]", fontsize=12)
ax.set_ylabel("Phasenverschiebung [rad]", fontsize=12)
ax.grid(True)
ax.legend()
plt.savefig('Arctan2.pdf')


