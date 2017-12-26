# -*- coding: utf-8 -*-
from openprocurement.tender.core.utils import optendersresource
from openprocurement.tender.openeu.views.bid_document import TenderEUBidDocumentResource


@optendersresource(name='frameworkagreement:Tender Bid Documents',
                   collection_path='/tenders/{tender_id}/bids/{bid_id}/documents',
                   path='/tenders/{tender_id}/bids/{bid_id}/documents/{document_id}',
                   procurementMethodType='frameworkagreement',
                   description="Tender Frameworkagreement bidder documents")
class TenderFrameworkagreementBidDocumentResource(TenderEUBidDocumentResource):
    """ Tender Frameworkagreement Bid Document Resource """
