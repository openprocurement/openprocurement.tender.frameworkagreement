# -*- coding: utf-8 -*-
from copy import deepcopy
from datetime import timedelta

from openprocurement.api.utils import get_now

from openprocurement.tender.frameworkagreement.models import TenderFrameworkagreement


# TenderFrameworkagreementTest


def simple_add_tender(self):
    u = TenderFrameworkagreement(self.initial_data)
    u.tenderID = "UA-X"
    u.noticePublicationDate = get_now().isoformat()

    assert u.id is None
    assert u.rev is None

    u.store(self.db)

    assert u.id is not None
    assert u.rev is not None

    fromdb = self.db.get(u.id)

    assert u.tenderID == fromdb['tenderID']
    assert u.doc_type == "Tender"
    assert u.procurementMethodType == "frameworkagreement"
    assert fromdb['procurementMethodType'] == "frameworkagreement"

    u.delete_instance(self.db)
