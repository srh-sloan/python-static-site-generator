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
        print('rel',rel)
        directory = self.dest / rel
        print (directory)

        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        print('created', self.dest)

        for path in self.source.rglob("*"):
            print(path)
            if path.is_dir():
                self.create_dir(path)
            else:
                print('not a dir')


s = Site('/Users/sarahsloan/dev/LearningWorkspace/python-static-site-generator/content/', '/Users/sarahsloan/dev/LearningWorkspace/site_dest')
s.build()