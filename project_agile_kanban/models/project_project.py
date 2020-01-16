# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

from odoo import models, fields, api


class Project(models.Model):
    _inherit = "project.project"

    agile_method = fields.Selection(
        selection_add=[("kanban", "Kanban")], default="kanban",
    )

    @api.multi
    def agile_kanban_enabled(self):
        self.ensure_one()
        return self.agile_enabled and self.agile_method == "kanban"

    def get_analytic_types(self):
        types = super(Project, self).get_analytic_types()
        types.append("kanban")
        return types
