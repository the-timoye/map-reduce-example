import pandas as pd

df = pd.read_csv('song_file.txt', delimiter='\n', squeeze=True)
print(df.tolist())