from odoo import models, fields, api, _

class Rental(models.Model):
    _name = "library.rental"
    _description = "Book Rental Information"
    
    book_id = fields.Many2one(comodel_name = "library.book")
    customer_id = fields.Many2one(comodel_name = "library.customer")
    
    rental_date = field.Date()
    return_date = field.Date()
    