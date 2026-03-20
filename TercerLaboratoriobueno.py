# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:12:29 2026

@author: ASUS
"""

# -- coding: utf-8 --
"""
Analisis de señales de voz
Tiempo - FFT - Caracteristicas espectrales
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks, butter, filtfilt 

# ==========================
# Filtro pasa banda
# ==========================

def filtro_pasabanda(signal, fs, f_low, f_high, orden=4):

    nyquist = fs / 2
    low = f_low / nyquist
    high = f_high / nyquist
    b, a = butter(orden, [low, high], btype='band')
    señal_filtrada = filtfilt(b, a, signal)

    return señal_filtrada

# Lista de archivos de audio
archivos = [
"hombre1.wav",
"hombre2.wav",
"hombre3.wav",
"mujer1.wav",
"mujer2.wav",
"mujer3.wav"
]

# Tabla de resultados
print("\nRESULTADOS\n")
print("Archivo | F0 (Hz) | Frec media (Hz) | Brillo (Hz) | Energia")
print("\nMEDICION DE JITTER Y SHIMMER\n")
print("Archivo | Jitter_abs | Jitter_rel(%) | Shimmer_abs | Shimmer_rel(%)\n")
for archivo in archivos:
    
    # Cargar archivo
    fs, señal = wavfile.read(archivo)
    
    # Si el audio es estereo se convierte a mono
    if len(señal.shape) > 1:
        señal = señal[:,0]
    
    # Normalizar señal
    señal = señal / np.max(np.abs(señal))

    # Dominio del tiempo
    t = np.arange(len(señal)) / fs
        
    plt.figure()
    plt.plot(t, señal)
    plt.title("Señal de voz - " + archivo)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("[-]")
    plt.grid()
    plt.show()

    # Transformada de Fourier
    N = len(señal)
    fft_signal = fft(señal)
    magnitud = np.abs(fft_signal)
    frecuencias = fftfreq(N, 1/fs)

    # Solo frecuencias positivas
    frec_pos = frecuencias[:N//2]
    mag_pos = magnitud[:N//2]

    plt.figure()
    plt.semilogx(frec_pos, mag_pos)
    plt.title("Espectro de frecuencia - " + archivo)
    plt.xlabel("Frecuencia (Hz)")
    plt.xlim(10, 80000)  # asegura el rango de la transformada de fourier
    plt.ylabel("presencia en la señal")
    plt.grid()
    plt.show()

    
    # Frecuencia fundamental
    
    # Buscar picos en el espectro
    peaks, _ = find_peaks(mag_pos, height=np.max(mag_pos)*0.1)
    
    if len(peaks) > 0:
        f0 = frec_pos[peaks[0]]
    else:
        f0 = 0

    mask = (frec_pos >= 50) & (frec_pos <= 4000)
    frec_pos = frec_pos[mask]
    mag_pos = mag_pos[mask]
    
    # Frecuencia media    
    frecuencia_media = np.sum(frec_pos * (mag_pos**2)) / np.sum(mag_pos**2)
    

    # Brillo (centroide espectral)
    brillo = frecuencia_media

    # Energia de la señal
    energia = np.sum(señal**2)

    # Mostrar resultados
    
    print(f"{archivo} | {f0:.2f} | {frecuencia_media:.2f} | {brillo:.2f} | {energia:.2f}")
    
    # ==========================
# PARTE B
# Medición de Jitter y Shimmer
# ==========================

    # ==========================
    # Filtro segun voz
    # ==========================

    if "hombre" in archivo:
        señal_filtrada = filtro_pasabanda(señal, fs, 80, 240)
        
    else:
        señal_filtrada = filtro_pasabanda(señal, fs, 165, 280)
    # ==========================
    # Tiempo
    # ==========================
    t = np.arange(len(señal_filtrada)) / fs
    # ==========================
    # Grafica señal filtrada
    # ==========================
    plt.figure()
    plt.plot(t, señal_filtrada)
    plt.title("Señal filtrada - " + archivo)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("[-]")
    plt.grid()
    plt.show()
   
    # ==========================
    # Calculo de F0 con autocorrelación 
    # ==========================

    corr = np.correlate(señal_filtrada, señal_filtrada, mode='full')
    corr = corr[len(corr)//2:]

    corr[0] = 0

    # Rango de voz humana
    min_lag = int(fs / 400)
    max_lag = int(fs / 80)

    lag = np.argmax(corr[min_lag:max_lag]) + min_lag

    T0 = lag / fs
    f0 = 1 / T0
    
    # ==========================
    # Detectar picos REALES en la señal
    # ==========================

    distance = int(0.8 * T0 * fs)

    peaks, _ = find_peaks( señal_filtrada, height=0.1, distance=int(0.8 * T0 * fs), prominence=0.08 )
    
    
    # ==========================
    # Grafica con picos
    # ==========================

    plt.figure()
    plt.plot(t, señal_filtrada)
    plt.plot(peaks/fs, señal_filtrada[peaks], "ro")
    plt.title("Picos detectados - " + archivo)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("[-]")
    plt.grid()
    plt.show()

    # ==========================
    # Calculo de periodos Ti
    # ==========================
    tiempos = peaks / fs
    Ti = np.diff(tiempos)
    
    # Limpiar valores raros
    Ti = Ti[(Ti > 0.5*T0) & (Ti < 1.5*T0)]
    
    if len(Ti) < 2:
        print(archivo, "No suficientes ciclos")
        continue

    # ==========================
    # JITTER ABSOLUTO Y RELATIVO 
    # ==========================
    
    jitter_abs = np.mean(np.abs(np.diff(Ti)))
    jitter_rel = (jitter_abs / np.mean(Ti)) * 100

    # ==========================
    # Amplitudes Ai
    # ==========================

    Ai = señal_filtrada[peaks]

    # Limpiar amplitudes raras
    Ai = Ai[(Ai > 0.5*np.mean(Ai)) & (Ai < 1.5*np.mean(Ai))]

    if len(Ai) < 2:
        print(archivo, "No suficientes picos")
        continue

    shimmer_abs = np.mean(np.abs(np.diff(Ai))) 
    shimmer_rel = (shimmer_abs / np.mean(Ai)) * 100

    # ==========================
    # Mostrar resultados
    # ==========================

    print(f"{archivo} | {jitter_abs:.6f} | {jitter_rel:.4f} | {shimmer_abs:.6f} | {shimmer_rel:.4f}")

  