# This file is part of the contract_invoice_journal module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta


__all__ = ['Configuration']


class Configuration:
    __metaclass__ = PoolMeta
    __name__ = 'contract.configuration'
    default_journal = fields.Property(fields.Many2One('account.journal',
            'Default Journal'))
