class EmailGenerator(object):
    _tlds = None
    _words = None

    @property
    def words(self):
        if not LoremIpsumGenerator._text:
            data = pkg_resources.resource_stream("mockingbird.resources", "ipsum.txt")
            LoremIpsumGenerator._text = []
            
            for line in data:
                LoremIpsumGenerator._text.append(line)

        return LoremIpsumGenerator._text

    @property
    def tlds(self):
        

    def action(self):
        