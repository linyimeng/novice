import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule }   from '@angular/forms';

import { PurchasesComponent } from './component';

import { GoodsComponent } from './goods/goods';
import { GoodsListComponent } from './goods/list/component';
import { GoodsCreateComponent } from './goods/create/component';
import { GoodsDetailComponent } from './goods/detail/component';

import { SupplierComponent } from './supplier/supplier';
import { SupplierCreateComponent } from './supplier/create/component';
import { SupplierListComponent } from './supplier/list/component';
import { SupplierDetailComponent } from './supplier/detail/component';

import { PurchaseOrdersComponent } from './purchase-orders/purchaseorders';
import { PurchaseOrdersListComponent } from './purchase-orders/list/component';
import { PurchaseOrdersCreateComponent } from './purchase-orders/create/component';
import { PurchaseOrdersDetailComponent } from './purchase-orders/detail/component';

import { GoodsPurchaseReportsComponent } from './reports/goods-purchase/goods-purchase';
import { GoodsPurchaseListComponent } from './reports/goods-purchase/list/component';

import { SupplierPurchaseReportsComponent } from './reports/supplier-purchase/supplier-purchase';
import { SupplierPurchaseListComponent } from './reports/supplier-purchase/list/component';

import { purchasesRouting } from './routing';

import { GoodsService } from '../../../services/goods.service';
import { TypeattrService } from '../../../services/typeattr.service';
import { CompanyService } from '../../../services/company.service';

import { GoodstypeSelectComponent } from '../erpform/goodstype-select';
import { SupplierSelectComponent } from '../erpform/supplier-select';
import { ImgUploadComponent } from '../erpform/imgupload';
import { SelectModule } from 'ng2-select';
@NgModule({
    imports:[
        CommonModule,
        FormsModule,
        SelectModule,
        purchasesRouting
    ],
    declarations:[
        GoodsComponent,
        GoodsListComponent,
        GoodsCreateComponent,
        GoodsDetailComponent,

        PurchasesComponent,
        SupplierComponent,
        SupplierCreateComponent,
        SupplierListComponent,
        SupplierDetailComponent,

        PurchaseOrdersComponent,
        PurchaseOrdersListComponent,
        PurchaseOrdersCreateComponent,
        PurchaseOrdersDetailComponent,

        GoodsPurchaseReportsComponent,
        GoodsPurchaseListComponent,

        SupplierPurchaseReportsComponent,
        SupplierPurchaseListComponent,
        
        GoodstypeSelectComponent,
        SupplierSelectComponent,
        ImgUploadComponent,
    ],
    providers:[
        GoodsService,
        TypeattrService,
        CompanyService,
    ]
})

export default class PurchasesModule {}

