#Connect python to sqlserver
import pyodbc

sqlServerCon = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-13K0I1P;'
                      'Database=AirlineDW;'
                      'Trusted_Connection=yes;')

cursor = sqlServerCon.cursor()
cursor.execute('SELECT * FROM DimWeather')

print('WeatherID'+'\t'+'WeatherCondition'+'\t'+'Precipitation')
for i in cursor:
    print(str(i[0])+'\t\t'+str(i[1])+'\t\t'+str(i[2]))