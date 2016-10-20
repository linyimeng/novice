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
                    { path:'detail',component:GoodsDetailComponent },
                ]
            },
            {
                path:'supplier',
                component:SupplierRightComponent,
                children:[
                    { path:'', component:SupplierListComponent },
                    { path:"create", component:SupplierCreateComponent },
                    { path:'list', component:SupplierListComponent },
                ]
            },
        ]
    },
];

export const purchasesRouting:ModuleWithProviders = RouterModule.forChild(purchasesRoutes);