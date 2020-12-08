import os 

direcion_archivo = os.path.abspath(__file__)
print(direcion_archivo)

BASE_DIR = os.path.dirname(direcion_archivo)
DIRECION_DEL_PROJECTO = os.path.dirname(BASE_DIR)
print(BASE_DIR, DIRECION_DEL_PROJECTO)

email_txt = os.path.join(BASE_DIR, "templates", "email.txt")

content = ""

with open(email_txt, 'r') as f:
    content = f.read()

print(content.format(name='Jorgito'))