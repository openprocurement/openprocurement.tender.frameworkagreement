# -*- coding: utf-8 -*-
from openprocurement.tender.openeu.views.tender import TenderEUResource
from openprocurement.tender.core.utils import optendersresource


@optendersresource(name='frameworkagreement:Tender',
                   path='/tenders/{tender_id}',
                   procurementMethodType='frameworkagreement',
                   description="Open Contracting compatible data exchange format. See http://ocds.open-contracting.org/standard/r/master/#tender for more info")
class TenderFrameworkagreementResource(TenderEUResource):
    """ Resource handler for Tender Frameworkagreement """
