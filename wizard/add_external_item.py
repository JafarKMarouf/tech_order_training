from odoo import _, api, fields, models, tools # type: ignore

import logging
_logger = logging.getLogger(__name__)

class AddExternalItem(models.TransientModel):
    _name = 'wizard.external.item'
    _description = 'External Items Wizard'
    
    
    external_item_ids = fields.Many2many(
        string='External Item',
        comodel_name='external.item',
    )
    
    def action_add_item(self):
        pass