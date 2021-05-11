from odoo import  fields, models

class User(models.Model):
    _name = 'user.data'
    _description = "User Details"

    email = fields.Char(string="Email id", copy=False)
    password = fields.Char(string="Password")
    repassword = fields.Char(string="Repassword")
    credit = fields.Integer()
    role =fields.Char(string="Role")

class Admin(models.Model):
	_name = 'admin.data'
	_description = "Admin Details"

	email = fields.Char(string="Email")
	password = fields.Char(string="Password")
	repassword = fields.Char(string="Repassword")
	role = fields.Char(string="Role")

class Credit(models.Model):
    _name = 'credit.credit'
    _description = "Credit Details"

    user_id = fields.Many2one('user.data')
    credit = fields.Integer()

class Order(models.Model):
	_name = 'order.order'
	_description = 'Order Details'

	user_id = fields.Many2one('user.data')