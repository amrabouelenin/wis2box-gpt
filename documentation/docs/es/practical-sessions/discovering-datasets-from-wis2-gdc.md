---
title: Descubriendo conjuntos de datos del Catálogo Global de Descubrimiento WIS2
---

# Descubriendo conjuntos de datos del Catálogo Global de Descubrimiento WIS2

!!! abstract "Resultados de aprendizaje!"

    Al final de esta sesión práctica, podrás:

    - usar pywiscat para descubrir conjuntos de datos del Catálogo Global de Descubrimiento (GDC)

## Introducción

En esta sesión aprenderás cómo descubrir datos del Catálogo Global de Descubrimiento WIS2 (GDC).

Actualmente, están disponibles los siguientes GDCs:

- Medio Ambiente y Cambio Climático Canadá, Servicio Meteorológico de Canadá: <https://wis2-gdc.weather.gc.ca>
- Administración Meteorológica de China: <https://gdc.wis.cma.cn/api>
- Servicio Meteorológico Alemán: <https://wis2.dwd.de/gdc>

Durante las sesiones de capacitación locales, se configura un GDC local para permitir a los participantes consultar el GDC sobre los metadatos que publicaron desde sus instancias de wis2box. En este caso, los instructores proporcionarán la URL al GDC local.

## Preparación

!!! note
    Antes de comenzar, por favor inicia sesión en tu VM de estudiante.

## Instalación de pywiscat

Usa el instalador de paquetes de Python `pip3` para instalar pywiscat en tu VM:
```bash
pip3 install pywiscat
```

!!! note

    Si encuentras el siguiente error:

    ```
    WARNING: The script pywiscat is installed in '/home/username/.local/bin' which is not on PATH.
    Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
    ```

    Entonces ejecuta el siguiente comando:

    ```bash
    export PATH=$PATH:/home/$USER/.local/bin
    ```

    ...donde `$USER` es tu nombre de usuario en tu VM.

Verifica que la instalación haya sido exitosa:

```bash
pywiscat --version
```

## Encontrando datos con pywiscat

Por defecto, pywiscat se conecta al Catálogo Global de Descubrimiento de Canadá. Vamos a configurar pywiscat para consultar el GDC de entrenamiento estableciendo la variable de entorno `PYWISCAT_GDC_URL`:

```bash
export PYWISCAT_GDC_URL=http://<local-gdc-host-or-ip>
```

Vamos a usar [pywiscat](https://github.com/wmo-im/pywiscat) para consultar el GDC configurado como parte del entrenamiento.

```bash
pywiscat search --help
```

Ahora busca en el GDC todos los registros:

```bash
pywiscat search
```

!!! question

    ¿Cuántos registros se devuelven de la búsqueda?

??? success "Haz clic para revelar la respuesta"
    El número de registros depende del GDC que estés consultando. Al usar el GDC de entrenamiento local, deberías ver que el número de registros es igual al número de conjuntos de datos que han sido ingresados en el GDC durante las otras sesiones prácticas.

Intentemos consultar el GDC con una palabra clave:

```bash
pywiscat search -q observations
```

!!! question

    ¿Cuál es la política de datos de los resultados?

??? success "Haz clic para revelar la respuesta"
    Todos los datos devueltos deben especificar datos "core"

Intenta consultas adicionales con `-q`

!!! tip

    La bandera `-q` permite la siguiente sintaxis:

    - `-q synop`: encuentra todos los registros con la palabra "synop"
    - `-q temp`: encuentra todos los registros con la palabra "temp"
    - `-q "observations AND fiji"`: encuentra todos los registros con las palabras "observations" y "fiji"
    - `-q "observations NOT fiji"`: encuentra todos los registros que contienen la palabra "observations" pero no la palabra "fiji"
    - `-q "synop OR temp"`: encuentra todos los registros con "synop" o "temp"
    - `-q "obs~"`: búsqueda difusa

    Cuando busques términos con espacios, enciérralos en comillas dobles.

Obtengamos más detalles sobre un resultado de búsqueda específico que nos interese:

```bash
pywiscat get <id>
```

!!! tip

    Usa el valor `id` de la búsqueda anterior.


## Conclusión

!!! success "¡Felicidades!"

    En esta sesión práctica, aprendiste a:

    - usar pywiscat para descubrir conjuntos de datos del Catálogo Global de Descubrimiento WIS2

