class TagCloud:
    def __init__(self):
        self.tags = {}

    def __add__(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1


cloud = TagCloud()
cloud["python"]
cloud.add("python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)


# access private members using underscore
print(cloud.__dict__)