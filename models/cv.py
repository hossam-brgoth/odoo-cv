# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class Cv(models.Model):

    """
        TABLE INFO
    """
    _name            = 'cv.paper'
    _description     = 'The CV paper'
    _sql_constraints = [('cv_name_unique', 'unique(name)',
                        'Name exist, choose another')]

    """     
        DATA FIELDS
    """

    # A method that calculate age based onchange birth_date
    @api.onchange('birth_date')
    def _compute_age(self):
        for rec in self:
            if rec.birth_date:
                optimized_birth_date = datetime.strptime(str(rec.birth_date), "%Y-%m-%d").date()
                current_day = fields.Date.today()
                rec.age = fields.relativedelta(current_day, optimized_birth_date).years

    # Basic info
    name            = fields.Char("Name", required=True)
    user_id         = fields.Many2one('res.users', string='Added by', default=lambda self: self.env.user)
    last_title      = fields.Char("Last Title")
    nationality     = fields.Many2one('res.country')
    birth_place     = fields.Char("Birth Place")
    birth_date      = fields.Date("Birth Date")
    last_cv_update  = fields.Date("Last CV Update")
    age             = fields.Integer("Age", compute='_compute_age', store=True)

# Contact details
    mobile_no       = fields.Char("Mobile Number", required=True)
    email           = fields.Text("Email")
    fb_account      = fields.Char("Facebook URL account")

# Education
    high_school     = fields.Text("High School education")
    bs_degree       = fields.Text("B.S. degree education")
    master_degree   = fields.Text("M.S. degree education")

# Experience & language
    your_experience = fields.Text("Your Experience")
    native_lang     = fields.Char("Native language")
    secondary_lang  = fields.Char("Secondary language")
    certifications  = fields.One2many('ir.attachment', 'cv_id', 'Certifications')

# Personal info
    image           = fields.Binary("Image")
    gender          = fields.Selection([("0", "Male"), ("1", "Female")], "Gender", default='0')
    social_state    = fields.Selection([("0", "Single"), ("1", "Married")], "Social state", default='0')
    do_you_have_diseases = fields.Boolean("Do you have diseases?")
    date_created    = fields.Datetime('Create Date and Time', default=lambda self: fields.Datetime.now())

    reviewers = fields.Many2many('res.partner', string='CV Reviewers')

    state = fields.Selection([
        ('concept', 'Concept'),
        ('started', 'Started'),
        ('progress', 'In progress'),
        ('finished', 'Done'),
    ], default='concept')

    interviews_count = fields.One2many('calendar.event', 'cv_id', 'Interviews counts' """,
        compute='_compute_interviews_count' """)

    """     
        METHODS
    """
# A method that set 'diseases checkbox' as True
    @api.multi
    def mark_diseases(self):
        for field in self:
            field.do_you_have_diseases = True
        return True

    @api.one
    def concept_progressbar(self):
        self.write({
            'state': 'concept',
        })

    # This function is triggered when the user clicks on the button 'Set to started'
    @api.one
    def started_progressbar(self):
        self.write({
            'state': 'started'
        })

    # This function is triggered when the user clicks on the button 'In progress'
    @api.one
    def progress_progressbar(self):
        self.write({
            'state': 'progress'
        })

    # This function is triggered when the user clicks on the button 'Done'
    @api.one
    def done_progressbar(self):
        self.write({
            'state': 'finished',
        })
