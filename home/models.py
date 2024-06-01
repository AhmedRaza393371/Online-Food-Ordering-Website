from django.db import models

# Table1 model
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    address = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    password = models.CharField(max_length=255,db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Customer'


# Producttable1 model
class Producttable1(models.Model):
    productid = models.AutoField(db_column='productID', primary_key=True)  # Field name made lowercase.
    productname = models.CharField(db_column='productName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    prdouctprice = models.IntegerField(db_column='prdouctPrice', blank=True, null=True)  # Field name made lowercase.
    productdesc = models.CharField(db_column='ProductDesc', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    image_path = models.CharField(max_length=255)  # Add the image_path field

    class Meta:
        managed = False
        db_table = 'ProductTable1'


# Orderdetails model without primary key
class Orderdetails(models.Model):
    order = models.ForeignKey('Ordertable', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('Producttable1', models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OrderDetails'
        unique_together = (('order', 'product'),)

    def __str__(self):
        return f"{self.order} - {self.product}"


# Ordertable model
class Ordertable(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Customer', models.DO_NOTHING, blank=True, null=True, db_column='cust_id')  # Update the db_column
    order_date = models.DateField(blank=True, null=True)  # Changed to DateField
    totalprice = models.IntegerField(db_column='totalPrice', blank=True, null=True)  # Field name made lowercase.    

    class Meta:
        managed = False
        db_table = 'OrderTable'


# Cart model
class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Producttable1)


# CartItem model
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Producttable1, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
