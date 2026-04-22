# -*- coding: utf-8 -*-
from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    # Keep compatibility with hr SELF_READABLE/WRITEABLE field list.
    notes = fields.Text(
        related="employee_id.notes",
        readonly=False,
        related_sudo=False,
    )
