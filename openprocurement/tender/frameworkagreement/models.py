# -*- coding: utf-8 -*-
from zope.interface import implementer

from schematics.types import StringType

from openprocurement.tender.openeu.models import (
    IAboveThresholdEUTender
)
from openprocurement.tender.openeu.models import (
    Tender as BaseTender,
)


class IFrameworkagreementTender(IAboveThresholdEUTender):
    """ Marker interface for frameworkagreement tenders """


@implementer(IFrameworkagreementTender)
class Tender(BaseTender):
    """ frameworkagreement Tender model """

    procurementMethodType = StringType(default="frameworkagreement")


TenderFrameworkagreement = Tender
