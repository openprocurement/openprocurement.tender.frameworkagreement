# -*- coding: utf-8 -*-
from openprocurement.tender.core.utils import optendersresource
from openprocurement.tender.openeu.views.cancellation import \
    TenderCancellationResource as TenderEUCancellationResource


@optendersresource(name='frameworkagreement:Tender Cancellations',
                   collection_path='/tenders/{tender_id}/cancellations',
                   path='/tenders/{tender_id}/cancellations/{cancellation_id}',
                   procurementMethodType='frameworkagreement',
                   description="Tender Frameworkagreement Cancellations")
class TenderFrameworkagreementCancellationResource(TenderEUCancellationResource):
    """ Tender Frameworkagreement Cancellation Resource """
