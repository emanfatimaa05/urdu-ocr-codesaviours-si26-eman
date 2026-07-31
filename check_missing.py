import pandas as pd, os
df = pd.read_csv('data/labels.csv')
missing = [f for f in df['image'] if not os.path.exists(f)]
print(f'Missing files: {len(missing)}')
print(missing)