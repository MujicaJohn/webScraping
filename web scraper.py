import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/johnm/Desktop/WebDriver/chromedriver.exe')
driver.get('https://oxylabs.io/blog')
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

for a in soup.findAll(attrs='blog-card__content-wrapper'):
    name = a.find('h2')
    if name not in results:
        results.append(name.text)

for b in soup.findAll(attrs='blog-card__date-wrapper'):
    date = b.find('p')
    if date not in results:
        other_results.append(name.text)

df = pd.DataFrame({'Names': results, 'Dates': other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')
