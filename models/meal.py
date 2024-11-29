from odoo import _, api, fields, models, tools # type: ignore

class Meal(models.Model):

    _name = 'order.meal'
    _description = 'Order Meal Model'
    _order = 'name'
    
    name = fields.Char(
        string = 'Name', required=True,
        default= lambda self:_('NEW')
    )
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (name)', 'Meal name already exists!'),
    ]
    
    price = fields.Float(string = 'Price', copy=False)
    category_id = fields.Many2one(
        'order.meal.category',
        string='Category',
        ondelete='cascade'
    )
    meal_ingredient_ids = fields.One2many('meal.ingredient', 'meal_id', string = "Ingredient")
    
    def view_all_feedbacks(self):
        feedback_ids = self.env['customer.feedback'].search([
            ('meal_id', '=', self.id)
        ])
        return {
            'type' : 'ir.actions.act_window',
            'name' : 'Feedbacks',
            'view_mode' : 'tree',
            'res_model' : 'customer.feedback',
            'target' : 'current',
            'domain' : [('id', 'in', feedback_ids.ids)],
            'context' : {'default_meal_id':self.id}
        }
    
    