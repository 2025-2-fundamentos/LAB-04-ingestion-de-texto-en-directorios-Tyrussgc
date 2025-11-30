# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


from pathlib import Path  #? Importa la clase Path de la librería pathlib para facilitar la manipulación de rutas de archivos y directorios.
import pandas as pd  #? Importa la librería pandas para trabajar con estructuras de datos (DataFrame) en Python.
from zipfile import ZipFile  #? Importa la clase ZipFile de la librería zipfile para manejar archivos comprimidos (.zip).

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    # Abrir y descomprimir el archivo zip
    with ZipFile("files/input.zip", "r") as z:  #? Abre el archivo zip ubicado en "files/input.zip" en modo lectura ("r").
        z.extractall("files/")  #? Extrae todos los archivos del archivo zip al directorio "files/".

    direccion_input = Path("files/input")  #? Define la ruta donde se encuentra la carpeta "input" después de la descompresión.
    direccion_output = Path("files/output")  #? Define la ruta donde se guardarán los archivos de salida (en "files/output").
    direccion_output.mkdir(parents=True, exist_ok=True)  #? Crea la carpeta "output" si no existe, incluyendo las carpetas padre si es necesario.

    for dataset in ["train", "test"]:  #? Itera sobre las carpetas "train" y "test", que contienen las subcarpetas con los archivos de texto.
        frases = []  #? Inicializa una lista vacía para almacenar las frases y sus etiquetas (sentimiento).
        for target_path in (direccion_input / dataset).iterdir():  #? Itera sobre los directorios dentro de "train" o "test".
            for file_path in target_path.iterdir():  #? Itera sobre los archivos de cada subdirectorio (por ejemplo, los archivos de texto de "negative", "positive" o "neutral").
                frase = file_path.read_text()  #? Lee el contenido del archivo de texto.
                frases.append((frase, target_path.name))  #? Añade una tupla con la frase y su etiqueta (el nombre del directorio, que es el sentimiento).
        
        df = pd.DataFrame(frases, columns=["phrase", "target"])  #? Crea un DataFrame de pandas con las frases y sus respectivas etiquetas.
        df.to_csv(direccion_output / f"{dataset}_dataset.csv")  #? Guarda el DataFrame como un archivo CSV en el directorio "output" con el nombre "train_dataset.csv" o "test_dataset.csv".