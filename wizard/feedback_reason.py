from odoo import _, api, fields, models, tools # type: ignore

import logging
_logger = logging.getLogger(__name__)

class FeedbackReason(models.TransientModel):
    _name = 'feedback.reason'
    _description = 'Feedback Reason'
    
    reason = fields.Char('Reason')

    def action_add_reason(self):
        _logger.info("Hello world")
