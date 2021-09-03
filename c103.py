#import pandas as pd 
#df=pd.DataFrame()
#print(df)


#import pandas as pd 
#data=[1,2,3,4]
#df=pd.DataFrame(data)
#print(df)

import pandas as pd
import plotly.express as px 

df=pd.read_csv('csv files/line_chart.csv')
fig=px.line(df,x="Year",y="Per capita income",color="Country",title="Per Capita Income")
fig.show()

#import pandas as pd
#import plotly.express as px 

#df=pd.read_csv('csv files/data.csv')
#fig=px.bar(df,x='Country',y='InternetUsers')
#fig.show()

#import pandas as pd
#import plotly.express as px 

#df=pd.read_csv('csv files/data.csv')
#fig=px.scatter(df,x="Population",y="Per capita",size="Percentage",color="Country",size_max=60)
#fig.show()