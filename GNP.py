import sqlalchemy
import pandas as pd 
import matplotlib.pyplot as plt 

conn = sqlalchemy.create_engine(
    'mysql+pymysql://root:abnegation123@localhost:3306/world'
)

qry = 'select name, GNP from country where region = "southeast asia" order by name'

df = pd.read_sql_query(sqlalchemy.text(qry), conn)
colour = ['r', 'lightpink', 'pink', 'lightcoral', 'r', 'g', 'b', 'k', 'y', 'r', 'cyan']


plt.style.use('seaborn')
plt.bar(df['name'], df['GNP'], color = colour)
plt.ylabel('Gross National Product (US$)')
plt.xlabel('Negara')
plt.xticks(rotation=60)
plt.title('Pendapatan Bruto Nasional ASEAN')
for a,b in zip(df['name'], df['GNP']):
    plt.text(a, b + 1000, str(b), ha = 'center')
plt.show()