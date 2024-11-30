from odoo import _, api, fields, models, tools # type: ignore


class ExternalItem(models.Model):
    _name = 'external.item'
    _description = 'Exteranl Item'
    _rec_name = 'product_id'
    
    product_id = fields.Many2one(
        'product.product',
        string='Product',
    )
    color = fields.Integer(string = 'Color')
