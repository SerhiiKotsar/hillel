#  Create a class describing any company. For example, Toshiba or Apple
class Company:

    def __init__(self, name, logo, tagline, sphere):
        self.name = name
        self.logo = logo
        self.tagline = tagline
        self.sphere = sphere

    def company_info(self):
        return f'Company name: {self.name}. Logo: {self.logo}. Tagline: {self.tagline}. Sphere: {self.sphere}.'


if __name__ == '__main__':
    my_company = Company(name='Apple', logo='bitten apple', tagline='think different', sphere='electronics')
    print(my_company.company_info())
