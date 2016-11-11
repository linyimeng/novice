import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { WarehouseComponent } from './warehouse.component';

import { WarehouseLossRightComponent } from './loss/right-title/warehouse-loss-right-title.component';
import { WarehouseLossListComponent } from './loss/list/warehouse-loss-list.component';
import { WarehouseLossCreateComponent } from './loss/create/warehouse-loss-create.component';

import { WarehouseLastReportsRightComponent } from './warehouse-last-reports/right-title/warehouse-loss-right-title.component';
import { WarehouseLastReportsComponent } from './warehouse-last-reports/content/warehouse-last-reports-content.component';

import { WarehouseGoodsReportsRightComponent  } from './goods-last-reports/component';
import { GoodsLastReportsContentComponent } from './goods-last-reports/content/component';
//模块路由
import { warehouseRouting } from './warehouse.routing';

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

        WarehouseLastReportsRightComponent,
        WarehouseLastReportsComponent,

        WarehouseGoodsReportsRightComponent,
        GoodsLastReportsContentComponent,

    ],
    exports:[
    ],
    providers:[
        
    ]
})

export class WarehouseModule {}

