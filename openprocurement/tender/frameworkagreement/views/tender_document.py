# -*- coding: utf-8 -*-
from openprocurement.tender.core.utils import optendersresource
from openprocurement.tender.openeu.views.tender_document import TenderEUDocumentResource


@optendersresource(name='frameworkagreement:Tender Documents',
                   collection_path='/tenders/{tender_id}/documents',
                   path='/tenders/{tender_id}/documents/{document_id}',
                   procurementMethodType='frameworkagreement',
                   description="Tender Frameworkagreement related binary files (PDFs, etc.)")
class TenderFrameworkagreementDocumentResource(TenderEUDocumentResource):
    """ Tender Frameworkagreement Document Resource """
