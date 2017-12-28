# -*- coding: utf-8 -*-
import unittest

from openprocurement.tender.belowthreshold.tests.document import (
    TenderDocumentResourceTestMixin,
    TenderDocumentWithDSResourceTestMixin
)

from openprocurement.tender.frameworkagreement.tests.base import BaseFrameworkagreementContentWebTest


class TenderDocumentResourceTest(BaseFrameworkagreementContentWebTest, TenderDocumentResourceTestMixin):
    docservice = False
    initial_auth = ('Basic', ('broker', ''))


class TenderDocumentWithDSResourceTest(TenderDocumentResourceTest,
                                       TenderDocumentWithDSResourceTestMixin):
    docservice = True


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TenderDocumentResourceTest))
    suite.addTest(unittest.makeSuite(TenderDocumentWithDSResourceTest))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
