from odoo import fields, models

class WaaneizaApplicantCertificate(models.Model):
    _name = "waaneiza.applicant.certificate"
    _description = "Applicant Certificate"

    applicant_id = fields.Many2one(
        "waaneiza.applicant",
        string="Applicant",
        ondelete="cascade",
        required=True,
    )

    name = fields.Char(
        string="Certificate Name",
        required=True,
    )

    link = fields.Char(
        string="Certificate Link",
        required=True,
    )