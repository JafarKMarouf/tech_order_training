from odoo import _, api, fields, models, tools # type: ignore

class MealIngredient(models.Model):
    _name = 'meal.ingredient'
    _description = 'Meal Ingredient Model'
    
    
    name = fields.Char(string = 'Name', required=True)
    quantity = fields.Float(string = 'Quantity', required=True)
    
    product_id = fields.Many2one(
        'product.product',
        string='Product',
    )
    meal_id = fields.Many2one(
        'order.meal',
        string='Meal',
    )