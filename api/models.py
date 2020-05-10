from django.db import models

# RESTAURANT MODEL

class Restaurant(models.Model):
    name = models.CharField(max_length=80, unique=True)
    address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# SPECIAL MODEL

class Special(models.Model):
    CATEGORY_CHOICES = (
        ('food', 'food'),
        ('beer', 'beer'),
        ('wine', 'wine'),
        ('liquor', 'liquor'),
    )

    DAY_CHOICES = (
        ('All Days', 'All Days'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )

    # Note: "related_name" is what "each special is to a given restaurant."
    # Usually it is just the lower-cased plural of the model it is within.
    # Note 2: the "to_field='name'" arg makes it so that the Query returns the actual name of the restaurant (b/c the Restaurant's name field is 'name), rather than the restaurant's pk. 
    restaurant = models.ForeignKey(Restaurant, related_name="specials", to_field='name', on_delete=models.CASCADE)

    # What the special is called (ex. "1/2 price burgers")
    title = models.CharField(max_length=80)
    
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='food')

    # The day of the week the special falls on
    day = models.CharField(max_length=10, choices=DAY_CHOICES, default='All Days')

    # auto timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title