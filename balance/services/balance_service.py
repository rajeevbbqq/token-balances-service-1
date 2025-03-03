from infrastructure.repository.snapshot_repository import Snapshot
from http import HTTPStatus

snapshot = Snapshot()


def find_snapshot_by_address(address):
    snapshot_details = snapshot.find_by_address(address)
    if snapshot_details is not None:

        data = {
            "wallet_address": address,
            "balance_in_cogs": snapshot_details.balance_in_cogs,
            "snapshot_date": str(snapshot_details.snapshot_date),
            "transfer_info": None,
        }

        transfer_details = snapshot.find_transfer_status(address)

        if transfer_details is not None:
            data["transfer_info"] = {
                "converted_tokens": transfer_details.transfer_amount_in_cogs,
                "transfer_time": str(transfer_details.transfer_time),
                "transaction_hash": transfer_details.transfer_transaction,
            }

        message = HTTPStatus.OK.phrase
        statusCode = HTTPStatus.OK.value
    else:
        data = None
        statusCode = HTTPStatus.BAD_REQUEST.value
        message = "Address not found in snapshot"

    return statusCode, message, data
