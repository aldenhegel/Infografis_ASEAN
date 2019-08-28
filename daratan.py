import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import sqlalchemy
import matplotlib


conn = sqlalchemy.create_engine(
    'mysql+pymysql://root:abnegation123@localhost:3306/world'
)

qry = 'select name, surfacearea from country where region = "southeast asia" order by name'

df = pd.read_sql_query(sqlalchemy.text(qry), conn)

plt.title('Persentase Luas Daratan ASEAN')
plt.grid(True)

plt.pie(df['surfacearea'], labels = list(df['name']), startangle=180, counterclock=False,
                autopct='%1.1f%%', textprops={'color': 'black'}
        )

plt.show()
