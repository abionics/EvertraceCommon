from tvmbase.models.tvm.account import Account

from common.constants import NEVER_EXISTS_ACCOUNT_NAME
from common.services.detector.response.detected import Detected


def detect_special(account: Account) -> Detected:
    if account.data is None:
        return Detected.from_special(NEVER_EXISTS_ACCOUNT_NAME)
    if account.data.code_hash is None:
        name = '<' + account.data.acc_type_name + '>'
        return Detected.from_special(name)
