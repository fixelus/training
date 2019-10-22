from odoo from models, fields, api, _

class Author(models.Model):
    _name = "library.author"
    
    name = fields.Text(required = True)
    book_ids = fields.Many2many(comodel_name = "library.book")