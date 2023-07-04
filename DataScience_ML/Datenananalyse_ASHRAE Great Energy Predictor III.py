import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Einlesen der Datensätze
df_meta = pd.read_csv('ashrae3-building_metadata.csv')
df_weather = pd.read_csv('ashrae3-weather_train.csv')
df_train = pd.read_csv('ashrae3-train.csv')

## wir behalten nur die für die Fragen relevanten Spalten der Datensätze, da sonst das Notebook abstürzt
df_meta = df_meta.drop(columns=['year_built', 'floor_count'])
df_weather = df_weather.drop(columns=['cloud_coverage','dew_temperature', 'precip_depth_1_hr', 'sea_level_pressure','wind_direction', 'wind_speed'])

# timestamp auf selbe Datentypen bringen
df_train['timestamp'] = pd.to_datetime(df_train['timestamp'])
df_weather['timestamp'] = pd.to_datetime(df_weather['timestamp'])



# der meter Wert in Zeilen wo meter_reading = 0 ist, muss mit 0.2931 multipliziert werden (siehe: https://www.kaggle.com/c/ashrae-energy-prediction/discussion/119261)
df_train.loc[df_train['meter_reading'] == 0, 'meter'] *= 0.2931

## Zeilen mit fehlenden Informationen entfernen
df_weather = df_weather.dropna()
df_train = df_train.dropna()
df_meta = df_meta.dropna()

# Merge df_train and df_weather on 'building_id
df = pd.merge(df_train, df_meta, on='building_id')

# Merge dieses nun mit df_weather
final_df = pd.merge(df, df_weather, on=['site_id', 'timestamp'], how='left')

# droppe weitere nicht verwendete Spalten
final_df = final_df.drop(columns=['building_id', 'site_id'])

# Datentyp Konversionen, um genutzten Speicherplatz zu verringern, da Notebook immer noch die ganz Zeit abstürzt
final_df['meter'] = final_df['meter'].astype('int8')
final_df['square_feet'] = final_df['square_feet'].astype('int32')
final_df['air_temperature'] = final_df['air_temperature'].astype('float32')

# nehme zufälliges Sample von der Hälfte der Daten, in der Hoffnung, dass die Merkmale der Daten erhalten bleibt und wir das Notebook verwenden können ohne dass dieses abstürzt
sampled_df = final_df.sample(frac=0.5, random_state=1)

# speichere als csv-Datei, um in Notebook einlesen zu können
sampled_df.to_csv('final_df.csv', index=False)