# This file has been generated by Connect SDK Wizard.
# Copyright (c) 2020 Ingram Micro. All Rights Reserved.

from connect import Flow


class PurchaseAssetFlow(Flow):
    def __init__(self):
        super().__init__(lambda request: request.type == 'purchase')
        self.step('Check item quantity', check_item_quantity) \
            .step('Check mail param', check_mail_param) \
            .step('Set purchase id', set_purchase_id) \
            .step('Approve request', approve_request)

    def check_item_quantity(self):
        for item in self.getAssetRequest().asset.items:
            if int(item.quantity) > 100000:
                self.fail('Cannot purchase product in such quantities.')

    def check_mail_param(self):
        for param in self.getAssetRequest().asset.params:
            if param.name == 'email' and not param.value:
                param.valueError = 'Email address has not been provided, please provide one.'
                self.inquire(None)

    def set_purchase_id(self):
        param = self.getAssetRequest().asset.getParamById('purchase_id')
        if param:
            param.value = '...'  # We can assign the id given by the external service here
        else:
            self.fail('The asset is expected to have a "purchase_id" param.')

    def approve_request(self):
        self.approveByTemplate('TL-000-000-000')
