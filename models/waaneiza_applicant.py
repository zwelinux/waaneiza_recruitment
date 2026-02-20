# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class WaaneizaApplicant(models.Model):
    _name = "waaneiza.applicant"
    _description = "Waaneiza Application"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id desc"
    _rec_name = "partner_name"

    # ======================
    # BASIC INFORMATION
    # ======================
    name = fields.Char(
        string="Subject / Application",
        required=True,
        tracking=True,
    )
    partner_name = fields.Char(
        string="Applicant's Name",
        tracking=True,
    )
    partner_email = fields.Char(string="Email", tracking=True)
    partner_phone = fields.Char(string="Phone", tracking=True)
    partner_nrc_no = fields.Char(string="NRC Number", tracking=True)
    present_address = fields.Char(string="Present Address", tracking=True)
    registered_address = fields.Char(string=" Registered Address", tracking=True)
    father_name = fields.Char(string="Father's Name", tracking=True)
    father_job = fields.Char(string="Father's Job", tracking=True)
    father_phone = fields.Char(string="Father's Phone", tracking=True)
    father_address = fields.Char(string="Father's Address", tracking=True)
    mother_name = fields.Char(string="Mother's Name", tracking=True)
    mother_job = fields.Char(string="Mother's Job", tracking=True)
    mother_phone = fields.Char(string="Mother's Phone", tracking=True)
    mother_address = fields.Char(string="Mother's Address", tracking=True)
    sibling_name = fields.Char(string="Sibling's Name", tracking=True)
    sibling_job = fields.Char(string="Sibling's Job", tracking=True)
    sibling_phone = fields.Char(string="Sibling's Phone", tracking=True)
    sibling_address = fields.Char(string="Sibling's Address", tracking=True)

    # street = fields.Char(tracking=True)
    # street2 = fields.Char(tracking=True)
    # city = fields.Char(tracking=True)
    # state_id = fields.Many2one("res.country.state", tracking=True)
    # zip = fields.Char(tracking=True)
    # country_id = fields.Many2one("res.country", tracking=True)

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], tracking=True)
    place_of_birth = fields.Char('Place of Birth', tracking=True)
    date_of_birth = fields.Date('Date of Birth', tracking=True)
    age = fields.Char(string="Age", tracking=True)
    weight = fields.Char(string="Weight", tracking=True)
    height = fields.Char(string="Height", tracking=True)
    nationality = fields.Char(string="Nationality", tracking=True)
    race = fields.Char(string="Race", tracking=True)
    religion = fields.Char(string="Religion", tracking=True)

    marital = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('cohabitant', 'Legal Cohabitant'),
        ('widower', 'Widower'),
        ('divorced', 'Divorced')
    ], string='Marital Status', default='single', tracking=True)
    spouse_complete_name = fields.Char(string="Spouse Complete Name", tracking=True)
    spouse_birthdate = fields.Date(string="Spouse Birthdate", tracking=True)
    children = fields.Integer(string='Number of Children', tracking=True)

    academic_education = fields.Char("Academic Education", tracking=True)
    professional_education = fields.Char("Professional Education", tracking=True)
    language = fields.Char("Language", tracking=True)
    working_experience = fields.Char("Working Experience", tracking=True)
    career = fields.Char("Career", tracking=True)

    # ======================
    # ABILITY / AVAILABILITY
    # ======================
    available_from = fields.Char(
        string="When can you start work with us if employed?",
        tracking=True
    )
    seriously_ill_or_contagious = fields.Boolean(
        string="Have you ever been seriously ill or contracted with contagious disease?",
        tracking=True
    )
    can_drive_car = fields.Boolean(
        string="Can you drive car?",
        tracking=True
    )
    can_drive_motorcycle = fields.Boolean(
        string="Can you drive motorcycle?",
        tracking=True
    )
    has_driving_licence = fields.Boolean(
        string="Do you hold a valid driving licence?",
        tracking=True
    )
    can_travel = fields.Boolean(
        string="Can you travel?",
        tracking=True
    )
    applied_before = fields.Boolean(
        string="Have you ever applied for employment with us before?",
        tracking=True
    )
    further_information = fields.Text(
        string="Further Information",
    )

    # ======================
    # RECRUITMENT
    # ======================
    user_id = fields.Many2one(
        "res.users",
        string="Recruiter",
        default=lambda self: self.env.user,
    )
    interviewer_ids = fields.Many2many(
        "res.users",
        string="Interviewers",
    )

    priority = fields.Selection(
        [
            ("0", "Normal"),
            ("1", "Good"),
            ("2", "Very Good"),
            ("3", "Excellent"),
        ],
        string="Evaluation",
        default="0",
    )

    # ======================
    # JOB
    # ======================
    job_id = fields.Many2one(
        "waaneiza.job",
        string="Applied Job",
        required=True,
        ondelete="restrict",
    )
    company_id = fields.Many2one(
        "res.company",
        default=lambda self: self.env.company,
    )
    employment_type = fields.Many2one(
        "hr.contract.type",
        string="Employee Type",
        related="job_id.employment_type",
        store=True,
        readonly=True,
    )
    salary_expected = fields.Float("Expected Salary",
                                   help="Salary Expected by Applicant",
                                   tracking=True,
                                   )
    salary_proposed = fields.Float("Proposed Salary",
                                   help="Salary Proposed by the Organisation",
                                   tracking=True,
                                   )

    # English Test
    english_test_passed = fields.Boolean(string="English Test Passed",tracking=True)
    english_test_points = fields.Char(string="English Test Points",tracking=True)
    english_test_rating = fields.Selection(
        [
            ('advance', 'Advance'),
            ('upper_intermediate', 'Upper Intermediate'),
            ('intermediate', 'Intermediate'),
            ('pre_intermediate', 'Pre Intermediate'),
            ('elementary', 'Elementary'),
            ('basic', 'Basic'),

        ],
        default="basic",
        string="English Test Rating",
        tracking=True,
    )

    # CE Test
    ce_test_passed = fields.Boolean(string="CE Test Passed",tracking=True)
    ce_test_points = fields.Char(string="CE Test Points",tracking=True)
    ce_test_rating = fields.Selection(
        [
            ('normal_eq', 'Normal EQ'),
            ('high_eq', 'High EQ'),
            ('low_eq', 'Low EQ'),
        ],
        default="normal_eq",
        string="CE Test Rating",
        tracking=True,
    )

    # ======================
    # STAGE (IMPORTANT PART)
    # ======================
    stage_id = fields.Many2one(
        "waaneiza.applicant.stage",
        store=True,
        string="Stage",
        index=True,
        ondelete="restrict",
        group_expand="_read_group_stage_ids",
        tracking=True,
    )

    is_hired_stage = fields.Boolean(
        related="stage_id.hired_stage",
        store=True,
        string="Is Hired Stage",
    )

    kanban_state = fields.Selection([
        ('normal', 'Grey'),
        ('done', 'Green'),
        ('blocked', 'Red')], string='Kanban State',
        copy=False, default='normal', required=True)

    refuse_reason_id = fields.Many2one('hr.applicant.refuse.reason', string='Refuse Reason', tracking=True)
    active = fields.Boolean(default=True)
    previous_stage_id = fields.Many2one(
        "waaneiza.applicant.stage",
        string="Previous Stage",
        copy=False,
        readonly=True,
    )

    # ======================
    # NOTES
    # ======================
    description = fields.Text(string="Notes")

    # ======================
    # DOCUMENT LINKS (UPLOAD LINKS)
    # ======================

    passport_photo_link = fields.Char(
        string="Passport Size Photo Link",
        tracking=True,
    )

    nrc_front_link = fields.Char(
        string="NRC Photo (Front) Link",
        tracking=True,
    )

    nrc_back_link = fields.Char(
        string="NRC Photo (Back) Link",
        tracking=True,
    )

    degree_photo_link = fields.Char(
        string="Degree Photo Link",
        tracking=True,
    )

    census_front_link = fields.Char(
        string="Census Photo (Front) Link",
        tracking=True,
    )

    census_back_link = fields.Char(
        string="Census Photo (Back) Link",
        tracking=True,
    )

    certificate_links = fields.Text(
        string="Certificate Links (Raw)",
        help="Imported from Google Form. Auto-processed into certificates.",
    )

    certificate_ids = fields.One2many(
        "waaneiza.applicant.certificate",
        "applicant_id",
        string="Certificates",
    )

    driving_license_front_link = fields.Char(
        string="Driving License Photo (Front) Link",
        tracking=True,
    )

    driving_license_back_link = fields.Char(
        string="Driving License Photo (Back) Link",
        tracking=True,
    )

    # ======================
    # METHODS
    # ======================

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        return self.env["waaneiza.applicant.stage"].search([], order=order)

    def action_refuse(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Refuse Reason",
            "res_model": "waaneiza.applicant.refuse.wizard",
            "view_mode": "form",
            "target": "new",
            "context": {
                "default_applicant_id": self.id,
                "active_model": self._name,
                "active_id": self.id,
                "active_ids": self.ids,
            },
        }
    

    def _process_certificate_links(self):
        Certificate = self.env["waaneiza.applicant.certificate"]

        for record in self:
            if not record.certificate_links:
                continue

            existing_links = set(record.certificate_ids.mapped("link"))

            raw_links = record.certificate_links.replace("\n", ",")
            links = [l.strip() for l in raw_links.split(",") if l.strip()]

            for idx, link in enumerate(links, start=1):
                if link in existing_links:
                    continue

                Certificate.create({
                    "applicant_id": record.id,
                    "name": f"Certificate {len(existing_links) + idx}",
                    "link": link,
                })



    @api.model
    def create(self, vals):
        if not vals.get('stage_id'):
            applied_stage = self.env['waaneiza.applicant.stage'].search(
                [('sequence', '=', 1)], limit=1
            )
            if applied_stage:
                vals['stage_id'] = applied_stage.id

        record = super().create(vals)
        record._process_certificate_links()
        return record


    def write(self, vals):
        res = super().write(vals)

        if "certificate_links" in vals:
            self._process_certificate_links()

        return res

    def reset_applicant(self):
        """Restore applicant back to previous stage; fallback to first open stage."""
        Stage = self.env["waaneiza.applicant.stage"]

        # fallback: first non-fold stage by sequence
        fallback_stage = Stage.search([("fold", "=", False)], order="sequence asc, id asc", limit=1)

        for applicant in self:
            stage_to_restore = applicant.previous_stage_id or fallback_stage

            applicant.write({
                "stage_id": stage_to_restore.id if stage_to_restore else False,
                "refuse_reason_id": False,
                "previous_stage_id": False,  # reset saved value after restore
            })

    def toggle_active(self):
        self = self.with_context(just_unarchived=True)
        res = super(WaaneizaApplicant, self).toggle_active()
        active_applicants = self.filtered(lambda a: a.active)
        if active_applicants:
            active_applicants.reset_applicant()
        return res

    # @api.depends('job_id')
    # def _compute_stage(self):
    #     Stage = self.env['waaneiza.applicant.stage']
    #     for applicant in self:
    #         if not applicant.job_id:
    #             applicant.stage_id = False
    #             continue
    #
    #         stage = Stage.search([
    #             '|',
    #             ('job_ids', '=', False),
    #             ('job_ids', 'in', applicant.job_id.id),
    #             ('fold', '=', False),
    #         ], order='sequence asc', limit=1)
    #
    #         applicant.stage_id = stage.id or False

    # @api.model
    # def create(self, vals):
    #     if not vals.get('stage_id'):
    #         applied_stage = self.env['waaneiza.applicant.stage'].search(
    #             [('sequence', '=', 1)], limit=1
    #         )
    #         if applied_stage:
    #             vals['stage_id'] = applied_stage.id
    #     return super().create(vals)

    def action_open_attachments(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'ir.attachment',
            'name': _('Documents'),
            'context': {
                'default_res_model': 'waaneiza.applicant',
                'default_res_id': self.ids[0],
                'show_applicant_name': 1,
            },
            'view_mode': 'tree,form',
            'views': [
                (self.env.ref('waaneiza_recruitment.view_ir_attachment_tree_hr_documentse').id, 'tree'),
                (False, 'form'),
            ],
            'search_view_id': self.env.ref('waaneiza_recruitment.ir_attachment_view_search_inherit_hr_recruitment').ids,
            'domain': [('res_model', '=', 'waaneiza.applicant'), ('res_id', 'in', self.ids), ],
        }

    # ======================
    # CREATE EMPLOYEE
    # ======================

    employee_information_id = fields.Many2one(
        "hr.employee.information",
        string="Employee Information",
        tracking=True,
        copy=False,
    )

    def action_create_employee(self):
        self.ensure_one()

        if self.employee_information_id:
            raise UserError(_("Employee record already created."))

        partner = self._get_or_create_contact()

        # values (Mapping)
        vals = {

            "name": self.partner_name,
            "private_email": self.partner_email,
            "phone": self.partner_phone,
            "place_of_birth": False,
            "gender": self.gender,
            "birthday": self.date_of_birth,
            "identification_id": self.partner_nrc_no,
            "marital": self.marital,
            "children": self.children,
            "address_home_id": partner.id,
            "study_field": self.academic_education,
        }

        # Create employee information record
        emp = self.env["hr.employee.information"].sudo().create(vals)

        # Link back to applicant
        self.employee_information_id = emp.id

        # Open created employee record
        return {
            "type": "ir.actions.act_window",
            "name": _("Employee"),
            "res_model": "hr.employee.information",
            "view_mode": "form",
            "res_id": emp.id,
            "target": "current",
        }

    def _get_or_create_contact(self):
        """Create/Update res.partner and return partner record."""
        self.ensure_one()

        Partner = self.env["res.partner"].sudo()

        email = (self.partner_email or "").strip().lower()
        phone = (self.partner_phone or "").strip()

        domain = []
        if email:
            domain = [("email", "=", email)]
        elif phone:
            domain = [("mobile", "=", phone)]

        partner = Partner.search(domain, limit=1) if domain else Partner.browse()

        vals_partner = {
            "name": self.partner_name,
            "email": self.partner_email or False,
            "mobile": self.partner_phone or False,
            "street": self.present_address or False,
            "function": self.job_id or False,
        }

        if partner:
            partner.write(vals_partner)
        else:
            partner = Partner.create(vals_partner)

        return partner

    is_duplicate_nrc = fields.Boolean(
        compute="_compute_duplicates",
        store=True
    )

    is_duplicate_email = fields.Boolean(
        compute="_compute_duplicates",
        store=True
    )

    @api.depends("partner_nrc_no", "partner_email")
    def _compute_duplicates(self):
        # default
        for rec in self:
            rec.is_duplicate_nrc = False
            rec.is_duplicate_email = False

        # compute for all records in DB (simple approach)
        self.env.cr.execute("""
                            SELECT partner_nrc_no
                            FROM waaneiza_applicant
                            WHERE partner_nrc_no IS NOT NULL
                              AND partner_nrc_no != ''
                            GROUP BY partner_nrc_no
                            HAVING COUNT(*) > 1
                            """)
        dup_nrcs = set(r[0] for r in self.env.cr.fetchall())

        self.env.cr.execute("""
                            SELECT partner_email
                            FROM waaneiza_applicant
                            WHERE partner_email IS NOT NULL
                              AND partner_email != ''
                            GROUP BY partner_email
                            HAVING COUNT(*) > 1
                            """)
        dup_emails = set(r[0] for r in self.env.cr.fetchall())

        for rec in self:
            if rec.partner_nrc_no and rec.partner_nrc_no in dup_nrcs:
                rec.is_duplicate_nrc = True
            if rec.partner_email and rec.partner_email in dup_emails:
                rec.is_duplicate_email = True
