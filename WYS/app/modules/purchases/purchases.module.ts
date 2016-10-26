import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PurchasesComponent } from './purchases.component';

import { GoodsRightComponent } from './goods/goods-right/goods-right.component';
import { GoodsListComponent } from './goods/goods-list/goods-list.component';
import { GoodsCreateComponent } from './goods/goods-create/goods-create.component';
import { GoodsDetailComponent } from './goods/goods-detail/goods-detail.component';

import { SupplierRightComponent } from './supplier/supplier-right/supplier-right.component';
import { SupplierCreateComponent } from './supplier/supplier-create/supplier-create.component';
import { SupplierListComponent } from './supplier/supplier-list/supplier-list.component';

import { PurchaseOrdersRightComponent } from './purchase-orders/purchase-orders-right/purchase-orders-right.component';
import { PurchaseOrdersListComponent } from './purchase-orders/purchase-orders-list/purchase-orders-list.component';
import { PurchaseOrdersCreateComponent } from './purchase-orders/purchase-orders-create/purchase-orders-create.component';

import { GoodsPurchaseReportsRightComponent } from './goods-purchase-reports/goods-purchase-reports-right/goods-purchase-reports-right.component';
import { GoodsPurchaseReportsContentComponent } from './goods-purchase-reports/goods-purchase-reports-content/goods-purchase-reports-content.component';

import { SupplierPurchaseReportsRightComponent } from './supplier-purchase-reports/supplier-purchase-reports-right/supplier-purchase-reports-right.component';
import { SupplierPurchaseReportsContentComponent } from './supplier-purchase-reports/supplier-purchase-reports-content/supplier-purchase-reports.component';

import { purchasesRouting } from './purchases.routing';

@NgModule({
    imports:[
        CommonModule,
        purchasesRouting,
    ],
    declarations:[
        GoodsRightComponent,
        GoodsListComponent,
        GoodsCreateComponent,
        GoodsDetailComponent,

        PurchasesComponent,
        SupplierRightComponent,
        SupplierCreateComponent,
        SupplierListComponent,

        PurchaseOrdersRightComponent,
        PurchaseOrdersListComponent,
        PurchaseOrdersCreateComponent,

        GoodsPurchaseReportsRightComponent,
        GoodsPurchaseReportsContentComponent,

        SupplierPurchaseReportsRightComponent,
        SupplierPurchaseReportsContentComponent

    ],
    exports:[
    ],
    providers:[

    ]
})

export class PurchasesModule {}

