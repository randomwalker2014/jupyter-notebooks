import os
import getpass

def create_dir(subdirname):
    username = os.environ['JUPYTERHUB_USER']
    data_dir = os.path.join("/home",username + '-workspace',subdirname)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir,0o700)
        
port = int(os.environ.get('JUPYTER_NOTEBOOK_PORT', '8080'))

c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = port
c.NotebookApp.open_browser = False
c.NotebookApp.quit_button = False

if os.environ.get('JUPYTERHUB_SERVICE_PREFIX'):
    c.NotebookApp.base_url = os.environ.get('JUPYTERHUB_SERVICE_PREFIX')

password = os.environ.get('JUPYTER_NOTEBOOK_PASSWORD')
if password:
    import notebook.auth
    c.NotebookApp.password = notebook.auth.passwd(password)
    del password
    del os.environ['JUPYTER_NOTEBOOK_PASSWORD']

image_config_file = '/opt/app-root/src/.jupyter/jupyter_notebook_config.py'

if os.path.exists(image_config_file):
    with open(image_config_file) as fp:
        exec(compile(fp.read(), image_config_file, 'exec'), globals())
        
create_dir("my-datasets")
create_dir("my-models")
create_dir("my-notebooks")
create_dir("my-results")

