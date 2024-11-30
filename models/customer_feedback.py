from odoo import _, api, fields, models, tools # type: ignore

class CustomeFeedback(models.Model):
    _name = 'customer.feedback'
    _description = 'Customer Feedback Model'
    _rec_name = 'name'
    
    name = fields.Char('Name')
    meal_id = fields.Many2one(
        'order.meal',
        string='Meal',
        readonly=True
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
    )
    state = fields.Selection([
        ('new', 'New'),
        ('approved','Approved'),
        ('rejected','Rejected')
        ],string = 'State',
         default='new'
    )
    
    comment = fields.Text('Comment')
    reason = fields.Char('Reason', readonly=True)
    
    def action_approved(self):
        if self.state == 'new':
            self.state = 'approved'
            
    def action_rejected(self):
        if self.state == 'new':
            self.state = 'rejected'