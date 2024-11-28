from odoo import _, api, fields, models, tools # type: ignore

class Meal(models.Model):

    _name = 'order.meal'
    _description = 'Order Meal Model'
    _order = 'name'
    
    name = fields.Char(
        string = 'Name', required=True,
        default= lambda self:_('NEW')
    )
    price = fields.Float(string = 'Price', copy=False)
    category_id = fields.Many2one(
        'order.meal.category',
        string='Category',
        ondelete='cascade'
    )