# -*- coding: utf-8 -*-

from odoo import models, fields, api


class account_def_pro_acc_payble(models.Model):
    _inherit='res.partner'
    property_account_payable_id = fields.Many2one(default=lambda self:self._get_default_partner())

    def _get_default_partner(self):
        # Replace 'default_partner_id' with the ID of the partner you want as the default value.
         l=self.env['account.account'].search_read([('code','=','20300701')],limit=1)
         print(l,"____________________ls is here ")


         return l[0]
