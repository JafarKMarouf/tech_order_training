from odoo import _, api, fields, models, tools


class CustomeFeedback(models.Model):
    _name = 'customer.feedback'
    _description = 'Customer Feedback Model'
    _rec_name = 'name'
    
    name = fields.Char('Name')
    meal_id = fields.Many2one(
        'order.meal',
        string='Meal',
    )
    
    customer_id = fields.Many2one(
        'res.partner',
        string='Customer',
    )
    rate = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3')
        ],string = 'Rate',
        default='0'
                            
    )
    comment = fields.Text('Comment')