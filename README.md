# Análisis espectral de la voz
## Segundo Laboratorio, procesamiento digital de señales

**Maria Camila Ospina Jara, Juan Felipe Serna Alarcón**

## Descripción
<div align="justify">
  Esta actividad de laboratorio se centró en el empleo de técnicas de análisis espectral para la diferenciación y clasificación de señales de voz según el género (masculino y femenino)
Utilizando herramientas de procesamiento digital en Python, se extrajeron atributos del dominio de la frecuencia para reconocer la importancia de parámetros como el brillo, la intensidad 
y la estabilidad vocal en contextos de ingeniería biomédica

## Introducción
Las características espectrales son fundamentales para el análisis y la comprensión de las señales de voz, ya que permiten capturar los patrones fonéticos, los rasgos del hablante y los matices lingüísticos. 
Durante esta práctica, se exploraron conceptos clave como el centroide espectral (centro de masa del espectro), la frecuencia fundamental (F0) que define la altura tonal, y la frecuencia media. Asimismo, se
abordaron medidas de inestabilidad vocal como el jitter (variación de frecuencia) y el shimmer (variación de amplitud), los cuales son indicadores de la calidad de la vibración de las cuerdas vocales y tienen una
alta relevancia en la detección de patologías y el reconocimiento de voz.

## Desarrollo de la práctica 
### Parte A: Adquisición y Caracterización Básica
En esta fase inicial, se realizó la grabación de una frase corta de aproximadamente 5 segundos en 6 sujetos distintos (3 hombres y 3 mujeres) utilizando dispositivos estandarizados y guardando
los archivos en formato .wav. Posteriormente, las señales se importaron a Python para su visualización en el dominio del tiempo, lo que permitió identificar la forma de onda y la presencia de
silencios o artefactos. Mediante la aplicación de la Transformada de Fourier, se obtuvieron los espectros de magnitud para identificar visual y numéricamente los picos de frecuencia, reportando para cada señal 
su frecuencia fundamental, frecuencia media, brillo e intensidad.

### resultados obtenidos
|Archivo     | F0 (Hz) | Frec media (Hz) | Brillo (Hz) | Energia (J)|
|------------|---------|-----------------|-------------|--------|
|hombre1.wav | 97.34   | 367.26          | 367.26      | 4165.74|
|hombre2.wav | 124.93  | 400.57          | 400.57      | 5776.35|
|hombre3.wav | 126.31  | 370.71          | 370.71      | 6723.02|
|mujer1.wav  | 69.49   | 454.73          | 454.73      | 4512.75|
|mujer2.wav  | 180.05  | 544.49          | 544.49      | 2111.32|
|mujer3.wav  | 180.08  | 475.11          | 475.11      | 3594.31|

### Parte B: Medición de Estabilidad Vocal (Jitter y Shimmer)
Para profundizar en el análisis, se seleccionaron grabaciones representativas de cada género y se aplicó un filtro pasa-banda específico (80–400 Hz para hombres y 150–500 Hz para mujeres) 
con el fin de eliminar ruidos no deseados. Se procedió a detectar los periodos de vibración y los picos de amplitud en cada ciclo para calcular el jitter relativo y el shimmer relativo. 
Los resultados se compararon con los rangos típicos para voces sanas (≤1% para jitter y ≤3–5% para shimmer), permitiendo evaluar la estabilidad de la voz de los participantes

### Parte C: Análisis Comparativo 
Finalmente, se realizó una comparación sistemática de los resultados obtenidos. Se analizaron las diferencias en la frecuencia fundamental y otros términos como el brillo y la intensidad 
entre voces masculinas y femeninas, buscando explicaciones desde la fisiología humana para justificar estos hallazgos. Esta etapa permitió reflexionar sobre la 
utilidad clínica de estas herramientas, especialmente en la evaluación de la variabilidad vocal y su potencial uso en diagnósticos biomédicos




```python

```

![Diagrama de flujo del código](2ParteA.png)


</div>
