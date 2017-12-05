# -*- coding: utf-8 -*-
import unittest

from openprocurement.api.tests.base import snitch

from openprocurement.tender.frameworkagreement.tests.base import (
    test_tender_data, test_lots, test_bids,
    BaseFrameworkagreementWebTest, BaseFrameworkagreementContentWebTest,
)

from openprocurement.tender.frameworkagreement.tests.tender_blanks import (
    # TenderFrameworkagreementTest
    simple_add_tender,
)


class TenderFrameworkagreementTest(BaseFrameworkagreementWebTest):
    initial_auth = ('Basic', ('broker', ''))
    initial_data = test_tender_data
    test_bids_data = test_bids

    test_simple_add_tender = snitch(simple_add_tender)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TenderFrameworkagreementTest))
    #suite.addTest(unittest.makeSuite(TestTenderEUProcess))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')