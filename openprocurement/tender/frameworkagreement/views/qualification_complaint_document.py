# -*- coding: utf-8 -*-
from openprocurement.tender.openeu.utils import qualifications_resource
from openprocurement.tender.openeu.views.qualification_complaint_document import \
    TenderEUQualificationComplaintDocumentResource


@qualifications_resource(name='frameworkagreement:Tender Qualification Complaint Documents',
                         collection_path='/tenders/{tender_id}/qualifications/{qualification_id}/complaints/{complaint_id}/documents',
                         path='/tenders/{tender_id}/qualifications/{qualification_id}/complaints/{complaint_id}/documents/{document_id}',
                         procurementMethodType='frameworkagreement',
                         description="Tender Frameworkagreement qualification complaint documents")
class TenderFrameworkagreementQualificationComplaintDocumentResource(TenderEUQualificationComplaintDocumentResource):
    """ Tender Frameworkagreement Qualification Complaint Documents Resource """
