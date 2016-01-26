# This file is part of the contract_invoice_journal module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta


__all__ = ['ContractConsumption']
__metaclass__ = PoolMeta


class ContractConsumption:
    __name__ = 'contract.consumption'

    @classmethod
    def _get_invoice(cls, keys):
        config = Pool().get('contract.configuration')(1)
        invoice = super(ContractConsumption, cls)._get_invoice(keys)
        journal = config.default_journal
        if journal:
            invoice.journal = journal
        return invoice
