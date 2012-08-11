# Mockingbird

Mockingbird creates mock data for your models. It keeps your front-end
devs happy, they can work with the output and not need to talk to a database.

It is **not** related to [http://pypi.python.org/pypi/mock/](http://pypi.python.org/pypi/mock/)

If you are setting up your application like this, it can be a very powerful
tool to keep your front end dev marking-it-up&trade; and stylin-it-up&trade;

```python

class SqlContactRepository(object):
    def get_contact(self):
        """
        this method is not done yet, but it would be really great
        for the my front end developers start working and not wait on me.
        I will use the MockContactRepository for the time being
        while I work here. Maybe I will fetch Django Models or some other
        custom work... Who knows! While I figure it out though no need
        to make my front end wait!
        """
        pass

class MockContactRepository(object)
    def get_contact(self):
        return mockingbird.Contact()


class ContactService(object):
    def __init__(self, dao):
        self.dao = dao

    def get_contact(self):
        return self.dao.get_contact()


class MyController(MyControllerBase):
    def some_action(self):
        service = ContactService(MockContacts)
        contacts = service.get_contact()
```

I would even go one step further and not even define the service in the
controller, but define all of the services for your app in say...

[http://github.com/aventurella/pydi](http://github.com/aventurella/pydi)

Then you can control all of your service dependencies from one location,
but I digress. With the flip of some text all of your services could deliver
mock data or real data.

**Mockingbird! Your models, mock data!  Shaaaaaaaaaaa!**

## Setup

First make some models. I'm just going to use plain-ol-python-objects.
You should be able to use any kind of model you like, Django, SQLAlchemy, etc
though those are untested.

Mockingbird uses ```setattr(your_model, "attribute_name", value)```. So anything
that supports that should work.

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
```

Now that we have some models, lets tell Mockingbird about them:

```python

from mockingbird import Mockingbird

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

```

As you can see, we let Mockingbird know the class we would like to register
and the attributes we would like it to set. In the dictionary that is passed
the keys represent the attributes and the values represent the kind of mock data
we would like to have applied.

Now to get one of our models filled up with mock data:

```python

contact = mockingbird.Contact()
book = mockingbird.AddressBook()

print(contact.meta.__dict__)
print(book.contacts)
print(book.contacts[0].meta.__dict__)
```

Ta da! model objects filled to the brim with fake data. Let your front end devs
go nuts while you work on the server logic.

Currently Mockingbird supports the following Mock Data Generators:

- MockBoolean
- MockChoice
- MockDate
- MockEmail
- MockInt
- MockList
- MockObject
- MockPhoneNumber
- MockRealName
- MockText

If you would like to see how their used, go ahead and look at tests/test_generators.py
for now until I can write up the docs on their options. Or browse through ```mockingbird.generators.*```

Here are some additional generators I am thinking about adding:

- MockAddress
- MockCity
- MockHash
- MockPrice
- MockState
- MockUsername
- MockZip
