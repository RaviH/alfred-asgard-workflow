# author Ravi Hasija

url = "{0}/cluster/show/{1}"


class Item:
    def __init__(self, name, base_url):
        self.uid = name
        self.title = name
        self.subTitle = name
        self.arg = name
        self.autoComplete = name
        self.quick_look_url = url.format(base_url, name)

    def __str__(self):
        return "uid: {0}, title: {1}, subTitle: {2}, arg: {3}, autoComplete: {4}".format(self.uid, self.title,
                                                                                         self.subTitle, self.arg,
                                                                                         self.autoComplete)
