{
    "name": "Waaneiza Recruitment",
    "version": "17.0.1.0.0",
    "category": "Human Resources",
    "depends": ["base", "hr", "hr_recruitment", "mail",],
    "data": [
        "security/ir.model.access.csv",
        "views/ir_attachment_views.xml",
        "views/waaneiza_applicant_views.xml",
        "views/waaneiza_applicant_stage.xml",
        "views/waaneiza_refuse_wizard.xml",
        "views/waaneiza_hr_job_views.xml",
        "views/menus.xml",
    ],
    "application": False,
    "installable": True,
}
