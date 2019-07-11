# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Attachment(models.Model):
    _inherit = 'ir.attachment'
    cv_id = fields.Many2one('cv.paper', 'Cer')
