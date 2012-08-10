x MockDate

x MockPhone

x MockEmail

x MockRealName

x MockText

x MockInt

x MockBoolean

x MockChoice

x MockObject

x MockList

? MockAddress

? MockCity

? MockState

? MockZip

? MockUsername

? MockHash

? MockPrice

Syntax test:

```python
from mockingbird import Mockingbird

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


mockingbird = Mockingbird()
mockingbird.spec(Contact, {"name": MockRealName(),
                          "label": MockString(min=4, max=10),
                          "meta": MockObject(ContactMeta)})

mockingbird.spec(ContactMeta, {"phone": MockPhone(),
                               "email": MockEmail(),
                               "dob": MockDate(),
                               "age": MockInt(min=22, max=44)
                               "is_married": MockBoolean()})

mockingbird.spec(AddressBook, {"contacts": MockList(Contact, min=10, max=20)})

contact = mockingbird.Contact()
book = mockingbird.AddressBook()
```
