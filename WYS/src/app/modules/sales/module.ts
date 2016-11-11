import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { SalesComponent } from './sales';

import { ClientRightComponent } from './client/component';
import { ClientListComponent } from './client/list/component';
import { ClientCreateComponent } from './client/create/component';
import { ClientDetailComponent } from './client/detail/component';

import { SalesOrdersRightComponent } from './sales-order/component';
import { SalesOrdersListComponent } from './sales-order/list/component';
import { SalesOrdersCreateComponent } from './sales-order/create/component';

import { GoodsSalesReportsRightComponent } from './goods-sales-reports/component';
import { GoodsSalesReportsComponent } from './goods-sales-reports/content/component';
//模块路由
import { salesRouting } from './routing';

@NgModule({
    imports:[
        CommonModule,
        salesRouting,
    ],
    declarations:[
        SalesComponent,

        ClientRightComponent,
        ClientListComponent,
        ClientCreateComponent,
        ClientDetailComponent,

        SalesOrdersRightComponent,
        SalesOrdersListComponent,
        SalesOrdersCreateComponent,
        GoodsSalesReportsRightComponent,
        GoodsSalesReportsComponent,

    ],
    exports:[
    ],
    providers:[
        
    ]
})

export class SalesModule {}

