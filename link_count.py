
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time
import pandas as pd




driver = webdriver.Chrome()

data={'post_id':[0]}
df=pd.DataFrame(data)
print("data frame printting ")

try:
	for i in range(1,40000):
		driver.get("https://www.newsgallery.com/post/full/dummy/"+str(i)+"/")
		links=driver.find_elements(By.TAG_NAME,"a")
		if len(links) > 14:
			print(i)
		
			df.loc[df.shape[0]]=i
			

		else:
			print("no value found at ..............."+str(i))


		print(df)
		#print(df.dtypes)

except:
	print("saving dataframe in emergency")
	df.to_csv('post_id.csv', header=False, index=False) 


else:
	print("exiting Normally")
	df.to_csv('post_id.csv', header=False, index=False) 





# 14 in case of 404
# 51 in case of post

