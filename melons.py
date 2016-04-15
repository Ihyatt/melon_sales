

class AbstractMelonOrder(object):
    """Parent class"""
    tax = None
    order_type = None

    def __init__(self, species, qty, country_code = None):
        self.species = species
        self.qty = qty
        self.shipped = False

        if country_code:
            self.country_code = country_code
 
    def get_total(self):
        """Calculate price."""

        total = 0
        base_price = 5
        #checks to see if these are Christmas melons or not
        if self.order_type == "international":

            if self.qty < 10:
                if self.species == "Christmas melon":
                    total = (1 + self.tax) * self.qty * (base_price * 1.5) + 3
                else: 
                    total = (1 + self.tax) * self.qty * base_price
            if self.qty > 10:
                if self.species == "Christmas melon":
                    total = (1 + self.tax) * self.qty * (base_price * 1.5)
                else: 
                    total = (1 + self.tax) * self.qty * base_price

        elif self.order_type == "domestic":
            if self.species  == "Christmas melon":
                total = (1 + self.tax) * self.qty * (base_price * 1.5)
            else: 
                total = (1 + self.tax) * self.qty * base_price

        return total


    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order. Subclass"""
    
    order_type = "domestic"
    tax = 0.08
    country_code = "US"


class InternationalMelonOrder(AbstractMelonOrder):
    """ international melon order. Subclass """ 
    
    order_type = "international"
    tax = 0.17
  
    def get_country_code(self):
        """Return the country code."""

        return self.country_code