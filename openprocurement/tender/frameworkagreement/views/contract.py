# -*- coding: utf-8 -*-
from openprocurement.tender.core.utils import optendersresource
from openprocurement.tender.openeu.views.contract import \
    TenderAwardContractResource as TenderEUContractResource


@optendersresource(name='frameworkagreement:Tender Contracts',
                   collection_path='/tenders/{tender_id}/contracts',
                   path='/tenders/{tender_id}/contracts/{contract_id}',
                   procurementMethodType='frameworkagreement',
                   description="Tender Frameworkagreement contracts")
class TenderFrameworkagreementContractResource(TenderEUContractResource):
    """ Tender Frameworkagreement Contract Resource """
