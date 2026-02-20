# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import request

class WaaneizaRecruitmentAPI(http.Controller):

    @http.route('/waaneiza/api/applicant', auth='public', methods=['POST'], csrf=False, type='json')
    def create_applicant(self, **kw):
        data = request.get_json_data() or {}


        name = data.get("name") or "New Application"
        email = data.get("email")
        phone = data.get("phone")
        job_id = data.get("job_id")

        job_name = (data.get("job_name") or "").strip()
        job = False
        if job_name:
            Job = request.env['waaneiza.job'].sudo()
            job = Job.search([('name', '=', job_name)], limit=1)
            if not job:
                job = Job.create({'name': job_name})

        vals = {
            "name": name,
            "partner_name": name,
            "partner_email": email,
            "applicant_phone": phone,
            "job_id": job.id if job else False,
            "description": (data.get("description") or "").strip(),
        }

        
        if job_id:
            vals["job_id"] = int(job_id)

        applicant = request.env["waaneiza.applicant"].sudo().create(vals)
        return {"status": "success", "id": applicant.id}
