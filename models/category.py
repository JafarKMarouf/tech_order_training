from odoo import _, api, fields, models, tools # type: ignore

class Category(models.Model):

    _name = 'order.meal.category'
    _description = 'Order Meal Category'
    _order = 'name'
    
    name = fields.Char(
        string = 'Name', 
        required=True,
        copy = False
    )

