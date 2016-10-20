import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { GoodsRightComponent } from './goods/goods-right/goods-right.component';
import { GoodsListComponent } from './goods/goods-list/goods-list.component';
import { GoodsCreateComponent } from './goods/goods-create/goods-create.component';

import { SupplierRightComponent } from './supplier/supplier-right/supplier-right.component';
import { SupplierCreateComponent } from './supplier/supplier-create/supplier-create.component';
import { SupplierListComponent } from './supplier/supplier-list/supplier-list.component';

export const PurchasesRouting = [
    {
        path:'',
        redirectTo:'supplier',
        pathMatch:'full'
    },
    {
        path:'goods',
        component:GoodsRightComponent,
        children:[
            {
                path:'',
                component:GoodsListComponent,
            },
            {
                path:'create',
                component:GoodsCreateComponent,
            },
            {
                path:'list',
                component:GoodsListComponent,
            },
        ]
    },
    {
        path:'supplier',
        component:SupplierRightComponent,
        children:[
            {
                path:'',
                component:SupplierListComponent
            },
            {
                path:"create",
                component:SupplierCreateComponent
            },
            {
                path:'list',
                component:SupplierListComponent
            },
        ]
    },
];

