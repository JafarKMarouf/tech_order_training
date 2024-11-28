from odoo import _, fields, models # type: ignore

class Order(models.Model):

    _name = 'order.tag'
    _description = 'Order Tag Model'
    _order = 'name'

    name = fields.Char('Name', required= True)
    color = fields.Integer('Color')