class Vacancy:
    def __init__(self, title, href, company, responsibility, requirements):
        self.title = title
        self.href = href
        self.company = company
        self.responsibility = responsibility
        self.requirements = requirements

    def __str__(self):
        sb = []
        for key in self.__dict__:
            sb.append("{key}='{value}'\n".format(key=key, value=self.__dict__[key]))
        return ''.join(sb)
