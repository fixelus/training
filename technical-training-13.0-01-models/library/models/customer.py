#

# -*- coding: utf-8 -*-
from odoo import api, models, fields, _

class Customer(models.Model):
    
    _name = "library.customer"
    
    _description = "customer"
    
    name = fields.Text(required=True, string="Customer Name")
    type = fields.selection()
    
    address = fields.Text()
    phone = fields.Text()
    email = fields.Text(required = True, default = '')
    book_id = fields.Many2one("library.book")
