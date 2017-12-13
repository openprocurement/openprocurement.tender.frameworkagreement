# -*- coding: utf-8 -*-
from openprocurement.tender.openeu.adapters import TenderAboveThresholdEUConfigurator
from openprocurement.tender.frameworkagreement.models import Tender


class TenderFrameworkagreementConfigurator(TenderAboveThresholdEUConfigurator):
    """ Frameworkagreement Tender configuration adapter """

    name = "frameworkagreement Tender configurator"
    model = Tender


