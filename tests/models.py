class Account(object):
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.username = None


class Message(object):
    def __init__(self):
        self.service = None
        self.text = None


class Contact(object):
    def __init__(self):
        self.name = None
        self.label = None
        self.meta = None


class ContactMeta(object):
    def __init__(self):
        self.phone = None
        self.email = None
        self.dob = None,
        self.age = 0
        self.is_married = False


class AddressBook(object):
    def __init__(self):
        self.contacts = []
