
REPOS = (("es","origin","master"),)

def staging():
    "Configures Fabric to access the Staging Server"
    config.fab_hosts = ['core-stage.esw.com']
    config.fab_user = "django"
    config.fab_password = "3sw1nd0ws"
    config.repos = (('es','origin','stage-master'),)

def production():
    "Configures Fabric to access the Production Server"
    config.fab_hosts = ['core.esw.com']
    config.fab_user = "django"
    config.fab_password = "3sw1nd0ws"
    config.repos = (('es','origin','master'),)

def reboot_apache():
    "Reboot Apache2 server."
    require('fab_hosts',provided_by=[staging,production])
    require('fab_user',provided_by=[staging,production])
    sudo("apache2ctl graceful")

def syncdb():
    "Runs Syncdb for the django project"
    require('fab_hosts',provided_by=[staging,production])
    run("cd ~/$(repo)/; python manage.py syncdb")

def migrate():
    "Runs Syncdb for the django project"
    require('fab_hosts',provided_by=[staging,production])
    run("cd ~/$(repo)/; python manage.py migrate")

def git_pull():
    "Updates the repository"
    run("cd ~/$(repo)/; git pull $(parent) $(branch)")
    
def git_reset():
    "Resets the repository to specified version."
    run("cd ~/$(repo)/; git reset --hard $(hash)")

def pull():
    "Pulls from the remote GitRepo"
    require('fab_hosts',provided_by=[staging,production])
    require('repos',provided_by=[staging,production])
    for repo, parent, branch in config.repos:
        config.repo = repo
        config.parent = parent
        config.branch = branch
        invoke(git_pull)

def test():
    local("python manage.py test",fail='abort')

def reset(repo, hash):
    """
    Reset all git repositories to specified hash.
    Usage:
        fab reset:repo=my_repo,hash=etcetc123
    """
    require("fab_hosts",provided_by=[staging,production])
    require('repos',provided_by=[staging,production])
    config.hash = hash
    config.repo = repo
    invoke(git_reset)

def deploy():
    "Deploys the project to the target environment"
    require('fab_hosts',provided_by=[staging,production])
    require('repos',provided_by=[staging,production])
    invoke(pull)
    invoke(syncdb)
    invoke(migrate)
    invoke(reboot_apache)
    
