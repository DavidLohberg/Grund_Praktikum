
import numpy as np
import matplotlib.pyplot as plt

# Abtastrate und Zeitvektor
Fs = 1000  # Abtastrate in Hz
T = 1.0 / Fs
N = 1000
t = np.arange(N) * T

# Signal: 50-Hz-Sinuswelle
signal = np.sin(2 * np.pi * 50 * t)

# FFT berechnen
yf = np.fft.fft(signal)
xf = np.fft.fftfreq(N, T)

# Einseitiges Amplitudenspektrum
half_n = N // 2
frequencies = xf[:half_n]
amplitudes = 2.0 / N * np.abs(yf[:half_n])

# Plot erstellen
fig, ax = plt.subplots()
ax.plot(frequencies, amplitudes)

ax.set_title("Amplitudenspektrum (FFT)")
ax.set_xlabel("Frequenz [Hz]")
ax.set_ylabel("Amplitude")
ax.grid(True)

# PDF speichern
fig.savefig("frequenzteiler.pdf", bbox_inches="tight")
