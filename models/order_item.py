from odoo import _, api, fields, models # type: ignore
from datetime import date, datetime, timedelta

class OrderItem(models.Model):

    _name = 'order.item'
    _description = 'Order Item'
    _rec_name = 'meal_id'
    
    meal_id = fields.Many2one('order.meal', string="Meal", copy=False)
    order_id = fields.Many2one('meal.order', string="Order", readonly=True, copy=False)

    price = fields.Float(string = 'Price')
    quantity = fields.Float(string = 'Quantity')
    total_price = fields.Float(string = 'Total Price')
