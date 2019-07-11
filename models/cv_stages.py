from odoo import models, fields, api


class CvStages(models.TransientModel):
    _name        = 'cv.stages'
    _description = 'The CV Stages'

    @api.multi
    def started_progressbar(self):
        vals = self.env.context['active_ids']               # Getting IDs for cv.paper
        for cv in vals:                                     # Looping around these IDs
            rec = self.env['cv.paper'].browse(cv)           # View all obj fields
            if rec.state == 'concept':
                rec.state = 'started'

