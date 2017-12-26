# -*- coding: utf-8 -*-
from openprocurement.tender.core.utils import optendersresource
from openprocurement.tender.openeu.views.lot import TenderEULotResource


@optendersresource(name='frameworkagreement:Tender Lots',
                   collection_path='/tenders/{tender_id}/lots',
                   path='/tenders/{tender_id}/lots/{lot_id}',
                   procurementMethodType='frameworkagreement',
                   description="Tender Frameworkagreement lots")
class TenderFrameworkagreementLotResource(TenderEULotResource):
    """ Tender Frameworkagreement Lot Resource """
