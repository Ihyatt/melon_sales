

class AbstractMelonOrder(object):
    """Parent class"""

    def __init__(self, species, qty, country_code = "US"):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code
 

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order. Subclass"""
    
    order_type = "domestic"
    tax = 0.08

    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

class InternationalMelonOrder(AbstractMelonOrder):
    """ international melon order. Subclass """ 
    
    order_type = "international"
    tax = 0.17

    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code