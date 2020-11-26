from imagescrapper import ImageScrapper

class SKBIS():
    def __init__(self,searchString):
        self.searchString=searchString

    def mainExecution(self):
        IS=ImageScrapper(searchString=self.searchString)
        
        html_data=IS.get_Raw_HTML()

        url_list=IS.extract_URL(html_data=html_data)

        NumImages=21

        IS.clear_Previous()

        IS.prepare_Folder()

        count=1
        for url in url_list:
            if count > NumImages:
                break
            
            img=IS.download_Image(url)
            IS.save_Image(img,count=count)    

            count+=1
        
        return IS.list_added_images()