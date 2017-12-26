# -*- coding: utf-8 -*-
from openprocurement.tender.core.utils import optendersresource
from openprocurement.tender.openeu.views.question import \
    TenderQuestionResource as TenderEUQuestionResource


@optendersresource(name='frameworkagreement:Tender Questions',
                   collection_path='/tenders/{tender_id}/questions',
                   path='/tenders/{tender_id}/questions/{question_id}',
                   procurementMethodType='frameworkagreement',
                   description="Tender Frameworkagreement questions")
class TenderFrameworkagreementQuestionResource(TenderEUQuestionResource):
    """ Tender Frameworkagreement Question Resource """
