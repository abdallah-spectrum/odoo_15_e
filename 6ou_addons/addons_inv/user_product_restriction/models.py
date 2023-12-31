# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import Warning

class ResUsers(models.Model):
    _inherit = 'res.users'

    user_product_ids = fields.Many2many(
        'product.template',
        'product_user_rel',
        'user_id',
        'product_id',
        'Allowd Products')

    user_category_ids = fields.Many2many(
        'product.category',
        'category_user_rel',
        'user_id',
        'category_id',
        'Allowd Category')

    # user_category_ids = fields.Many2many(
    #     'product.category',
    #     'category_user_rel',
    #     'user_id',
    #     'category_id',
    #     'Allowd Category')