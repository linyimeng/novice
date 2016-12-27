import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { WarehouseComponent } from './warehouse';

import { WarehouseLossRightComponent } from './loss/loss';
import { WarehouseLossListComponent } from './loss/list/component';
import { WarehouseLossCreateComponent } from './loss/create/component';

import { WarehouseGoodsReportsRightComponent  } from './reports/goods-last-reports/goods-last-reports';
import { GoodsLastReportsContentComponent } from './reports/goods-last-reports/content/component';
//模块路由
import { warehouseRouting } from './routing';

@NgModule({
    imports:[
        CommonModule,
        warehouseRouting,
    ],
    declarations:[
        WarehouseComponent,

        WarehouseLossRightComponent,
        WarehouseLossListComponent,
        WarehouseLossCreateComponent,

        WarehouseGoodsReportsRightComponent,
        GoodsLastReportsContentComponent,
    ],
    exports:[
    ],
    providers:[
        
    ]
})

export default class WarehouseModule {}

