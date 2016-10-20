import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

import { PurchasesComponent } from './purchases.component';

import { GoodsRightComponent } from './goods/goods-right/goods-right.component';
import { GoodsListComponent } from './goods/goods-list/goods-list.component';
import { GoodsCreateComponent } from './goods/goods-create/goods-create.component';

import { SupplierRightComponent } from './supplier/supplier-right/supplier-right.component';
import { SupplierCreateComponent } from './supplier/supplier-create/supplier-create.component';
import { SupplierListComponent } from './supplier/supplier-list/supplier-list.component';


@NgModule({
    imports:[
        CommonModule,
        RouterModule,
    ],
    declarations:[
        GoodsRightComponent,
        GoodsListComponent,
        GoodsCreateComponent,

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

