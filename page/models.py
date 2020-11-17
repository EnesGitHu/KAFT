from django.db import models
DEFAULT_STATUS = "draft"
STATUS = [
    #sol kısım database e kayıt sol kısım bize gözüken
    ("draft", "Taslak"),
    ("published", "Yayinlandi"),
    ("deleted", "Silindi"),

]

class Page(models.Model):
    #title: Hakkımızda/İletişim 
    #slug : sadece create sırasında oluşmalıdır
    #content
    #cover_image
    #created_add
    #update_add
    #status

    title = models.CharField(max_length = 200)
    content = models.TextField()
    slug = models.SlugField(max_length = 200, default = "")
    
    
    cover_image = models.ImageField(
        upload_to = "page",
        null = True,
        blank=True,
        
    )
    status = models.CharField(
        default = DEFAULT_STATUS,
        choices = STATUS,
        max_length = 10,
    )
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField (auto_now_add=True)


class Carousel(models.Model):
    title = models.CharField(max_length=200,blank=True, null=True)

    cover_image = models.ImageField(
        upload_to="carousel",
        blank=True, 
        null=True,
    )
    status = models.CharField(
        default = DEFAULT_STATUS,
        choices = STATUS,
        max_length = 10,
    )
   


    created_at = models.DateTimeField(auto_now_add=True)
    update_at =  models.DateTimeField(auto_now=True)
    

    

