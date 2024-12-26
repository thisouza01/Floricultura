import pandas as pd
from main import tabela

# recebo o data Frame criado no main
data_frame = tabela 

# atualizo para csv
data_frame.to_csv('floricultura_csv', index=False, sep='|')
