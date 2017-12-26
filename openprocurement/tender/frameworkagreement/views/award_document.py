# -*- coding: utf-8 -*-
from openprocurement.tender.core.utils import optendersresource
from openprocurement.tender.openeu.views.award_document import \
    TenderAwardDocumentResource as TenderEUAwardDocumentResource


@optendersresource(name='frameworkagreement:Tender Award Documents',
                   collection_path='/tenders/{tender_id}/awards/{award_id}/documents',
                   path='/tenders/{tender_id}/awards/{award_id}/documents/{document_id}',
                   procurementMethodType='frameworkagreement',
                   description="Tender Frameworkagreement Award documents")
class TenderFrameworkagreementAwardDocumentResource(TenderEUAwardDocumentResource):
    """ Tender Frameworkagreement Award Document Resource """
