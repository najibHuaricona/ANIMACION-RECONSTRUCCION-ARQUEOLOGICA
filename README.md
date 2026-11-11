# Reconstrucción digital de la Puerta del Sol mediante Splines Cúbicos

Proyecto académico en Python con 15 puntos, 14 tramos cúbicos, coeficientes, verificación C0/C1/C2, siete etapas y video final narrado en español.

## Inicio en Windows
1. Extrae el ZIP completo.
2. Instala Python 3.10 o superior.
3. Haz doble clic en `INICIAR.bat`.
4. Se abrirá `http://127.0.0.1:8000`.

## Archivos
- `assets/`: visualización de trabajo.
- `data/puntos_control.csv`: 15 puntos de control.
- `data/coeficientes_spline.csv`: coeficientes de 14 intervalos.
- `data/resumen_calculo.json`: método y errores.
- `src/spline.py`: algoritmo del spline paramétrico.
- `outputs/video_final_con_narracion.mp4`: video final.
- `outputs/video_presentacion_puerta_del_sol.mp4`: video sin voz.
- `outputs/paso_1.png` a `paso_7.png`: siete etapas.
- `docs/guion_narracion.txt`: narración del video.

## Modelo matemático
Para cada intervalo: X_i(t)=a_x+b_xu+c_xu^2+d_xu^3; Y_i(t)=a_y+b_yu+c_yu^2+d_yu^3, con u=t-t_i. El parámetro es centrípeto y se utiliza condición natural en los extremos.

## Limitación metodológica que debes declarar
La imagen incluida es una visualización educativa generada por IA, no una fotografía arqueológica. Los puntos y resultados se calcularon sobre ella. Si el docente exige fotografía real, sustituye la imagen por una fotografía propia o autorizada, digitaliza de nuevo los puntos y regenera los resultados. No presentes la visualización como foto real.

Ejecuta `python -m unittest discover -s tests -v` para probar el algoritmo.
