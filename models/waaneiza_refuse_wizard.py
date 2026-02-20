from odoo import api, fields, models, _
from odoo.exceptions import UserError


class WaaneizaApplicantRefuseWizard(models.TransientModel):
    _name = "waaneiza.applicant.refuse.wizard"
    _description = "Applicant Refuse Wizard"

    applicant_id = fields.Many2one(
        "waaneiza.applicant",
        string="Applicant",
        required=True,
        readonly=True,
    )

    refuse_reason_id = fields.Many2one(
        "hr.applicant.refuse.reason",
        string="Refuse Reason",
        required=True,
    )


    notes = fields.Text(string="Notes")

    def action_confirm_refuse(self):
        self.ensure_one()
        applicant = self.applicant_id

        if not applicant.previous_stage_id:
            applicant.previous_stage_id = applicant.stage_id.id

        applicant.write({
            "refuse_reason_id": self.refuse_reason_id.id,
            "active": False,
        })
        return {"type": "ir.actions.act_window_close"}



