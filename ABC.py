from app import app
from app import db
from app.models import SModel,ModStat
import click

@app.cli.command("fillthedata")
@click.argument("pathtoall")
def inittestdb(pathtoall):
    from app.fillthedata import fill_db
    fill_db(pathtoall)


@app.shell_context_processor
def make_shell_context():
   return {'db': db, 'SModel': SModel,'ModStat': ModStat }
