# -*- coding: utf-8 -*-

##############################################################################
#
# Customer Owned Products
# Copyright (C) 2014 OpusVL (<http://opusvl.com>)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api

class CustomerSpecificProducts(models.Model):
    """Add customer-specific and customer-owned fields to products.
    """
    _inherit = 'product.template'

    customer_specific_id = fields.Many2one('res.partner',
        string='Specific to Customer',
        domain=[('customer', '=', True)],
        help='Fill this in if this product is specific to a certain customer',
    )

    is_customer_owned = fields.Boolean(string='Customer owned')

    @api.onchange('customer_specific_id')
    def _onchange_customer_specific_id(self):
        """Automatically untick is_customer_owned when customer_specific_id is set to blank.
        """
        if not self.customer_specific_id:
            self.is_customer_owned = False

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
