from odoo import _, api, fields, models, tools # type: ignore

import logging
_logger = logging.getLogger(__name__)

class FeedbackReason(models.TransientModel):
    _name = 'feedback.reason'
    _description = 'Feedback Reason'
    
    reason = fields.Char('Reason')

    def action_add_reason(self):
        # feedback = self.env['customer.feedback'].search([('id','=',self.env.context.get('active_id'))])
        feedback = feedback = self.env['customer.feedback'].browse(self.env.context.get('active_id'))
        feedback.update({
            'reason' : self.reason,
            'state' : 'rejected'
        })
        # feedback.reason = self.reason
        # feedback.state = 'rejected'
        # _logger.info('context' + str(self.env.context))