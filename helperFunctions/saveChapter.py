import zipfile
from io import BytesIO
from django.core.files.base import ContentFile
from comics.models import Chapter, Comic, Page
def save(fileForm, chapterForm, request):
    #if request.FILES['zip'].content_type == 'application/x-zip-compressed' : 
        # isImagesValid = True
        # try:
        #     zip = zipfile.ZipFile(request.FILES['zip'])
  
        #     for name in zip.namelist():
        #         data = zip.read(name)
        #         try:
        #             from PIL import Image
        #             image = Image.open(BytesIO(data))
        #             image.load()
        #             image = Image.open(BytesIO(data))
        #             image.verify()
        #         except (err):
        #             print(err)
        #             isImagesValid =False
        
        # finally:

    if fileForm.is_valid() and chapterForm.is_valid():
        try :
            zip = zipfile.ZipFile(request.FILES['zip'])
            saved_chapter= chapterForm.save()
            counter = 1
            for name in zip.namelist():
                data = zip.read(name)
                from PIL import Image
                tempPage = Page(chapter = saved_chapter, page_number=counter)
                tempPage.image.save(name, ContentFile(BytesIO(data).getvalue()), save =False)
                tempPage.save()
            return saved_chapter
        except:
            return False 
        
         