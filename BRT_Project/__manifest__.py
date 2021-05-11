{
    'name': 'Background_Remove_Tool',
    'version': '1.0',
    'category': 'Extra Tools',
    'sequence': 5,
    'summary': 'Background Remove Tool Demo',
    'depends': ['base'],

    'description': """
            module for background remove tool
            """,

    'data' : [
        'security/ir.model.access.csv',
        'data/data.xml',
        'controller/brt_template.xml',
        'controller/assets.xml',

    ],

    'application' : True

}