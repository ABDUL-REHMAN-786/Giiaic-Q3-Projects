from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

Base = declarative_base()

class Item(Base):
    """Base class for all inventory items"""
    __tablename__ = 'items'
    
    item_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    item_type = Column(String(20), nullable=False)
    
    __mapper_args__ = {
        'polymorphic_identity': 'general',
        'polymorphic_on': item_type
    }
    
    def __init__(self, name, quantity, price):
        """Initialize base item attributes with validation"""
        self.name = name
        self.quantity = quantity if quantity >= 0 else 0
        self.price = price if price >= 0 else 0.0
        self.item_type = 'general'
    
    def display_details(self):
        """Display basic item details"""
        return f"ID: {self.item_id}, Name: {self.name}, Quantity: {self.quantity}, Price: ${self.price:.2f}"
    
    def update_quantity(self, new_quantity):
        """Update item quantity with validation"""
        if new_quantity >= 0:
            self.quantity = new_quantity
            return True
        return False
    
    def calculate_total_price(self):
        """Calculate total price (quantity * price)"""
        return self.quantity * self.price
    
    def to_dict(self):
        """Convert item to dictionary for easy display"""
        return {
            'ID': self.item_id,
            'Name': self.name,
            'Quantity': self.quantity,
            'Price': f"${self.price:.2f}",
            'Type': self.item_type.capitalize()
        }

class PerishableItem(Item):
    """Subclass for perishable items with expiry date"""
    __tablename__ = 'perishable_items'
    
    item_id = Column(Integer, ForeignKey('items.item_id'), primary_key=True)
    expiry_date = Column(Date)
    
    __mapper_args__ = {
        'polymorphic_identity': 'perishable',
    }
    
    def __init__(self, name, quantity, price, expiry_date):
        """Initialize perishable item with expiry date"""
        super().__init__(name, quantity, price)
        self.item_type = 'perishable'
        self.expiry_date = expiry_date
    
    def display_details(self):
        """Override to include expiry date"""
        base_info = super().display_details()
        return f"{base_info}, Expiry Date: {self.expiry_date.strftime('%Y-%m-%d')}"
    
    def to_dict(self):
        """Include expiry date in dictionary"""
        base_dict = super().to_dict()
        base_dict['Expiry Date'] = self.expiry_date.strftime('%Y-%m-%d')
        return base_dict

class ElectronicItem(Item):
    """Subclass for electronic items with warranty"""
    __tablename__ = 'electronic_items'
    
    item_id = Column(Integer, ForeignKey('items.item_id'), primary_key=True)
    warranty_years = Column(Integer)
    
    __mapper_args__ = {
        'polymorphic_identity': 'electronic',
    }
    
    def __init__(self, name, quantity, price, warranty_years):
        """Initialize electronic item with warranty"""
        super().__init__(name, quantity, price)
        self.item_type = 'electronic'
        self.warranty_years = warranty_years if warranty_years >= 0 else 0
    
    def display_details(self):
        """Override to include warranty"""
        base_info = super().display_details()
        return f"{base_info}, Warranty: {self.warranty_years} years"
    
    def to_dict(self):
        """Include warranty in dictionary"""
        base_dict = super().to_dict()
        base_dict['Warranty'] = f"{self.warranty_years} years"
        return base_dict

# Database setup
engine = create_engine('sqlite:///inventory.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)