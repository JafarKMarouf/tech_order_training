from odoo import _, api, fields, models, tools # type: ignore

class Meal(models.Model):

    _name = 'order.meal'
    _description = 'Order Meal Model'
    _order = 'name'
    
    name = fields.Char(string = 'Name')
    price = fields.Float(string = 'Price')