msg_template = """ Hola {name}, 
Gracias por unirte a {website}. Estamos
feliz de tenerte con nosotros.
"""

def formato_msg(mi_nombre='Jorgito', mi_sitio='comprendi.com'):
    mi_msg = msg_template.format(name=mi_nombre, website=mi_sitio)
    return mi_msg