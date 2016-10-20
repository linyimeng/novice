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
    ],
    exports:[
    ],
    providers:[

    ]
})

export class PurchasesModule {}

