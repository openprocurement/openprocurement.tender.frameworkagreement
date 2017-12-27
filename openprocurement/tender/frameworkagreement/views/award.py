# -*- coding: utf-8 -*-
from openprocurement.tender.core.utils import optendersresource
from openprocurement.tender.openeu.views.award import TenderAwardResource as TenderEUAwardResource


@optendersresource(name='frameworkagreement:Tender Awards',
                   collection_path='/tenders/{tender_id}/awards',
                   path='/tenders/{tender_id}/awards/{award_id}',
                   description="Tender Frameworkagreement Awards",
                   procurementMethodType='frameworkagreement')
class TenderFrameworkagreementAwardResource(TenderEUAwardResource):
    """ Tender Frameworkagreement Award Resource """
