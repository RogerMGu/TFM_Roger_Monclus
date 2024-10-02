import pandas as pd
import os

path = 'C:/Users/Roger/Les Meves Coses/Master VIU/Asignaturas/14MBID_TFM/Actividad/' # path to this file
os.chdir(path)

# Cargar los datos de cada CCAA
df_Andalucia = pd.read_csv("datasets/Detalles/Detalles Andalucia.csv") # 22-05-2024
df_Andalucia['Com_autónoma'] = 'Andalucía' # Añadir columna con la CCAA
df_Aragon = pd.read_csv("datasets/Detalles/Detalles Aragon.csv") # 22-05-2024
df_Aragon['Com_autónoma'] = 'Aragón'
df_Cantabria = pd.read_csv("datasets/Detalles/Detalles Cantabria.csv") # 23-05-2024
df_Cantabria['Com_autónoma'] = 'Cantabria'
df_CastyLeon = pd.read_csv("datasets/Detalles/Detalles Castilla y León.csv") # 23-05-2024
df_CastyLeon['Com_autónoma'] = 'Castilla y León'
df_CastlaMancha = pd.read_csv("datasets/Detalles/Detalles Castilla-La Mancha.csv") # 23-05-2024
df_CastlaMancha['Com_autónoma'] = 'Castilla-La Mancha'
df_Cataluña = pd.read_csv("datasets/Detalles/Detalles Cataluña.csv") # 23-05-2024
df_Cataluña['Com_autónoma'] = 'Cataluña'
df_Madrid = pd.read_csv("datasets/Detalles/Detalles Madrid.csv") # 21-05-2024
df_Madrid['Com_autónoma'] = 'Comunidad de Madrid'
df_Navarra = pd.read_csv("datasets/Detalles/Detalles Navarra.csv") # 23-05-2024
df_Navarra['Com_autónoma'] = 'Comunidad Foral de Navarra'
df_Valencia = pd.read_csv("datasets/Detalles/Detalles Valencia.csv") # 23-05-2024
df_Valencia['Com_autónoma'] = 'Comunidad de Valencia'
df_Extremadura = pd.read_csv("datasets/Detalles/Detalles Extremadura.csv") # 23-05-2024
df_Extremadura['Com_autónoma'] = 'Extremadura'
df_Galicia = pd.read_csv("datasets/Detalles/Detalles Galicia.csv") # 23-05-2024
df_Galicia['Com_autónoma'] = 'Galicia'
df_Baleares = pd.read_csv("datasets/Detalles/Detalles Islas Baleares.csv") # 23-05-2024
df_Baleares['Com_autónoma'] = 'Islas Baleares'
df_Canarias = pd.read_csv("datasets/Detalles/Detalles Islas Canarias.csv") # 23-05-2024
df_Canarias['Com_autónoma'] = 'Islas Canarias'
df_Rioja = pd.read_csv("datasets/Detalles/Detalles La Rioja.csv") # 24-05-2024
df_Rioja['Com_autónoma'] = 'La Rioja'
df_PaisVasco = pd.read_csv("datasets/Detalles/Detalles País Vasco.csv") # 24-05-2024
df_PaisVasco['Com_autónoma'] = 'País Vasco'
df_Asturias = pd.read_csv("datasets/Detalles/Detalles Asturias.csv") # 24-05-2024
df_Asturias['Com_autónoma'] = 'Principado de Asturias'
df_Murcia = pd.read_csv("datasets/Detalles/Detalles Murcia.csv") # 24-05-2024
df_Murcia['Com_autónoma'] = 'Región de Murcia'
df_Ceuta = pd.read_csv("datasets/Detalles/Detalles Ceuta.csv") # 24-05-2024
df_Ceuta['Com_autónoma'] = 'Ceuta'
df_Melilla = pd.read_csv("datasets/Detalles/Detalles Melilla.csv") # 24-05-2024
df_Melilla['Com_autónoma'] = 'Melilla'

# Juntar los datos de cada CCAA
df = pd.concat([df_Andalucia, df_Aragon, df_Cantabria, df_CastyLeon, df_CastlaMancha, df_Cataluña, df_Madrid, df_Navarra, df_Valencia, df_Extremadura, 
                df_Galicia, df_Baleares, df_Canarias, df_Rioja, df_PaisVasco, df_Asturias, df_Murcia, df_Ceuta, df_Melilla])\
    .reset_index(drop=True)

# Aleatorizar
df = df.sample(frac = 1, random_state = 2022).reset_index(drop = True)

# Guardar como .csv
ruta_descargas = 'C:/Users/Roger/Downloads/' # modifica la ruta a la carpeta de descargas
nombre_archivo = 'inmuebles_alquiler_idealista_052024.csv'

df.to_csv(ruta_descargas+nombre_archivo)

# Mover el archivo a la carpeta de 'datasets' dentro del repositorio de trabajo