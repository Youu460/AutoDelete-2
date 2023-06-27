#=========================================================================
# [AutoDelete - Telegram bot to delete messages after specific time]      
# Copyright (C) 2022 Arunkumar Shibu                       
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#=========================================================================

import os

API_ID       = int(os.environ.get("API_ID", "3484286"))
API_HASH     = os.environ.get("API_HASH", "a6d454f36dece01cdab40663048b65f2")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "2084584822:AAG18z9a_2GqszStcVG6o4NaMI98nLJHOCI")
SESSION      = os.environ.get("SESSION", "BQAl9GyoYRc3UYRCPZ3h-gL07JAZxMvKMrnmaJaNygt6MXMbRAdpnH6uNIdar7AIyjoA4DUeD4H9AZiV_GStkb7_B7ITIhABUB8-sUtgFdwmTf_WhJFOWqA35pCxa-z0mQCslNMXCivuQPWjYDOD1JjO6BfGh2dxt-vVv6p0Mw-rsc3ARH1VvA2CDVd3mZnrx2RdG2kFWo_uc4QyQ8l9_ZSXz5mHPmI7zH6JsyzBShUMwwoBTdOA6ztYRQG7vMa-Lc7m377j4gdwsS5A8y4-WdntSzNFAN_jstCbgW3aQjJk7Pn7cNGJgOC3VAIn1dUVH_KoLqAYwYB1uatFAE-H0U6lAAAAAWchZMMA")
TIME         = int(os.environ.get("TIME", 10))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1001605382205").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://satanmaman:satanmaman@satanmaman.hsumwsj.mongodb.net/?retryWrites=true&w=majority")
PORT         = os.environ.get("PORT", "8080")
