# -*- coding: utf-8 -*-
# © 2017 Elico Corp (https://www.elico-corp.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Business Requirement Earned Value",
    "summary": "Follow-up project completion (estimated / consumed)",
    "version": "10.0.1.0.0",
    "category": "Project",
    'website': 'https://github.com/OCA/business-requirement/',
    'support': 'support@elico-corp.com',
    "author": "Elico Corp,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "hr_timesheet",
        "project_issue_sheet",
        "business_requirement_deliverable_project",
    ],
    "data": [
        'data/project_completion_report_data.xml',
        "report/project_completion_report_view.xml",
        "security/ir.model.access.csv",
        'views/br_and_project_inherit_view.xml',
    ],
}
