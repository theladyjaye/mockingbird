class MockingbirdException(RuntimeError):
    """There was an ambiguous exception that occurred."""

class MissingSpec(MockingbirdException, AttributeError, KeyError):
    """Object spec registration was not found"""