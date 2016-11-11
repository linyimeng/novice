import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { WarehouseComponent } from './warehouse.component';

import { WarehouseLossRightComponent } from './loss/right-title/warehouse-loss-right-title.component';
import { WarehouseLossListComponent } from './loss/list/warehouse-loss-list.component';
import { WarehouseLossCreateComponent } from './loss/create/warehouse-loss-create.component';

import { WarehouseLastReportsRightComponent } from './warehouse-last-reports/right-title/warehouse-loss-right-title.component';
import { WarehouseLastReportsComponent } from './warehouse-last-reports/content/warehouse-last-reports-content.component';

import { WarehouseGoodsReportsRightComponent  } from './goods-last-reports/component';
import { GoodsLastReportsContentComponent } from './goods-last-reports/content/component';
const warehouseRoutes:Routes = [
    // '' 当路径为空时导航到首页，首页为部门
    {
        path:'warehouse',
        redirectTo:'/warehouse/loss',
        pathMatch:'full'
    },
    {
        path:'warehouse',
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
                        path:'warehouselastreports',component:WarehouseLastReportsRightComponent,
                        children:[
                            { path:'',component:WarehouseLastReportsComponent }
                        ]
                    },
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
