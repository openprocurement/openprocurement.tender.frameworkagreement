# -*- coding: utf-8 -*-
from openprocurement.tender.core.utils import optendersresource
from openprocurement.tender.openeu.views.bid import TenderBidResource as TenderEUBidResource


@optendersresource(name='frameworkagreement:Tender Bids',
                   collection_path='/tenders/{tender_id}/bids',
                   path='/tenders/{tender_id}/bids/{bid_id}',
                   procurementMethodType='frameworkagreement',
                   description="Tender Frameworkagreement bids")
class TenderFrameworkagreementBidResource(TenderEUBidResource):
    """ Tender Frameworkagreement Bid Resource """
