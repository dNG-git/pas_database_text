# -*- coding: utf-8 -*-
##j## BOF

"""
direct PAS
Python Application Services
----------------------------------------------------------------------------
(C) direct Netware Group - All rights reserved
http://www.direct-netware.de/redirect.py?pas;database_text

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
59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
----------------------------------------------------------------------------
http://www.direct-netware.de/redirect.py?licenses;gpl
----------------------------------------------------------------------------
#echo(pasDatabaseTextVersion)#
#echo(__FILEPATH__)#
"""

from sqlalchemy.event import listen
from sqlalchemy.schema import Column, DDL
from sqlalchemy.types import TEXT, VARCHAR

from .abstract import Abstract

class TextEntry(Abstract):
#
	"""
"TextEntry" contains the database representation for a text entry.

:author:     direct Netware Group
:copyright:  direct Netware Group - All rights reserved
:package:    pas
:subpackage: database_text
:since:      v0.1.00
:license:    http://www.direct-netware.de/redirect.py?licenses;gpl
             GNU General Public License 2
	"""

	# pylint: disable=invalid-name,unused-argument

	__tablename__ = "{0}_text_entry".format(Abstract.get_table_prefix())
	"""
SQLAlchemy table name
	"""
	db_schema_version = 1
	"""
Database schema version
	"""

	id = Column(VARCHAR(32), primary_key = True)
	"""
text_entry.id
	"""
	content = Column(TEXT)
	"""
text_entry.content
	"""

	@classmethod
	def before_apply_schema(cls):
	#
		"""
Called before applying the SQLAlchemy generated schema to register the
custom DDL for PostgreSQL.

:since: v0.1.00
	"""

		create_postgresql_tsvector_index = "CREATE INDEX idx_{0}_text_entry_content ON {0}_text_entry USING gin(to_tsvector('simple', content));"
		create_postgresql_tsvector_index = create_postgresql_tsvector_index.format(cls.get_table_prefix())

		listen(cls.__table__,
		       "after_create",
		       DDL(create_postgresql_tsvector_index).execute_if(dialect = "postgresql")
		      )
	#
#
#

##j## EOF