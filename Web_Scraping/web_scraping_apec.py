from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd 


# Specify the path to chromedriver
chromedriver_path = "chromedriver.exe"
service = Service(chromedriver_path)

driver = webdriver.Chrome(service=service)
#driver.get('https://www.example.com')


#driver = webdriver.Chrome('chromedriver.exe') 
x=driver.get('https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles=data%20scientist&page={page}');

myElem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'card-offer__company')))

#options to let the window open

#on recupere le titre de chaque offre et on le stock dans un tableau 
jobs={
    "Title":[],
    "Company":[],
    "Description":[],
    "Salaire":[],
    "Type_Contrat":[],
    "Localisation":[],
    "Date_Publication":[]
}
for page in range(10):
        
    #on recupere le bloc contenant tous les informations 
    job_board=driver.find_elements(By.CLASS_NAME, 'card-offer__text')
    #chaque bloc est ajouté dans le tableau 
    for offre in job_board:
        title = offre.find_element(By.CLASS_NAME,'card-title ')
        company = offre.find_element(By.CLASS_NAME,'card-offer__company ')
        description = offre.find_element(By.CLASS_NAME,'card-offer__description')
        salaire = offre.find_element(By.TAG_NAME,"li")
        type_contrat = offre.find_element(By.XPATH,'ul[@class="details-offer important-list"]/li[1]') 
        localisation = offre.find_element(By.XPATH,'ul[@class="details-offer important-list"]/li[2]') 
        date_publication = offre.find_element(By.XPATH,'ul[@class="details-offer important-list"]/li[3]') 

        #details_offer = offre.find_element(By.CLASS_NAME,'details-offer')
        #for detail in details_offer:
        #    type_contrat = details_offer.find_element(By.TAG_NAME,'li')
        #   localisation = details_offer.find_elements(By.TAG_NAME,'li')
        #  date_publication = details_offer.find_elements(By.TAG_NAME,'li')

    #on ajoute les elements dans le dict
        jobs['Title'].append(title.text)
        jobs['Company'].append(company.text)
        jobs['Description'].append(description.text)
        jobs['Salaire'].append(salaire.text)
        jobs['Type_Contrat'].append(type_contrat.text)
        jobs['Localisation'].append(localisation.text)
        jobs['Date_Publication'].append(date_publication.text)

        
#print(jobs['Localisation'])

    print(f"the page that was scraped is page number{page}")

#formatter le dictionnaire pour obtenir dataframe puis exporter en csv
pd.DataFrame(jobs).to_csv('Jobs_Apex.csv')


search_box=driver.find_element(By.ID, 'keywords')
search_box.send_keys('ChromeDriver')
search_box.submit()
input()
driver.quit()
