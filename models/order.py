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
    
    order_date = fields.Date(
            string='Order Date',
            copy = False,
            default = fields.datetime.now(),
            # readonly=True
    )

    expected_duration  = fields.Integer(string = 'Expected Duration')
    expected_date = fields.Datetime(string = 'Expected Date', 
                            compute = '_compute_expected_date',
                            inverse='_inverse_expected_duartion',
                            # readonly=True
    )
    
    is_urgent = fields.Boolean(string = 'Is Urgent', 
                            copy = False, 
                            default=True
    )
    active = fields.Boolean(default=True)
    table_number = fields.Integer(string = 'Table Number')
    total_price = fields.Float(
        string = 'Total Price', 
        compute='_compute_total_price' )
    
    order_tag_ids = fields.Many2many('order.tag', string = 'Tags')
    item_ids = fields.One2many('order.item', 'order_id', string="Items")    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('in_process', 'In Process'),
        ('cancel', 'Cancelled'),
        ('delivered', 'Delivered'),
        ], string='State',
        default='draft'
    )
    
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (name)', 'Order name already exists!'),
    ]
    
    # constrains on order date in ORM Level
    @api.constrains('order_date')
    def _check_order_date(self):
        # _logger.error("order date: "+str(self.order_date.date()))
        # _logger.error("today: "+str(datetime.now().date()))
        for record in self:
            if record.order_date < datetime.now().date():
                raise ValidationError('Order Date Must not be in past')
    
    @api.depends('item_ids','item_ids.total_price')
    def _compute_total_price(self):
        for record in self:
            total_price = 0
            for item in record.item_ids:
                total_price = total_price + item.total_price
            record.total_price = total_price
          
    @api.depends('order_date','expected_duration')
    def _compute_expected_date(self):
        for record in self:
            record.expected_date = record.order_date + timedelta(days= record.expected_duration)
    
    def _inverse_expected_duartion(self):
        for rec in self:
            expected = (rec.expected_date.date() - rec.order_date).days
            _logger.info('expected_duration : '+ str(expected))
            rec.expected_duration = expected
      

    def action_confirm(self):
        self.state = 'confirm'
        self.order_date = datetime.now().date()
    
    def action_in_process(self):
        self.state = 'in_process' 
 
    def action_delivered(self):
        self.state = 'delivered' 
 
    def action_cancel(self):
        self.state = 'cancel'
    
    