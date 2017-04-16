from base_notifier import BaseNotifier
from bid import Bid

ITEMS_DELIMITER = " ### "


class CommBuysNotifier(BaseNotifier):
    def __init__(self):
        BaseNotifier.__init__(self)

    def get_site(self):
        return Bid.Site.COMMBUYS

    def get_items(self, bid):
        if bid.items:
            return ITEMS_DELIMITER.join(bid.items)
        else:
            return bid.description

    def get_url(self, bid):
        return "https://www.commbuys.com/bso/external/bidDetail.sdo?bidId={}" \
            .format(bid.identifier)
