from odoo import _, api, fields, models # type: ignore
from datetime import date, datetime, timedelta
from odoo.exceptions import ValidationError # type: ignore

import logging
_logger = logging.getLogger(__name__)

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
            default = fields.datetime.now().date(),
            # readonly=True
    )
    is_urgent = fields.Boolean(string = 'Is Urgent', copy = False)
    active = fields.Boolean(default=True)
    table_number = fields.Integer(string = 'Table Number')
    total_price = fields.Float(string = 'Total Price', copy=False)
    order_tag_ids = fields.Many2many('order.tag', string = 'Tags')
    
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (name)', 'Order name already exists!'),
    ]
    
    # constrains on order date in ORM Level
    @api.constrains('order_date')
    def _check_order_date(self):
        # _logger.error("order date: "+str(self.order_date.date()))
        # _logger.error("today: "+str(datetime.now().date()))
        for record in self:
            if record.order_date.date() < datetime.now().date():
                raise ValidationError('Order Date Must not be in past')
    