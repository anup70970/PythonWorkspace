import pandas as pd

read_data = pd.read_html('https://www.simpliance.in/holiday-list/maharashtra')

print(read_data)

with open('data.txt','w') as op:
    op.write(str(read_data))
    op.close()
