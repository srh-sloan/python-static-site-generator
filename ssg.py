import typer
from ssg.site import Site

def main(source, dest):
    config = {'source':source, 'dest':dest}
    print('config:',config)
    site = Site(**config).build()


typer.run(main)