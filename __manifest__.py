# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'School Management Web Portal',
    'version' : '1.0.0',
    'summary': 'School Management Web Portal Summary',
    'sequence': -97,
    'description': """
School Management By Kapil.
    """,
    'author':'Kapil',
    'category': 'Portal1',
    'website': 'https://www.odoo.com/app/invoicing',
    'images' : [],
    'depends' : ['mail','product','portal','website','web'],
    'data': [
        'views/portal_rfq_views.xml',
    ],
    'assets':{
        'web.assets_frontend':[
            'school_management_web_portal/static/src/js/patient_validation.js',
            'school_management_web_portal/static/**/*',
        ],
    },
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
