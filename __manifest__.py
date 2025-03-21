# -*- coding: utf-8 -*-
{
    'name': "ITS stock delivery confirmation",

    'summary': """ This module facilitates stock inventory.
        """,

    'description': """
         Allow to know whether the warehouse worker has actually delivered the physical goods to the 
            customer.
    """,

    'author': "ITS, Lari Feuzeu ",
    'website': "http://www.its-nh.com",
    'category': 'Stock Management',
    'version': '11.1.0.1',

    # odoo dependencies
    'depends': ['base', 'branch', 'account', 'stock'],

    # Settings data files
    'data': [
        'views/stock_pincking.xml',
        'views/sale_oder.xml',
        'views/account_move.xml',
        'security/security.xml',

    ],
}
