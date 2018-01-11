# -*- coding: utf-8 -*-
import unittest

from openprocurement.api.tests.base import snitch

from openprocurement.tender.belowthreshold.tests.base import (
    test_organization,
)

from openprocurement.tender.belowthreshold.tests.bid import TenderBidBatchDocumentWithDSResourceTestMixin

from openprocurement.tender.frameworkagreement.tests.base import (
    BaseFrameworkagreementContentWebTest,
    test_features_tender_data,
    test_bids
)
from openprocurement.tender.openeu.tests.bid import (
    TenderBidResourceTestMixin,
    Tender2BidResourceTestMixin,
    TenderBidDocumentResourceTestMixin
)
from openprocurement.tender.openeu.tests.bid_blanks import (
    # TenderBidDocumentWithDSResourceTest
    patch_tender_bidder_document_private_json,
    put_tender_bidder_document_private_json,
    get_tender_bidder_document_ds,
    # TenderBidDocumentResourceTest
    patch_and_put_document_into_invalid_bid,
    create_tender_bidder_document_nopending,
    # TenderBidFeaturesResourceTest
    features_bidder,
    features_bidder_invalid,
    # TenderBidResourceTest
    delete_tender_bidder,
    bids_invalidation_on_tender_change,

    create_tender_bid_with_all_documents,
    create_tender_bid_with_eligibility_document_invalid,
    create_tender_bid_with_financial_document_invalid,
    create_tender_bid_with_qualification_document_invalid,
    create_tender_bid_with_eligibility_document,
    create_tender_bid_with_qualification_document,
    create_tender_bid_with_financial_document,
    create_tender_bid_with_financial_documents,
    create_tender_bid_with_eligibility_documents,
    create_tender_bid_with_qualification_documents,

)



class TenderBidResourceTest(BaseFrameworkagreementContentWebTest, TenderBidResourceTestMixin, Tender2BidResourceTestMixin):
    initial_status = 'active.tendering'
    initial_auth = ('Basic', ('broker', ''))
    test_bids_data = test_bids  # TODO: change attribute identifier
    author_data = test_bids_data[0]['tenderers'][0]

    test_delete_tender_bidder = snitch(delete_tender_bidder)
    test_bids_invalidation_on_tender_change = snitch(bids_invalidation_on_tender_change)


class TenderBidFeaturesResourceTest(BaseFrameworkagreementContentWebTest):
    initial_data = test_features_tender_data
    initial_status = 'active.tendering'
    initial_auth = ('Basic', ('broker', ''))
    test_bids_data = test_bids  # TODO: change attribute identificator

    test_features_bidder = snitch(features_bidder)
    test_features_bidder_invalid = snitch(features_bidder_invalid)


class TenderBidDocumentResourceTest(BaseFrameworkagreementContentWebTest, TenderBidDocumentResourceTestMixin):
    initial_auth = ('Basic', ('broker', ''))
    initial_status = 'active.tendering'
    test_bids_data = test_bids  # TODO: change attribute identificator

    def setUp(self):
        super(TenderBidDocumentResourceTest, self).setUp()
        # Create bid
        response = self.app.post_json('/tenders/{}/bids'.format(
            self.tender_id), {'data': test_bids[0]})
        bid = response.json['data']
        self.bid_id = bid['id']
        self.bid_token = response.json['access']['token']
        # create second bid
        response = self.app.post_json('/tenders/{}/bids'.format(self.tender_id), {'data': test_bids[1]})
        bid2 = response.json['data']
        self.bid2_id = bid2['id']
        self.bid2_token = response.json['access']['token']

    test_patch_and_put_document_into_invalid_bid = snitch(patch_and_put_document_into_invalid_bid)
    test_create_tender_bidder_document_nopending = snitch(create_tender_bidder_document_nopending)


class TenderBidDocumentWithDSResourceTest(TenderBidDocumentResourceTest):
    docservice = True

    test_patch_tender_bidder_document_private_json = snitch(patch_tender_bidder_document_private_json)
    test_put_tender_bidder_document_private_json = snitch(put_tender_bidder_document_private_json)
    test_get_tender_bidder_document_ds = snitch(get_tender_bidder_document_ds)



class TenderBidDocumentWithDSResourceTest(TenderBidDocumentResourceTest):
    docservice = True


class TenderBidBatchDocumentsWithDSResourceTest(BaseFrameworkagreementContentWebTest,
                                                TenderBidBatchDocumentWithDSResourceTestMixin):
    docservice = True
    initial_status = 'active.tendering'


    bid_data_wo_docs = {'tenderers': [test_organization],
                        'value': {'amount': 500},
                        'selfEligible': True,
                        'selfQualified': True,
                        'documents': []
        }

    test_create_tender_bid_with_eligibility_document_invalid = snitch(create_tender_bid_with_eligibility_document_invalid)
    test_create_tender_bid_with_eligibility_document = snitch(create_tender_bid_with_eligibility_document)
    test_create_tender_bid_with_eligibility_documents = snitch(create_tender_bid_with_eligibility_documents)

    test_create_tender_bid_with_qualification_document_invalid = snitch(create_tender_bid_with_qualification_document_invalid)
    test_create_tender_bid_with_qualification_document = snitch(create_tender_bid_with_qualification_document)
    test_create_tender_bid_with_qualification_documents = snitch(create_tender_bid_with_qualification_documents)

    test_create_tender_bid_with_financial_document_invalid = snitch(create_tender_bid_with_financial_document_invalid)
    test_create_tender_bid_with_financial_document = snitch(create_tender_bid_with_financial_document)
    test_create_tender_bid_with_financial_documents = snitch(create_tender_bid_with_financial_documents)

    test_create_tender_bid_with_all_documents = snitch(create_tender_bid_with_all_documents)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TenderBidDocumentResourceTest))
    suite.addTest(unittest.makeSuite(TenderBidDocumentWithDSResourceTest))
    suite.addTest(unittest.makeSuite(TenderBidFeaturesResourceTest))
    suite.addTest(unittest.makeSuite(TenderBidResourceTest))
    suite.addTest(unittest.makeSuite(TenderBidBatchDocumentsWithDSResourceTest))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
