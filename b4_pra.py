import requests
from bs4 import BeautifulSoup
import datetime
from pymongo import MongoClient

#result = requests.get("https://www.newsgallery.com/post/full/dummy/39429/")
#result = requests.get("https://stage.newsgallery.com/post/full/c-gk-chesterton-the-future/27916/")
#result = requests.get("https://stage.newsgallery.com/post/full/hgello-dsad-sadsa-d-fsfdsf/28104/")


#result = requests.get("https://www.newsgallery.com/post/full/aliigddh-men-caalaan-kttne-ke-ddr-se-siitt-beltt-baandhkr-nikle-gnnpti/39774/") #post wid 2 img
#result = requests.get("https://www.newsgallery.com/post/full/gilgit-baltistan-is-technically-part-of-india-claims-ex-director-of-european-commission-while-supporting-abrogation-of-article-370/39771/") # post with video
#result = requests.get("https://www.newsgallery.com/post/full/gurugram-police-collaborates-with-google-for-spreading-traffic-related-info/39556/") #post with one image
result = requests.get("https://www.newsgallery.com/post/full/live-update-gnnesh-visrjn-aaj-log-dhuumdhaam-se-aise-mnaa-rhe-hain-annt-cturdshii/39751/") #postfor read more from ndtv


#print(result.status_code)
src = result.content

soup = BeautifulSoup(src, 'lxml')
#print(soup)
links = soup.find_all("a")


author=soup.find_all(class_="authorName")
time=soup.find_all(class_="posted_time")
category=soup.find_all(class_="newsLocation")
location_obj=soup.find_all(class_="post_location")
title= soup.find_all("h3",class_="post_title")


content=soup.find_all(class_="post_content")
content1=content[0].find_all("p")  #for short content
content2=content[0].find_all(class_="content_hidden") # for long content
content3=content[0].find_all(class_="content_display") #next two line for referal content and link
refer = content[0].find_all(class_="colorBlue")

f=lambda c1,c2: c1 if len(c1)>len(c2) else c2 
final_content = f(content1, content2)
if len(content1)==0 and len(content2)==0:
	final_content=content3

refer_link="Not found"
if final_content==content3:
	print(";;;;;;;;;;; equal to content3 ")
	refer_link=refer[0]['href']
	

attchment=soup.find_all(class_="slider_images-image")
attach = False
if len(attchment) != 0 :
	attach=True
"Dont forget to pass post id"
post = {'Title': title[0].text,'Auther':author[0].a['href'],'Time': time[0].text,'Category':category[0].find_all("li",recursive=False)[1].text,'Location': location_obj[0].a['href'], 'Content': final_content[0].text,'ReferLink': refer_link, 'IsAttachment':attach, 'TimeOfCreation': str(datetime.datetime.now())}
#print(post)

client = MongoClient()
db = client.NewsScrap
sPost = db.sPost

#sPost.insert(post)

ret=sPost.find()
print(ret.count())
for i in ret:
	print(i)
"""print(author[0].a['href'])
print(location_obj[0].a['href'])
print(title[0].text)
print(time[0].text)
print(category[0].find_all("li",recursive=False)[1].text)
print(final_content[0].text)
print("Is Attachment: ",attach)
print(refer_link)"""

