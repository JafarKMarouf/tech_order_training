from odoo import _, api, fields, models, tools # type: ignore

import logging
_logger = logging.getLogger(__name__)

class AddExternalItem(models.TransientModel):
    _name = 'wizard.external.item'
    _description = 'External Items Wizard'
    
    def set_default_item(self):
         
        order_external_items = self.env['meal.order'].browse(self.env.context.get('active_id'))
        external_items = self.env['external.item'].search([])
        items = list(set(external_items.ids) - set(order_external_items.external_item_ids.ids))
        
        # _logger.info('default external item: '+ str(items.ids))
        return items
    
    external_item_ids = fields.Many2many(
        string='External Item',
        comodel_name='external.item',
        default=set_default_item
    )
    
    def action_add_item(self):
        external_item = self.env['meal.order'].browse(self.env.context.get('active_ids'))
        external_item.update({
            'external_item_ids': [(4,item.id) for item in self.external_item_ids] 
        })
        # _logger.info('add external item: '+ str(external_item))
        
        # self.external_item_ids = self.env['external.item'].search[()]