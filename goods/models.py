from django.db import models

from users.models import CustomUser


class Category(models.Model):
    """ Категории объявлений """
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название категории', max_length=128, unique=True)
    # slug = models.SlugField(max_length=128, unique=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')

    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class AdvertManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()

    def get_queryset_by_id(self, advert_id):
        return self.get_queryset().get(id=advert_id)


class Advert(models.Model):
    """ Объявления """
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_id')
    # user_id = models.ForeignKey('CustomUser', null=False, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='category_id')
    # category_id = models.ForeignKey('Category', null=False, on_delete=models.CASCADE)
    title = models.CharField("Заголовок", max_length=350)
    description = models.TextField('Описание', null=True)
    image = models.ImageField("Картинка", upload_to='advert_images', blank=True, null=True)
    conditions = models.BooleanField('Состояние', default=0)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)



    objects = AdvertManager()  # Присваиваем кастомный менеджер

    class Meta:
        db_table = 'adverts'
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title
