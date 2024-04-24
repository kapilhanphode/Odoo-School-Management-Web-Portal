from odoo.addons.portal.controllers.portal import CustomerPortal, pager
from odoo.http import request
from odoo import http, _
from odoo.tools import groupby as groupbyelem
from operator import itemgetter
from odoo.exceptions import ValidationError


class StudentRegisterWebPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        res = super(StudentRegisterWebPortal, self)._prepare_home_portal_values(counters)
        res['student_registered_count'] = request.env['student.registration'].search_count([])
        # print(res)
        return res

    @http.route('/studentlist/', auth='public', website=True)
    def StudentListView(self, sortby='id', **kw):
        searchbar_sortings = {
            'id': {'label': _('ID Asc'), 'order': 'id asc'},
            'id1': {'label': _('ID Desc'), 'order': 'id desc'},
        }
        if not sortby:
            sortby = 'id'
        order = searchbar_sortings[sortby]['order']

        student_registration = http.request.env['student.registration'].search([], order=order)
        return http.request.render('school_management_web_portal.portal_student_registration_list_view', {
            'student_registration1': student_registration,
            'page_name': 'student_registration_list_view',
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby
        })

    @http.route("/studentlist/<model('student.registration'):student>/", auth='public', website=True)
    def StudentFormView(self, student):
        print('++++++++++++++++++appointment', student.id)
        return http.request.render('school_management_web_portal.student_form_view_portal', {
            'student1': student,
            'page_name': 'student_registration_list_view'
        })

    @http.route('/studform', type='http', methods=['POST', 'GET'], auth='user', website=True, csrf=False)
    def studentregistrationform(self, **kwargs):
        print('Student Registration Form View-----------------------')
        return request.render('school_management_web_portal.student_registration_form')

    @http.route('/studfromsubmit', type='http', methods=['POST', 'GET'], auth='user', website=True, csrf=False)
    def studentregistrationformsubmit(self, **kwargs):
        print('Student Registration Form-----------------------')
        print('admission_type-----------------------', kwargs.get('remediation_type'))
        print('kwargs', kwargs)
        student_age = kwargs.get('student_age')

        admission_type = kwargs.get('remediation_type')

        clg_stream = None
        stud_class = None
        teaching_jr_class = None
        graduation_clg_stream = None
        post_graduation_clg_stream = None

        if admission_type == 'school':
            stud_class = kwargs.get('options')
            print('stud_class',stud_class)
        elif clg_stream == 'option':
            clg_stream = kwargs.get('options')
            print('clg_stream',clg_stream)
        elif admission_type == 'jr_college':
            teaching_jr_class = kwargs.get('options')
            print('teaching_jr_class',teaching_jr_class)
        elif admission_type == 'graduation':
            graduation_clg_stream = kwargs.get('options')
            print('graduation_clg_stream',graduation_clg_stream)
        elif admission_type == 'post_graduation':
            post_graduation_clg_stream = kwargs.get('options')
            print('post_graduation_clg_stream',post_graduation_clg_stream)
        else:
            student_class = None

        vals = {
            'student_name': kwargs.get('student_name'),
            'student_phone_no': kwargs.get('student_phone'),
            'student_email': kwargs.get('student_email'),
            'student_gender': kwargs.get('student_gender'),
            'marital_status': kwargs.get('student_mart_status'),
            'student_age': kwargs.get('student_age'),
            'student_address': kwargs.get('student_address'),
            'student_admission_type': admission_type,
            'stud_class': stud_class,
            'clg_stream': clg_stream,
            'teaching_jr_class': teaching_jr_class,
            'graduation_clg_stream': graduation_clg_stream,
            'post_graduation_clg_stream': post_graduation_clg_stream,
        }
        stud_regs = request.env['student.registration'].sudo().create(vals)
        stud_gender = request.env['student.registration'].search([])
        print(stud_gender)
        return request.render('school_management_web_portal.student_registration_form',
                              {stud_regs: 'student_registration'})

    # @http.route('/create/student', type='http', methods=['POST', 'GET'], auth='user', website=True)
    # def studentcreated(self, **kwargs):
    #     print('kwargs', kwargs)
    #     # val = {
    #     #     'student_name':kwargs.get('stud_name')
    #     # }
    #     request.env['student.registration'].create(kwargs)
    #     return request.render('school_management_web_portal.patient_registration')

    # ---------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------

    class PartnerForm(http.Controller):
        # mention class name
        @http.route(['/student/form'], type='http', auth="public", website=True)
        # mention a url for redirection.
        # define the type of controller which in this case is ‘http’.
        # mention the authentication to be either public or user.
        def student_form(self, **post):
            # create method
            # this will load the form webpage
            return request.render("school_management_web_portal.student_form", {})

        @http.route(['/student/form/submit'], type='http', auth="public", website=True)
        # next controller with url for submitting data from the form#
        def customer_form_submit(self, **post):
            vals = request.env['student.registration'].sudo().create({
                'student_name': post.get('student_name'),
                'student_phone_no': post.get('student_phone_no'),
                'student_email': post.get('student_email')
            })
            vals = {
                'vals': vals,
            }
            # inherited the model to pass the values to the model from the form#
            return request.render("school_management_web_portal.student_form_success", vals)
            # finally send a request to render the thank you page#
