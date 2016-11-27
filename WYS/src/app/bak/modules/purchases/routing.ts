import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

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

import { AuthTokenGuard } from '../auth/authtoken.guard';
const purchasesRoutes:Routes = [
    // 当URL为 example.com/purchases 时导航到商品 goods
    {
        path:'purchases',
        redirectTo:'/purchases/goods',
        pathMatch:'full',
        canActivate:[AuthTokenGuard]
    },
    { path:'purchases',component:PurchasesComponent },
    {
        path:'purchases',
        component:PurchasesComponent,
        canActivate:[AuthTokenGuard],
        children:[
            {
                path:'goods',
                component:GoodsComponent,
                children:[
                    { path:'', component:GoodsListComponent,},
                    { path:'create', component:GoodsCreateComponent,},
                    { path:'list', component:GoodsListComponent, },
                    { path:':pk',component:GoodsDetailComponent },
                ]
            },
            {
                path:'supplier',
                component:SupplierComponent,
                children:[
                    { path:'', component:SupplierListComponent },
                    { path:"create", component:SupplierCreateComponent },
                    { path:'list', component:SupplierListComponent },
                    { path:':pk',component:SupplierDetailComponent }
                ]
            },
            {
                path:'purchaseorder',
                component:PurchaseOrdersComponent,
                children:[
                    { path:'',component:PurchaseOrdersListComponent},
                    { path:'list',component:PurchaseOrdersListComponent},
                    { path:'create',component: PurchaseOrdersCreateComponent},
                    { path:':ordercode',component:PurchaseOrdersDetailComponent}
                ]
            },
            {
                path:'reports',
                children:[
                    { 
                        path:'purchaseorders',
                        component:GoodsPurchaseReportsComponent,
                        children:[
                            {path:'',component:GoodsPurchaseListComponent}
                        ]
                    },
                    {
                        path:'supplier',
                        component:SupplierPurchaseReportsComponent,
                        children:[
                            { path:'',component:SupplierPurchaseListComponent}
                        ]
                    },
                ]
            },
        ]
    },
];

export const purchasesRouting:ModuleWithProviders = RouterModule.forChild(purchasesRoutes);