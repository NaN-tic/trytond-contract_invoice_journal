# This file is part of the contract_invoice_journal module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite
import unittest


class ContractInvoiceJournalTestCase(ModuleTestCase):
    'Test Contract Invoice Journal module'
    module = 'contract_invoice_journal'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            ContractInvoiceJournalTestCase))
    return suite
