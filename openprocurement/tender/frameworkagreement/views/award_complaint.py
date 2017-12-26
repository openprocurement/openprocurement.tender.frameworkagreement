# -*- coding: utf-8 -*-
from openprocurement.tender.core.utils import optendersresource
from openprocurement.tender.openeu.views.award_complaint import TenderEUAwardComplaintResource


@optendersresource(name='frameworkagreement:Tender Award Complaints',
                   collection_path='/tenders/{tender_id}/awards/{award_id}/complaints',
                   path='/tenders/{tender_id}/awards/{award_id}/complaints/{complaint_id}',
                   procurementMethodType='frameworkagreement',
                   description="Tender Frameworkagreement Award complaints")
class TenderFrameworkagreementAwardComplaintResource(TenderEUAwardComplaintResource):
    """ Tender Frameworkagreement Award Complaint Resource """
