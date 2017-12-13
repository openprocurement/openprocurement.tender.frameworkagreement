# -*- coding: utf-8 -*-
import os
from copy import deepcopy

from openprocurement.tender.openeu.tests.base import (
    BaseTenderWebTest,
    test_features_tender_data as base_eu_test_features_data,
    test_tender_data as base_eu_test_data,
    test_lots as base_eu_lots,
    test_bids as base_eu_bids,
)

test_tender_data = deepcopy(base_eu_test_data)
test_tender_data['procurementMethodType'] = "frameworkagreement"
test_features_tender_data = deepcopy(base_eu_test_features_data)
test_lots = deepcopy(base_eu_lots)
test_bids = deepcopy(base_eu_bids)

class BaseFrameworkagreementWebTest(BaseTenderWebTest):
    relative_to = os.path.dirname(__file__)
    initial_data = None
    initial_status = None
    initial_bids = None
    initial_lots = None
    initial_auth = ('Basic', ('broker', ''))
    docservice = False


class BaseFrameworkagreementContentWebTest(BaseFrameworkagreementWebTest):
    """ Frameworkagreement Content Test """
    initialize_initial_data = True
    initial_data = test_tender_data

    def setUp(self):
        super(BaseFrameworkagreementContentWebTest, self).setUp()
        if self.initial_data and self.initialize_initial_data:
            self.create_tender()