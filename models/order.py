from odoo import _, fields, models # type: ignore
from datetime import date, datetime, timedelta


class Order(models.Model):

    _name = 'meal.order'
    _description = 'Meal Order Model'
    _order = 'name'

    name = fields.Char(
        string = 'Name', required= True, 
        default= lambda self:_('NEW')
    )
    customer_id = fields.Many2one(
        'res.partner',
        string='Customer',
    )
    order_type = fields.Selection([
            ('internal', 'Internal'),
            ('external', 'External'),        
        ],
        string = 'Type',
        required = True, copy = False,
        default='internal'
    )
    note = fields.Text(string = 'Note')
    order_date = fields.Datetime(
            string='Order Date',
            copy = False,
            default=fields.datetime.now().date(),
            readonly=True
    )
    is_urgent = fields.Boolean(string = 'Is Urgent', copy = False)
    active = fields.Boolean(default=True)
    table_number = fields.Integer(string = 'Table Number')
    total_price = fields.Float(string = 'Total Price', copy=False)
    order_tag_ids = fields.Many2many('order.tag', string = 'Tags')
    
