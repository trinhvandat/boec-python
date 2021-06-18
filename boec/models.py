from django.db import models

# Create your models here.
# Create model user
class FullName(models.Model):
    firstName = models.CharField(max_length=256)
    midName = models.CharField(max_length=256)
    lastName = models.CharField(max_length=256)

class Address(models.Model):
    numberHouse = models.CharField(max_length=256)
    street = models.CharField(max_length=256)
    district = models.CharField(max_length=256)
    city = models.CharField(max_length=256)

class Account(models.Model):
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)

class Customer(models.Model):
    email = models.CharField(max_length=256)
    phoneNumber = models.CharField(max_length=11)
    fullName = models.ForeignKey(FullName, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __getName__(self):
        return self.fullName.firstName + " " + self.fullName.midName + " " + self.fullName.lastName

#Create model product
class Product(models.Model):
    name = models.CharField(max_length=256)
    priceEntry = models.IntegerField()
    dateEntry = models.DateField(null=True)
    publicationDate = models.DateField(null=True)
    barcode = models.CharField(max_length=256, null=True)
    producer = models.CharField(max_length=256, null=True)

class Book(Product):
    author = models.CharField(max_length=256, null=True)
    status = models.CharField(max_length=256)
    type = models.CharField(max_length=256)

class Clothes(Product):
    band = models.CharField(max_length=256, null=True)
    size = models.CharField(max_length=256)

class Electronic(Product):
    specification = models.CharField(max_length=256)
    warrantyPeriodDate = models.IntegerField(null=True)
    origin = models.CharField(max_length=256, null=True)

class Item(models.Model):
    name = models.CharField(max_length=256)
    discount = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    title = models.CharField(max_length=256, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

#Create model cart
class Cart(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)

#Create order
class Order(models.Model):
    createDate = models.DateField(null=True)
    total = models.FloatField(null=True)
    code = models.CharField(max_length=256, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    status = models.CharField(max_length=256)  #CREATED, APPROVED, CANCELED

#Create shipment
class Shipment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    fee = models.FloatField(null=True)
    type = models.CharField(max_length=256, null=True)
    status = models.CharField(max_length=256, null=True)
    receiveDate = models.DateField(null=True)

#Create payment:
class Payment(models.Model):
    order = models.ForeignKey(Order ,on_delete=models.CASCADE)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    total = models.FloatField(null=True)
    paymentDate = models.DateField(null=True)

class CreditCard(Payment):
    nameOnCard = models.CharField(max_length=256)
    cardNumber = models.CharField(max_length=256)
    code = models.CharField(max_length=256)

class BankTransfer(Payment):
    bankName = models.CharField(max_length=256)
    accountNumber = models.CharField(max_length=256)

#Create model rating
class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True)
    comment = models.CharField(max_length=512)
    status = models.CharField(max_length=256) #APPROVED, CREATED, REMOVED


# Employee models
class EmpAccount(models.Model):
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)

class EmpAddress(models.Model):
    numberHouse = models.CharField(max_length=256)
    street = models.CharField(max_length=256)
    district = models.CharField(max_length=256)
    city = models.CharField(max_length=256)

class EmpFullName(models.Model):
    firstName = models.CharField(max_length=256)
    midName = models.CharField(max_length=256)
    lastName = models.CharField(max_length=256)

class Employee(models.Model):
    email = models.CharField(max_length=256)
    code = models.CharField(max_length=256)
    salary = models.FloatField(max_length=256)
    position = models.CharField(max_length=256)
    dob = models.DateField(null=True)
    name = models.ForeignKey(EmpFullName, on_delete=models.CASCADE)
    account = models.ForeignKey(EmpAccount, on_delete=models.CASCADE)
    address = models.ForeignKey(EmpAddress, on_delete=models.CASCADE)

class ProcessedOrder(models.Model):
    processDate = models.DateField(null=True)
    status = models.CharField(max_length=256)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
