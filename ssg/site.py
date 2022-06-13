from pathlib import Path

class Site:
    def __init__(self, source, dest, parsers = None):
        print('In Site constructor')
        self.source = Path(source)
        self.dest = Path (dest)
        self.parsers = parsers or []
        print(self.source,self.dest)

    def create_dir(self, path):
        path = Path(path)
        rel = path.relative_to(self.source)
        print('rel',rel)
        directory = self.dest / path.relative_to(self.source)
        print (directory)

        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        print('created', self.dest)

        for path in self.source.rglob("*"):
            print(path)
            if path.is_dir():
                self.create_dir(path)
            elif path.is_file():
                self.run_parser(path)
            else:
                print('This should never print... Uh-Oh!')

    def load_parser(self, extension):
        for parser in self.parsers:
            if parser.valid_extension(extension):
                return parser

    def run_parser(self, path):
        parser = self.load_parser(path.suffix)
        if parser is not None:
            parser.parse(path, self.source, self.dest)
        else:
            print('No parser found for file type', path.suffix)


#s = Site('/Users/sarahsloan/dev/LearningWorkspace/python-static-site-generator/content/', '/Users/sarahsloan/dev/LearningWorkspace/site_dest')
#s.build()