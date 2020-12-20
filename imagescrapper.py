import os
import requests
from bs4 import BeautifulSoup
import shutil
class ImageScrapper():
    def __init__(self,searchString):
        self.SearchString=searchString
        self.URLString=None
        self.FilePath=self.FilePath=os.path.join(os.getcwd(),'static\\downloads')
        self.lis_img=[]
        self.set_URL()
        

    def set_URL(self):
        self.URLString= 'https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X'.format(self.SearchString)

    def set_FilePath(self):
        self.FilePath=os.path.join(os.getcwd(),'static\\downloads\\')
    
    def get_Raw_HTML(self):
        header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
        }
        try:
            print("Hitting :"+self.URLString)
            data=requests.get(self.URLString,headers=header)
            html_data=BeautifulSoup(data.content,'html.parser')
        except Exception as e:
            print("Error while Getting Raw HTML "+str(e))
            return None
        return html_data
    
    def extract_URL(self,html_data):
        # html_data=self.get_Raw_HTML()
        img_url=[]
        try:
            for img in html_data.find_all('img',{'class':'rg_i Q4LuWd'}):
                try:
                    if 'data-src' in img.attrs:
                        img_url.append(img['data-src'])
                        print("$$$$$$$${}$$$$$$$".format(img['data-src']))
                except Exception as e:
                    print("Error while Getting the Data Source "+str(e))
                    continue
        except Exception as e:
            print("Error while Extracting URL "+str(e))
        return img_url
            
    def clear_Previous(self):
        try:
            if os.path.exists(self.FilePath):
                shutil.rmtree(self.FilePath)
                print("##########DELETED PREVIOUS FILES#########")
            # self.set_FilePath()
        except Exception as e:
            print("Error while deleting the Previous Directory "+str(e))
    
    def prepare_Folder(self):
        try:
            if not os.path.exists(self.FilePath):
                os.mkdir(self.FilePath)
        except Exception as e:
            print("Error while Preparing Folder "+str(e))

    def download_Image(self,url):
        header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
        }
        print("Hitting :"+url)
        data=requests.get(url,headers=header)
        return data.content
    
    
    def save_Image(self,ImageContent,count):
        self.set_FilePath()
        try:
            with open(self.FilePath+str(count)+".jpg","wb") as f:
                f.write(ImageContent)
                self.lis_img.append('{}.jpg'.format(count))
                print("Saving Image in {}".format(self.FilePath))
        except Exception as e:
            print("Error while Saving Image Number {} ".format(count)+str(e))
    

    def list_added_images(self):
        return self.lis_img
    
    
    
