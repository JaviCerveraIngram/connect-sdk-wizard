# This file has been generated by Connect SDK Wizard.
# Copyright (c) 2020 Ingram Micro. All Rights Reserved.

from connect import Env
from connect import Processor
from connect.api import Query
from connect.logger import Logger, LoggerConfig

from flows.purchase_asset_flow import PurchaseAssetFlow
from flows.change_asset_flow import ChangeAssetFlow


if __name__ == '__main__':
    # Log level is set to debug. Never use this level when in production!
    Env.initLogger(LoggerConfig().level(Logger.LEVEL_DEBUG))

    # Process asset requests
    Processor() \
        .flow(PurchaseAssetFlow()) \
        .flow(ChangeAssetFlow()) \
        .processAssetRequests(Query() \
            .equal('asset.product.id__in', Env.getConfig().getProductsString()) \
            .equal('status', 'pending'))
