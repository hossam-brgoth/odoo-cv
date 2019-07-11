# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Interview(models.Model):
    _inherit = 'calendar.event'

    cv_id = fields.Many2one('cv.paper', 'inter')