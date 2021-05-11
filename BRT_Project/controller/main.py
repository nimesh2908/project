from odoo import http
from odoo.http import request

class Main(http.Controller):

    @http.route('/home', type="http", website=True)
    def home(self, **kwargs):
        return request.render('Background_Remove_Tool.home')

    @http.route('/signup', type="http", website=True)
    def signup(self, **kwargs):
        return request.render('Background_Remove_Tool.signup')

    @http.route('/signin', type="http", website=True)
    def signin(self, **kwargs):
        return request.render('Background_Remove_Tool.signin')

    @http.route('/backgroundRemove', type="http", website=True)
    def background(self, **kwargs):
        return request.render('Background_Remove_Tool.backgroundRemove')

    @http.route('/profile', type="http", website=True)
    def profile(self, **kwargs):
        return request.render('Background_Remove_Tool.profile')

    @http.route('/signupSubmit', type="http", website=True)
    def signupSubmit(self, **kwargs):
        print(kwargs.get("password"))
        request.env['user.data'].create({
            'email': kwargs.get("email"),
            'password': kwargs.get("password"),
            'repassword': kwargs.get("repassword"),
            'credit': 10,
            'role': "Customer",
            })
        return http.local_redirect('/signin')

    @http.route('/signinSubmit', type="http")
    def signinSubmit(self, **kwargs):
        res = request.env['user.data'].search([('email', '=', kwargs.get('email')),('password', '=', kwargs.get('password'))])
        role = request.env['admin.data'].search([('email', '=', kwargs.get('email')),('password', '=', kwargs.get('password'))])
        if len(res) or len(role): 
            if len(res):
                request.session['user_id'] = res.id
                request.session['credit'] = res.credit
                return request.render('Background_Remove_Tool.backgroundRemove')
            else:
                return request.render('Background_Remove_Tool.admin')
        else:
            return http.local_redirect('/signin')

    @http.route('/subcription', type="http", website=True)
    def subcription(self, **kwargs):
        print(request.session['user_id'])
        print(kwargs.get("flexRadioDefault"))
        cre = request.env['user.data'].search([('id', '=', request.session['user_id'])])
        cre.credit = cre.credit + int(kwargs.get("flexRadioDefault"))
        request.session['credit'] = cre.credit

        request.env['credit.credit'].create({
            'user_id': request.session['user_id'],
            'credit': kwargs.get("flexRadioDefault"),
            })
        return http.local_redirect('/profile')

    @http.route('/customerDetails', type="http")
    def customerDetails(self, **kwargs):
        return request.render('Background_Remove_Tool.customerDetails')

    @http.route('/purchaseCredit', type="http")
    def purchaseCredit(self, **kwargs):
        res = request.env['credit.credit'].search([])
        return request.render('Background_Remove_Tool.purchaseCredit',{'result':res})

    @http.route('/usageOfCredit', type="http")
    def usageOfCredit(self, **kwargs):   
        res = request.env['order.order'].search([])
        return request.render('Background_Remove_Tool.usageOfCredit',{'result':res})

    @http.route('/upload', type="http")
    def upload(self, **kwargs):
        request.env['order.order'].create({
            'user_id': request.session['user_id'],
            })
        upl = request.env['user.data'].search([('id', '=', request.session['user_id'])])
        upl.credit = upl.credit - 1
        return http.local_redirect('/backgroundRemove')

    @http.route('/payment', type="http")
    def payment(self, **kwargs):
        pay = request.env['credit.credit'].search([('user_id', '=', request.session['user_id'])])
        return request.render('Background_Remove_Tool.payment',{'result':pay})

    @http.route('/usage', type="http")
    def usage(self, **kwargs):
        usa = request.env['order.order'].search([('user_id', '=', request.session['user_id'])])
        return request.render('Background_Remove_Tool.usage',{'result':usa})

    @http.route('/logout', type="http")
    def logout(self, **kwargs):
        request.session.get('user_id') and request.session.pop('user_id')
        request.session.get('credit') and request.session.pop('credit')
        return request.render('Background_Remove_Tool.home')