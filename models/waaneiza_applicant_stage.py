from odoo import fields, models

class WaaneizaApplicantStage(models.Model):
    _name = "waaneiza.applicant.stage"
    _description = "Waaneiza Applicant Stage"
    _order = "sequence, id"

    name = fields.Char(string="Stage Name", required=True)
    sequence = fields.Integer(default=0)
    fold = fields.Boolean(string="Folded in Kanban")
    hired_stage = fields.Boolean(string="Hired Stage")
