import pandas as pd 
x = pd.read_csv('img.csv')
import requests
i = 0
for i in range(0,9):
    try:
        y = x.links[i]    
        img_data = requests.get(y).content
        name = 'image_name'+str(i)+'.jpg'
        with open(name, 'wb') as handler:
            handler.write(img_data)
    except KeyError:
        continue
        
  ###################################################
  #sorting images
  
 import pandas as pd 
from PIL import Image
df = pd.read_csv("/home/user/Desktop/train-annotations-human-imagelabels-boxable.csv")
filter_list = ['/m/01dws','/m/01dxs','/m/012074','/m/0120dh','/m/0152hh','/m/015p6','/m/019h78','/m/01dy8n','/m/01f8m5','/m/01gllr','/m/01h3n','/m/01h44','/m/01h8tj','/m/01yrx','/m/0bt9lr','/m/0bwd_0j','/m/0cd4d','/m/0ch_cf','/m/0cyf8']
df = df[df.LabelName.isin(filter_list)]
for index,row in df.iterrows():
    n = str(row['ImageID'])+'.jpg'
    print(row['ImageID'])
    if row['LabelName'] == "/m/01dws": 
        img = Image.open(n)  # Bear
        img.save('/home/user/gipl/Untitled Folder/Bear/'+str(n))
    elif row['LabelName'] == "/m/01dxs": #Brown bear
        img = Image.open(n) 
        img.save('/home/user/gipl/Untitled Folder/Brown bear/'+str(n))
    elif row['LabelName'] == "/m/012074":  #Magpie
        img = Image.open(n) 
        img.save('/home/user/gipl/Untitled Folder/Magpie/'+str(n))
    else:
        continue 
