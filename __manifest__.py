# -*- coding: utf-8 -*-
{
    'name': "tech_order_training",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Jafar Kamal Marouf",
    'website': "https://www.linkedin.com/in/jafar-marouf",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/meal.xml",
        "views/category.xml",
        "wizard/add_external_item.xml",
        "views/order.xml",
        "views/order_tag.xml",
        "views/order_item.xml",
        "views/meal_ingredient.xml",
        "wizard/feedback_reason.xml",
        "views/customer_feedback.xml",
        "views/external_item.xml",
        "data/server_action.xml"
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

