from odoo import _, api, fields, models, tools # type: ignore

class FeedbackReason(models.TransientModel):
    _name = 'feedback.reason'
    _description = 'Feedback Reason'
    
    reason = fields.Char('Reason')

    
