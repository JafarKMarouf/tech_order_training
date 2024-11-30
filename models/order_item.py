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
    total_price = fields.Float(string = 'Total Price', compute = '_compute_total_price')

    @api.onchange('meal_id')
    def set_price(self):
        if self.meal_id:
            self.price = self.meal_id.price

    @api.depends('quantity','price')
    def _compute_total_price(self):
        for record in self:
            record.total_price = record.price * record.quantity

    # @api.onchange('price','quantity')
    # def _compute_total_price(self):
    #     self.total_price = self.price * self.quantity
