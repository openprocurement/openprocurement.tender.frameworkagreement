# -*- coding: utf-8 -*-
from pyramid.interfaces import IRequest
from openprocurement.api.interfaces import IContentConfigurator
from openprocurement.tender.frameworkagreement.models import Tender, IFrameworkagreementTender
from openprocurement.tender.frameworkagreement.adapters import TenderFrameworkagreementConfigurator


def includeme(config):
    config.add_tender_procurementMethodType(Tender)
    config.scan("openprocurement.tender.frameworkagreement.views")
#    config.scan("openprocurement.tender.frameworkagreement.subscribers")
    config.registry.registerAdapter(TenderFrameworkagreementConfigurator,
                                    (IFrameworkagreementTender, IRequest),
                                    IContentConfigurator)