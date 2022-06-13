from pathlib import Path

class Site:
    def __init__(self, source, dest):
        print('In Site constructor')
        self.source = Path(source)
        self.dest = Path (dest)
        print(self.source,self.dest)

    def create_dir(self, path):
        path = Path(path)
        rel = path.relative_to(self.source)
        directory = Path(self.dest, '/', rel)
        print (directory)

s = Site('/Users/sarahsloan/dev/LearningWorkspace/python-static-site-generator/content/', '/Users/sarahsloan/dev/LearningWorkspace/site_dest')
s.create_dir('/images')