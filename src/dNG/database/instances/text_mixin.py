# -*- coding: utf-8 -*-

"""
direct PAS
Python Application Services
----------------------------------------------------------------------------
(C) direct Netware Group - All rights reserved
https://www.direct-netware.de/redirect?pas;database_text

The following license agreement remains valid unless any additions or
changes are being made by direct Netware Group in a written form.

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 2 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
more details.

You should have received a copy of the GNU General Public License along with
this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
----------------------------------------------------------------------------
https://www.direct-netware.de/redirect?licenses;gpl
----------------------------------------------------------------------------
#echo(pasDatabaseTextVersion)#
#echo(__FILEPATH__)#
"""

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import foreign, relationship, remote

from .text_entry import TextEntry

class TextMixin(object):
    """
"TextMixin" provides a relationship to an text entry in the database based
on the object ID.

:author:     direct Netware Group et al.
:copyright:  direct Netware Group - All rights reserved
:package:    pas
:subpackage: database_text
:since:      v0.2.00
:license:    https://www.direct-netware.de/redirect?licenses;gpl
             GNU General Public License 2
    """

    @declared_attr
    def rel_text_entry(self):
        """
Relation to TextEntry

:return: (object) SQLAlchemy relationship description
:since:  v0.2.00
        """

        return relationship(TextEntry, primaryjoin = (foreign(self.id) == remote(TextEntry.id)), uselist = False)
    #
#
