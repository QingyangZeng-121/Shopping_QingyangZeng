from django.db import models
from django.utils.timezone import now
from user.models import User


# Create your models here.
class ProductBrand(models.Model):
    name = models.CharField(max_length=40, null=False, verbose_name="type name")
    create_time = models.DateTimeField(null=False, default=now, verbose_name="create time")
    update_time = models.DateTimeField(null=False, default=now, verbose_name="update time")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product brand'
        verbose_name_plural = 'product brand'


class Product(models.Model):
    title = models.CharField(max_length=100, null=False, verbose_name="title")
    product_brand = models.ForeignKey(ProductBrand, related_name="product_brand", on_delete=models.CASCADE,
                                      verbose_name="product_brand")
    describe = models.TextField(null=False, verbose_name="describe")
    inventory = models.IntegerField(null=False, verbose_name="inventory", default=0)
    price = models.IntegerField(null=False, verbose_name="inventory", default=0)
    image = models.FileField(upload_to='good_image', verbose_name="image")
    Gender = models.CharField(max_length=100, null=False, verbose_name="Gender",default='')
    Description = models.TextField(null=False, verbose_name="Description",default='')
    PrimaryColor = models.CharField(max_length=100, null=False, verbose_name="PrimaryColor",default='')
    create_time = models.DateTimeField(null=False, default=now, verbose_name="create time")
    update_time = models.DateTimeField(null=False, default=now, verbose_name="update time")

    def __str__(self):
        return self.title

        # 修改显示的表的名字

    class Meta:
        # 给模型类起一个更可读的名字
        verbose_name = 'product'
        # 模型的复数形式
        verbose_name_plural = 'product'


class Order(models.Model):
    order_num = models.CharField(max_length=100, null=False, verbose_name="order_num")
    title = models.CharField(max_length=100, null=False, verbose_name="title")
    number = models.IntegerField(null=False, verbose_name="number", default=0)
    image = models.FileField(upload_to='good_image', verbose_name="image")
    total_price = models.IntegerField(null=False, verbose_name="total_price", default=0)
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE,
                             verbose_name="user")
    status = models.CharField(max_length=100, null=False, verbose_name="status")
    create_time = models.DateTimeField(null=False, default=now, verbose_name="create time")
    update_time = models.DateTimeField(null=False, default=now, verbose_name="update time")

    def __str__(self):
        return self.title

        # 修改显示的表的名字

    class Meta:
        # 给模型类起一个更可读的名字
        verbose_name = 'order'
        # 模型的复数形式
        verbose_name_plural = 'order'
