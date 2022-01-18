# -*- coding: utf-8 -*-
{
    'name': "Exploracion",

    'summary': """
        Módulo para exploración espacial""",

    'description': """
        Mostrar las capacidades de Odoo para crear nuevos
        modelos y sus vistas
    """,

    'author': "Indasoge",
    'website': "http://www.indasoge.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Exploracion',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase', 'contacts'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/record_rules.xml',
        'security/ir.model.access.csv',
        'views/exploracion_menu_items.xml',
        'views/naves_views.xml',
        'views/mision_views.xml',
        'views/res_partners_views_inherit.xml',
        'views/product_views_inherit.xml',
        'views/purchase_views_inherit.xml',
        'wizard/purchase_wizard_view.xml',
        'reports/mission_report.xml',
        'reports/mission_report_templates.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
