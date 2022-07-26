from django.db import models


class Category(models.Model):
    """ Our Model for Categories """
    class Meta:
        """ Our Model for Categories """
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """ Our Model for Category function to get friend name """
        return self.friendly_name


class Collection(models.Model):
    """ Our Model for Collection """
    class Meta:
        """ Our Model for Collection """
        verbose_name_plural = 'Collection'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """ Our Model for Collection function to get friendly name """
        return self.friendly_name


class Extra_Img(models.Model):
    """ Our Model for Extra images """
    img = models.ImageField(default=False, null=False, blank=False)
    extra_img = models.ForeignKey('Product', null=True, blank=True,
                                  on_delete=models.CASCADE)

    def __str__(self):
        return self.img.url
        


class Product(models.Model):
    """ Our Model for our Products """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    collection = models.ForeignKey('Collection', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(default="no-image-icon-23499.png",
                              null=True, blank=True)

    def __str__(self):
        return self.name
