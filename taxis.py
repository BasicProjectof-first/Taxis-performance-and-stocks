from itertools import count
from os import stat
from statistics import mean
from tkinter.font import Font
from turtle import color, update, width
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px

from datetime import datetime



st.set_page_config (page_title="Taxi Rides",
                   page_icon=":taxi"
)
hide_st_style="""
             <style>
             #MainMenu {visibility:hidden;}
             footer {visibility:hidden;}
             footer {visibility:hidden;}
             </style>
             """
st.markdown(hide_st_style,unsafe_allow_html=True)

header=st.container()
dataset=st.container()
graphs=st.container()
with header:
   st.header("To Analyze The Performance Of Taxis")
   vid=st.video("Taxis.mp4")
   dt=pd.read_csv("taxisstocks.csv")
   dt.value_counts()
   dt.fillna(value=0,inplace=True)
   dt.drop_duplicates()
   list=dt.columns.tolist()
   st.subheader("Line Chart of Taxis rides Performance")
   choice=st.sidebar.multiselect("Choose Taxis Data Attributes",list,default="Open")
   dat=dt[choice]
   st.line_chart(dat)
   
   
   

with dataset:
   ds=pd.read_csv("ube1.csv")
   st.subheader("Description about the Taxis Performance")
   st.write(ds)
   ds.fillna(value=0,inplace=True)
   ds.drop_duplicates()
   ds.value_counts()
   #st.write(ds.memory_usage())
   st.info("Maximum and Minimum Trips of Taxis")
   st.write("Maximum Trips of Vehicles:",ds['NumberofTrips'].max())
   st.write("Minimum Trips of Vehicles:",ds["NumberofTrips"].min())
   st.write("Total Number of Trips of Vehicles:",ds["NumberofTrips"].count())
   
with graphs:
   da=pd.read_csv("ube2.csv")
   corr=da.corr()
   st.success("Correlation realtion between active_vehicles and trips of Vehicles")
   st.write(corr)
   da.drop_duplicates()
   da.fillna(value=100,inplace=True)
   da.memory_usage()
   dv=pd.read_csv("ube.csv")
   #sns.set(style="darkgrid")
   #sns.regplot(x=dt['High'],y=dt['Low'],fit_reg=False)
   #st.set_option('deprecation.showPyplotGlobalUse', False)
   #st.pyplot()
   st.subheader("The Regression Plot between active_vehicles and trips")
   sns.set(style="darkgrid")
   sns.regplot(x=da['active_vehicles'],y=da['trips'],fit_reg=False)
   st.set_option('deprecation.showPyplotGlobalUse', False)
   st.pyplot()
   #sns.boxplot(x=da['active_vehicles'],y=da['trips'])
   #st.set_option('deprecation.showPyplotGlobalUse',False)
   #st.pyplot()
   def main():
      dt=pd.read_csv('taxisstocks.csv',index_col=0)
      dt.info()
      dt.dropna(axis=0)
      dt.drop_duplicates()
      dt.memory_usage()
      st.subheader("The Description about the Taxis Stocks of Data")
      st.write(dt.describe())
      st.subheader("The sample Taxis stock Data")
      st.write(dt.head(5))
      ma=dt['Volume'].max()
      st.warning('Maximum value for Taxis stock')
      st.write("Taxis stock:",ma)
      gro=dt.groupby(['Open'])[['Close']].agg(np.mean)
      st.write("Mean of Taxis stocks Data:",gro)
      cor=dt.corr()
      st.write("Correlation about total Taxis Stocks of Data",cor)
      
      
      st.subheader("The Kernel Density Estimation Plot(KDE) of Taxis Stocks")
      fig=plt.figure()
      dt['Open'].value_counts().plot(kind="kde")
      plt.xlabel('Starting Period of trading')
      st.pyplot(fig)
      #fig2=plt.figure()
      #sns.countplot(dt['Low'],fill=True)
      #st.pyplot(fig2)
      #fig3=plt.figure()
      #sns.barplot(x="Date",y="Close",data=dt)
from itertools import count
from os import stat
from statistics import mean
from tkinter.font import Font
from turtle import color, update, width
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px

from datetime import datetime



st.set_page_config (page_title="Taxi Rides",
                   page_icon=":taxi"
)
hide_st_style="""
             <style>
             #MainMenu {visibility:hidden;}
             footer {visibility:hidden;}
             footer {visibility:hidden;}
             </style>
             """
st.markdown(hide_st_style,unsafe_allow_html=True)

header=st.container()
dataset=st.container()
graphs=st.container()
with header:
   st.header("To Analyze The Performance Of Taxis")
   vid=st.video("Taxis.mp4")
   dt=pd.read_csv("taxisstocks.csv")
   dt.value_counts()
   dt.fillna(value=0,inplace=True)
   dt.drop_duplicates()
   list=dt.columns.tolist()
   st.subheader("Line Chart of Taxis rides Performance")
   choice=st.sidebar.multiselect("Choose Taxis Data Attributes",list,default="Open")
   dat=dt[choice]
   st.line_chart(dat)
   
   
   

with dataset:
   ds=pd.read_csv("ube1.csv")
   st.subheader("Description about the Taxis Performance")
   st.write(ds)
   ds.fillna(value=0,inplace=True)
   ds.drop_duplicates()
   ds.value_counts()
   #st.write(ds.memory_usage())
   st.info("Maximum and Minimum Trips of Taxis")
   st.write("Maximum Trips of Vehicles:",ds['NumberofTrips'].max())
   st.write("Minimum Trips of Vehicles:",ds["NumberofTrips"].min())
   st.write("Total Number of Trips of Vehicles:",ds["NumberofTrips"].count())
   
with graphs:
   da=pd.read_csv("ube2.csv")
   corr=da.corr()
   st.success("Correlation realtion between active_vehicles and trips of Vehicles")
   st.write(corr)
   da.drop_duplicates()
   da.fillna(value=100,inplace=True)
   da.memory_usage()
   dv=pd.read_csv("ube.csv")
   #sns.set(style="darkgrid")
   #sns.regplot(x=dt['High'],y=dt['Low'],fit_reg=False)
   #st.set_option('deprecation.showPyplotGlobalUse', False)
   #st.pyplot()
   st.subheader("The Regression Plot between active_vehicles and trips")
   sns.set(style="darkgrid")
   sns.regplot(x=da['active_vehicles'],y=da['trips'],fit_reg=False)
   st.set_option('deprecation.showPyplotGlobalUse', False)
   st.pyplot()
   #sns.boxplot(x=da['active_vehicles'],y=da['trips'])
   #st.set_option('deprecation.showPyplotGlobalUse',False)
   #st.pyplot()
   def main():
      dt=pd.read_csv('taxisstocks.csv',index_col=0)
      dt.info()
      dt.dropna(axis=0)
      dt.drop_duplicates()
      dt.memory_usage()
      st.subheader("The Description about the Taxis Stocks of Data")
      st.write(dt.describe())
      st.subheader("The sample Taxis stock Data")
      st.write(dt.head(5))
      ma=dt['Volume'].max()
      st.warning('Maximum value for Taxis stock')
      st.write("Taxis stock:",ma)
      gro=dt.groupby(['Open'])[['Close']].agg(np.mean)
      st.write("Mean of Taxis stocks Data:",gro)
      cor=dt.corr()
      st.write("Correlation about total Taxis Stocks of Data",cor)
      
      
      st.subheader("The Kernel Density Estimation Plot(KDE) of Taxis Stocks")
      fig=plt.figure()
      dt['Open'].value_counts().plot(kind="kde")
      plt.xlabel('Starting Period of trading')
      st.pyplot(fig)
      #fig2=plt.figure()
      #sns.countplot(dt['Low'],fill=True)
      #st.pyplot(fig2)
      #fig3=plt.figure()
      #sns.barplot(x="Date",y="Close",data=dt)
      #st.pyplot(fig3)
      st.subheader("Bar Chart about the Taxis Stocks of data")
      st.bar_chart(dt['High'],)
      plt.xlabel('Highest price of stock')
      fig4=plt.figure()
      sns.kdeplot(dt.Volume,shade=True,n_levels=20)
      plt.xlabel("Total Number of shares")
      st.pyplot(fig4)
      st.subheader("Histogram plot about the Taxis Stocks")
      fig5=plt.figure()
      st.subheader("The KDE plot of Taxis Stocks")
      sns.histplot(dt.High,kde=True,bins=10,fill=True,
                   element='poly',multiple="dodge")
      
      plt.xlabel("High Price of stocks")
      plt.ylabel("Total stocks(counts)")
      
      st.pyplot(fig5)
      fig6=plt.figure()
      st.info("Violin Plot")
      st.subheader("The relation between Starting period and Total Number of stocks of Taxis data")
      sns.violinplot(x=dt.High,y=dt.Volume)
      plt.xlabel("High price of stock")
      plt.ylabel("total Number of shares")
      st.pyplot(fig6)
      fig8=plt.figure()
      st.info("Swarm Plot")
      st.subheader("The relation between End of period and Total Number of stock of Taxis data")
      sns.swarmplot(x=dt.Close,y=dt.Volume)
      plt.xlabel("Low price of stock")
      plt.ylabel("Total Number of stock")
      st.pyplot(fig8)
      st.info("Heat Map")
      dt.groupby('Open').Volume.value_counts()
      orig=(dt.groupby('Open')
            .Volume.value_counts().
            unstack().fillna(0))
      plt.xlabel("Total Number of stock")
      plt.ylabel("Starting period of Stock")
      fig9=plt.figure()
      sns.heatmap(orig)
      st.pyplot(fig9)
      st.info("Strip Plot")
      st.subheader("The Strip plot of Taxis data")
      fig10=plt.figure()
      sns.stripplot(dt.Volume)
      plt.xlabel("Total Number of stock")
      st.pyplot(fig10)
      #fig11=plt.figure()
      #st.bar_chart(dv['Date'],format='%y-%m-% d %I-%p')
      #st.pyplot(fig11)
      
      
      
   main()
   upload_file=st.file_uploader('Upload a file conataining Taxis data')
   if upload_file is not None:
      data=pd.read_csv(upload_file)
      st.header('Statistics of data')
      ds.drop_duplicates()
      ds=data.describe()
      ds.fillna(value=0,inplace=True) 
      #st.write(ds)
      ds.value_counts()
      st.subheader("Sample Data of Taxis Performance")
      st.write(data.head())
      ds.memory_usage()
      #fig,ax=plt.subplots(1,1)
      #ax.scatter(x=ds['NumberofTrips'],y=ds['NumberofVehicles'])
      #st.pyplot(fig)
      st.subheader("Line Chart of uber")
      st.line_chart(ds['NumberofTrips'])
      def vehi():
         st.subheader("Bar Chart of Performace of Taxis")
         fig=plt.figure()
         ds['NumberofVehicles'].value_counts().plot(kind="bar")
         plt.xlabel("Number of vehicles")
         st.pyplot(fig)
         #st.subheader("Count Plot of Uber data")
         #fig9=plt.figure()
         #sns.countplot(ds['NumberofVehicles'])
         #st.pyplot(fig9)
         figs=px.bar(
            ds['NumberofTrips'],
            ds['NumberofVehicles']
         )
         plt.xlabel("Number of Trips")
         plt.ylabel("Number of Vehicles")
         st.plotly_chart(figs)
         
         
         
      vehi()
