# -*- coding: utf-8 -*-
from odoo import fields, models, _


class WaaneizaJob(models.Model):
    _name = "waaneiza.job"
    _description = "Waaneiza Job Position"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Job Position", required=True)
    department_id = fields.Many2one(
        "hr.department",
        string="Department"
    )
    company_id = fields.Many2one(
        "res.company",
        string="Company",
        default=lambda self: self.env.company
    )

    recruiter_id = fields.Many2one(
        "res.users",
        string="Recruiter"
    )

    no_of_recruitment = fields.Integer(string="Target Employees")
    description = fields.Text(string="Job Description")
    applicant_ids = fields.One2many("waaneiza.applicant", "job_id", string="Applicant IDs")
    document_count = fields.Integer(compute='_compute_document_count', string="Documents", default=0)
    application_count = fields.Integer(compute='_compute_application_count', string="Application Count")
    new_application_count = fields.Integer(
        compute='_compute_new_application_count',
        string="New Application",
        help="Number of applications that are new in the flow (typically at first step of the flow)")


    website_published = fields.Boolean(string="Published", default=False)
    job_page_url = fields.Char(string="Job Page URL")
    employment_type = fields.Many2one("hr.contract.type", string="Employee Type")


    def action_open_applications(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Job Applications",
            "res_model": "waaneiza.applicant",
            "view_mode": "kanban,tree,form",
            "domain": [("job_id", "=", self.id)],
            "context": {
                "default_job_id": self.id,
            },
        }



    def _compute_application_count(self):
        for rec in self:
            rec.application_count = len(rec.applicant_ids)

    def action_open_new_applications(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "New Applications",
            "res_model": "waaneiza.applicant",
            "view_mode": "kanban,tree,form",
            "domain": [
                ("job_id", "=", self.id),
                ("stage_id.sequence", "=", 1),
            ],
            "context": {
                "default_job_id": self.id,
                "search_default_new_stage": 1,
            },
        }

    def _compute_new_application_count(self):
        Applicant = self.env["waaneiza.applicant"]
        for rec in self:
            rec.new_application_count = Applicant.search_count([
                ("job_id", "=", rec.id),
                ("stage_id.sequence", "=", 1),
            ])

    def _compute_document_count(self):
        Attachment = self.env["ir.attachment"].sudo()
        Applicant = self.env["waaneiza.applicant"].sudo()

        for job in self:
            applicant_ids = Applicant.search([("job_id", "=", job.id)]).ids
            if not applicant_ids:
                job.document_count = 0
                continue

            job.document_count = Attachment.search_count([
                ("res_model", "=", "waaneiza.applicant"),
                ("res_id", "in", applicant_ids),
            ])

    def action_open_attachments(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'ir.attachment',
            'name': _('Documents'),
            'context': {
                'default_res_model': self._name,
                'default_res_id': self.ids[0],
                'show_partner_name': 1,
            },
            'view_mode': 'tree',
            'views': [
                (self.env.ref('waaneiza_recruitment.view_ir_attachment_tree_hr_documentse').id, 'tree')
            ],
            'search_view_id': self.env.ref('waaneiza_recruitment.ir_attachment_view_search_inherit_hr_recruitment').ids,
            'domain': ['|',
                       '&', ('res_model', '=', 'waaneiza.job'), ('res_id', 'in', self.ids),
                       '&', ('res_model', '=', 'waaneiza.applicant'), ('res_id', 'in', self.applicant_ids.ids),
                       ],
        }

