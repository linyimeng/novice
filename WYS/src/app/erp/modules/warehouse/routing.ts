import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { WarehouseComponent } from './warehouse';

import { WarehouseLossRightComponent } from './loss/loss';
import { WarehouseLossListComponent } from './loss/list/component';
import { WarehouseLossCreateComponent } from './loss/create/component';

import { WarehouseGoodsReportsRightComponent  } from './reports/goods-last-reports/goods-last-reports';
import { GoodsLastReportsContentComponent } from './reports/goods-last-reports/content/component';
const warehouseRoutes:Routes = [
    // '' 当路径为空时导航到首页，首页为部门
    {
        path:'',
        redirectTo:'/warehouse/reports/goodslastreports',
        pathMatch:'full'
    },
    {
        path:'',
        component:WarehouseComponent,
        children:[
            { 
                path:'loss',
                component:WarehouseLossRightComponent,
                children:[
                    { path:'',component:WarehouseLossListComponent },
                    { path:'list',component:WarehouseLossListComponent },
                    { path:'create',component:WarehouseLossCreateComponent}
                ]
            },
            {
                path:'reports',
                children:[
                    {
                        path:'goodslastreports',component:WarehouseGoodsReportsRightComponent,
                        children:[
                            {path:'',component:GoodsLastReportsContentComponent}
                        ]
                        
                    }
                ]
            },
        ]
    },
];

export const warehouseRouting:ModuleWithProviders = RouterModule.forChild(warehouseRoutes);
