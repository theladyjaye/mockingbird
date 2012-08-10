x MockDate

x MockPhone

x MockEmail

x MockRealName

x MockText

x MockInt

x MockBoolean

MockObject

MockList

? MockAddress

? MockCity

? MockState

? MockZip

? MockUsername

? MockHash

? MockPrice

Syntax test:

```python
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


Mockingbird.spec(Contact, {"name": MockRealName(),
                          "label": MockString(min=4, max=10),
                          "meta": MockObject(ContactMeta)})

Mockingbird.spec(ContactMeta, {"phone": MockPhone(),
                               "email": MockEmail(),
                               "dob": MockDate(),
                               "age": MockInt(min=22, max=44)
                               "is_married": MockBoolean()})

Mockingbird.spec(AddressBook, {"contacts": MockList(Contact, min=10, max=20)})

contact = Mockingbird.Contact()
book = Mockingbird.AddressBook()
```
