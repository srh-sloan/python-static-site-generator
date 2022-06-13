import typer
from ssg.site import Site
import ssg.parsers

def main(source, dest):
    config = {'source':source, 'dest':dest, 'parsers':[ssg.parsers.ResourceParser()]}
    print('config:',config)
    site = Site(**config).build()


typer.run(main)