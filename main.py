# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import csv

with open('COVID-19_DataSet.csv', mode='w') as csv_file:

     fieldnames = ['Country', 'Year', 'Month', 'COVID patients', 'Vaccination Drive', 'Recoveries', 'Deaths']
     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

     writer.writeheader()
     writer.writerow({'Country': 'INDIA', 'Year': '2020', 'Month': 'March', 'COVID patients': '1071', 'Vaccination Drive' : 'None', 'Recoveries' : '100', 'Deaths' : '29'})
     writer.writerow({'Country': 'INDIA', 'Year': '2020', 'Month': 'April', 'COVID patients': '33,062', 'Vaccination Drive' : 'None', 'Recoveries' : '10,000', 'Deaths' : '1079'})
     writer.writerow({'Country': 'INDIA', 'Year': '2020', 'Month': 'May', 'COVID patients': '139,049', 'Vaccination Drive' : 'None', 'Recoveries' : '1200', 'Deaths' : '4,000'})
     writer.writerow({'Country': 'INDIA', 'Year': '2020', 'Month': 'June', 'COVID patients': '549,036', 'Vaccination Drive' : 'None', 'Recoveries' : '800', 'Deaths' : '16,908'})
     writer.writerow({'Country': 'INDIA', 'Year': '2020', 'Month': 'July', 'COVID patients': '1,482,490', 'Vaccination Drive' : 'None', 'Recoveries' : '953,099', 'Deaths' : '33,020'})
     writer.writerow({'Country': 'INDIA', 'Year': '2020', 'Month': 'August', 'COVID patients': '3,432,490', 'Vaccination Drive' : 'None', 'Recoveries' : '2,583,099', 'Deaths' : '61,202'})
     writer.writerow({'Country': 'INDIA', 'Year': '2020', 'Month': 'September', 'COVID patients': '5,089,490', 'Vaccination Drive' : 'None', 'Recoveries' : '1,755,099', 'Deaths' : '92,020'})
     writer.writerow({'Country': 'INDIA', 'Year': '2020', 'Month': 'October', 'COVID patients': '8,082,490', 'Vaccination Drive' : 'None', 'Recoveries' : '7,371,099', 'Deaths' : '121,344'})
     writer.writerow({'Country': 'INDIA', 'Year': '2020', 'Month': 'November', 'COVID patients': '9,882,490', 'Vaccination Drive' : 'None', 'Recoveries' : '9,853,099', 'Deaths' : '135,020'})
     writer.writerow({'Country': 'INDIA', 'Year': '2020', 'Month': 'December', 'COVID patients': '10,382,490', 'Vaccination Drive' : 'None', 'Recoveries' : '10,993,099', 'Deaths' : '149,020'})
     writer.writerow({'Country': 'INDIA', 'Year': '2021', 'Month': 'January', 'COVID patients': '10,382,490',  'Vaccination Drive': 'None', 'Recoveries': '10,993,099', 'Deaths': '149,020'})
     writer.writerow({'Country': 'INDIA', 'Year': '2021', 'Month': 'Febuary', 'COVID patients': '20,382,490',  'Vaccination Drive': 'None', 'Recoveries': '15,393,339', 'Deaths': '180,020'})


