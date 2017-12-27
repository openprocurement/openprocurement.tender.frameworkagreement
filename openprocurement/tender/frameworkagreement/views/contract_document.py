# -*- coding: utf-8 -*-
from openprocurement.tender.core.utils import optendersresource
from openprocurement.tender.openeu.views.contract_document import \
    TenderAwardContractDocumentResource as TenderEUContractDocumentResource


@optendersresource(name='frameworkagreement:Tender Contract Documents',
                   collection_path='/tenders/{tender_id}/contracts/{contract_id}/documents',
                   path='/tenders/{tender_id}/contracts/{contract_id}/documents/{document_id}',
                   procurementMethodType='frameworkagreement',
                   description="Tender Frameworkagreement Contract documents")
class TenderFrameworkagreementContractDocumentResource(TenderEUContractDocumentResource):
    """ Tender Frameworkagreement Contract Document Resource """
