{
    'name': 'Sale Extension',
    'version': '1.1.0',
    'summary': 'Add custom field to Sale Order',
    'author': 'Odolution',
    'license': 'LGPL-3',
    'sequence': '-100',
    'description': 'This module adds a custom field to the Sale Order form.',
    'depends': ['sale'],
    'data': [
        'views/sale_order_view.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
}
