# Installation

    $ pip install pyvies

# Usage

From Python:

```python
import pyvies

# Initialize the validator with *your* VAT number

v = pyvies.Vies("DK", 12345678)

# Validate any VAT number in the EU to a dict containing these keys:
#  - "Date when request received"
#  - "Name"
#  - "Consultation Number"
#  - "Member State"
#  - "Address"
#  - "VAT Number" 

try:

    result = v.validate("GB", 12345678)

except pyvies.InvalidVATNumber, e:

    # Catch validation errors
    error = e.args[0]

except pyvies.Unavailable:

    # The database is unavailable
    pass
```

From the console:

    $ vies <requester_country> <requester_vat> <country> <vat>

E.g.:

    $ vies DK 12345678 GB 12345678

You can use the resulting error code to check for validation:

    $ vies DK 12345678 GB 12345678 && echo Valid

# License

LGPL

