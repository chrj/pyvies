#!/usr/bin/env python

import sys

import requests
import lxml.html

VIES_RESPONSE = "http://ec.europa.eu/taxation_customs/vies/vatResponse.html"

class ViesError(Exception): pass
class Unavailable(ViesError): pass
class InvalidVATNumber(ViesError): pass

class Vies(object):

    def __init__(self, my_cc, my_vat):
        self.my_cc = my_cc
        self.my_vat = my_vat

    def validate(self, cc, vat):

        params = {
            "memberStateCode": cc.upper(),
            "number": vat,
            "traderName": "",
            "traderStreet": "",
            "traderPostalCode": "",
            "traderCity": "",
            "requesterMemberStateCode": self.my_cc.upper(),
            "requesterNumber": self.my_vat,
            "action": "check",
            "check": "Verify",
        }

        r = requests.post(VIES_RESPONSE, data=params)

        html_doc = lxml.html.fromstring(r.text)

        if u"Application unavailable" in r.text:
            raise Unavailable()

        info = {}

        errors = html_doc.cssselect("span.invalidStyle")

        if errors:
            for error in errors:
                if error.text:
                    raise InvalidVATNumber(u"".join(error.itertext()))

        for tr in html_doc.cssselect("#vatResponseFormTable tr"):

            tds = list(tr.iterchildren())

            if len(tds) < 2:
                continue

            for td in tds:
                if td.get("class") == "labelStyle":
                    key = td.text.strip()
                if td.text and td.text.strip() and key:
                    info[key] = u"\n".join(t.strip() for t in td.itertext())

        return info

def main():

    if len(sys.argv) != 5:

        sys.stderr.write(
            "usage: %s <requester_country> <requester_vat> <country> <vat>\n"
            % sys.argv[0]
        )

        sys.stderr.write(
            "\nsee: http://ec.europa.eu/taxation_customs/vies/\n"
            "     https://bitbucket.org/chrj/pyvies\n"
        )

        sys.exit(-255)

    vies = Vies(sys.argv[1], sys.argv[2])

    try:
        result = vies.validate(sys.argv[3], sys.argv[4])
    except InvalidVATNumber, e:
        sys.stderr.write(e.args[0] + "\n")
        sys.exit(-1)
    except Unavailable:
        sys.stderr.write("Database unavailable\n")
        sys.exit(-1)

    for key, value in result.items():
        print "%s\n%s\n" % (key, value.encode("utf-8"))

if __name__ == "__main__":
    main()
