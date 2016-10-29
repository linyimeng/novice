import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PurchasesComponent } from './purchases.component';

import { GoodsRightComponent } from './goods/goods-right/goods-right.component';
import { GoodsListComponent } from './goods/goods-list/goods-list.component';
import { GoodsCreateComponent } from './goods/goods-create/goods-create.component';
import { GoodsDetailComponent } from './goods/goods-detail/goods-detail.component';

import { SupplierRightComponent } from './supplier/supplier-right/supplier-right.component';
import { SupplierCreateComponent } from './supplier/supplier-create/supplier-create.component';
import { SupplierListComponent } from './supplier/supplier-list/supplier-list.component';
import { SupplierDetailComponent } from './supplier/supplier-detail/supplier-detail.component';

import { PurchaseOrdersRightComponent } from './purchase-orders/purchase-orders-right/purchase-orders-right.component';
import { PurchaseOrdersListComponent } from './purchase-orders/purchase-orders-list/purchase-orders-list.component';
import { PurchaseOrdersCreateComponent } from './purchase-orders/purchase-orders-create/purchase-orders-create.component';

import { GoodsPurchaseReportsRightComponent } from './goods-purchase-reports/goods-purchase-reports-right/goods-purchase-reports-right.component';
import { GoodsPurchaseReportsContentComponent } from './goods-purchase-reports/goods-purchase-reports-content/goods-purchase-reports-content.component';

import { SupplierPurchaseReportsRightComponent } from './supplier-purchase-reports/supplier-purchase-reports-right/supplier-purchase-reports-right.component';
import { SupplierPurchaseReportsContentComponent } from './supplier-purchase-reports/supplier-purchase-reports-content/supplier-purchase-reports.component';
const purchasesRoutes:Routes = [
    // 当URL为 example.com/purchases 时导航到商品 goods
    {
        path:'purchases',
        redirectTo:'/purchases/goods',
        pathMatch:'full'
    },
    { path:'purchases',component:PurchasesComponent },
    {
        path:'purchases',
        component:PurchasesComponent,
        children:[
            {
                path:'goods',
                component:GoodsRightComponent,
                children:[
                    { path:'', component:GoodsListComponent,},
                    { path:'create', component:GoodsCreateComponent,},
                    { path:'list', component:GoodsListComponent, },
                    { path:':pk',component:GoodsDetailComponent },
                ]
            },
            {
                path:'supplier',
                component:SupplierRightComponent,
                children:[
                    { path:'', component:SupplierListComponent },
                    { path:"create", component:SupplierCreateComponent },
                    { path:'list', component:SupplierListComponent },
                    { path:':pk',component:SupplierDetailComponent }
                ]
            },
            {
                path:'purchaseorder',
                component:PurchaseOrdersRightComponent,
                children:[
                    { path:'',component:PurchaseOrdersListComponent},
                    { path:'list',component:PurchaseOrdersListComponent},
                    { path:'create',component: PurchaseOrdersCreateComponent}
                ]
            },
            {
                path:'reports',
                children:[
                    { 
                        path:'purchaseorders',
                        component:GoodsPurchaseReportsRightComponent,
                        children:[
                            {path:'',component:GoodsPurchaseReportsContentComponent}
                        ]
                    },
                    {
                        path:'supplier',
                        component:SupplierPurchaseReportsRightComponent,
                        children:[
                            { path:'',component:SupplierPurchaseReportsContentComponent}
                        ]
                    },
                ]
            },
        ]
    },
];

export const purchasesRouting:ModuleWithProviders = RouterModule.forChild(purchasesRoutes);