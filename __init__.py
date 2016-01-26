# This file is part of the contract_invoice_journal module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool

from configuration import *
from contract import *


def register():
    Pool.register(
        Configuration,
        ContractConsumption,
        module='contract_invoice_journal', type_='model')
