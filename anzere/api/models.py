from django.contrib.gis.db import models


# PARKING
class Parking(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    nb_place = models.IntegerField()
    free = models.BooleanField()
    geom = models.MultiPolygonField()
    t_0 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_1 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_2 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_3 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_4 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_5 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_6 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_7 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_8 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_9 = models.DecimalField(max_digits=10, decimal_places=10, )

    class Meta:
        managed = False
        db_table = 'parking'


# GARE
class Gare(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    geom = models.MultiPolygonField()
    t_0 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_1 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_2 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_3 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_4 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_5 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_6 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_7 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_8 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_9 = models.DecimalField(max_digits=10, decimal_places=10, )

    class Meta:
        managed = False
        db_table = 'gare'

    def __str__(self):
        return self.name


# Commerce
class Commerce(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    geom = models.MultiPolygonField()
    nb_place = models.IntegerField()
    type = models.IntegerField()
    t_0 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_1 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_2 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_3 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_4 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_5 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_6 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_7 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_8 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_9 = models.DecimalField(max_digits=10, decimal_places=10, )

    class Meta:
        managed = False
        db_table = 'commerce'

    def __str__(self):
        return self.name


# Passage
class Passage(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    geom = models.MultiPolygonField()

    class Meta:
        managed = False
        db_table = 'passage'

    def __str__(self):
        return self.name


# Pistes
class Piste(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    difficulty = models.IntegerField()
    geom = models.MultiPolygonField()
    t_0 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_1 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_2 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_3 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_4 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_5 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_6 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_7 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_8 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_9 = models.DecimalField(max_digits=10, decimal_places=10, )

    class Meta:
        managed = False
        db_table = 'piste'

    def __str__(self):
        return self.name


# Telecabine
class Telecabine(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    duration = models.IntegerField()
    geom = models.MultiPolygonField()
    t_0 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_1 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_2 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_3 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_4 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_5 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_6 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_7 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_8 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_9 = models.DecimalField(max_digits=10, decimal_places=10, )

    class Meta:
        managed = False
        db_table = 'telecabine'

    def __str__(self):
        return self.name


# Telesiege
class Telesiege(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    duration = models.IntegerField()
    geom = models.MultiPolygonField()
    t_0 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_1 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_2 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_3 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_4 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_5 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_6 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_7 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_8 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_9 = models.DecimalField(max_digits=10, decimal_places=10, )

    class Meta:
        managed = False
        db_table = 'telesiege'

    def __str__(self):
        return self.name


# Teleski
class Teleski(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    duration = models.IntegerField()
    geom = models.MultiPolygonField()
    t_0 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_1 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_2 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_3 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_4 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_5 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_6 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_7 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_8 = models.DecimalField(max_digits=10, decimal_places=10, )
    t_9 = models.DecimalField(max_digits=10, decimal_places=10, )

    class Meta:
        managed = False
        db_table = 'teleski'

    def __str__(self):
        return self.name
