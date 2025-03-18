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

API_ID       = int(os.environ.get("API_ID", "11824466"))
API_HASH     = os.environ.get("API_HASH", "5afd3ea9d0018ed654ae39a87aee62c7")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "7866098326:AAEOvwWtiCYwRY_m5PqWfeNQG3OpcNBC9DE")
SESSION      = os.environ.get("SESSION", "BQHFYKwAWfbfFed5GkMxqZrM6hmxNS2VJqh_tIxTToIxMA1AjSAbHY5VMqnUuDEx1g2BcVI3oYHzf0laOxtlMWZpHtGzaH1PiaMKrxamW0NI__iZ71GregM3GyYozXPR7hBu4odKvFZjk6g6Jn4CR1Piso32Z2WGRBA0gKOklTJqyMMJYXNKDHo_j2bH7fkFHE_sDBGJ8wkAIietDYWtQZPqcKux7cqhMXGjxLnd1y-UVpYcJaWKLMmvRUXH0PCSF_sGtGGddwt8amM3I6HcipUOc_SJFGPaySt0GiKE0q2ya9jhJYLbOq2KvSOqeNX7EOjrlSg_-LrIMgHAcEGGxqRetBvktQAAAAF_BT63AA")
TIME         = int(os.environ.get("TIME", 10))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1001605382205").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://satanmaman:satanmaman@satanmaman.hsumwsj.mongodb.net/?retryWrites=true&w=majority")
PORT         = os.environ.get("PORT", "8080")
