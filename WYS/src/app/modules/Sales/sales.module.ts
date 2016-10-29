import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { SalesComponent } from './sales.component';

import { ClientRightComponent } from './client/right-title/client-right.component';
import { ClientListComponent } from './client/list/client-list.component';
import { ClientCreateComponent } from './client/create/client-create.component';
import { ClientDetailComponent } from './client/detail/client-detail.component';

import { SalesOrdersRightComponent } from './sales-order/right-title/sales-order-right-title.component';
import { SalesOrdersListComponent } from './sales-order/list/sales-order-list.component';
import { SalesOrdersCreateComponent } from './sales-order/create/sales-order-create.component';

import { DateSalesReportsRightComponent } from './date-sales-reports/right-title/date-sales-reports-right-title.component';
import { DateSalesReportsComponent } from './date-sales-reports/content/date-sales-reports-content.component';

import { GoodsSalesReportsRightComponent } from './goods-sales-reports/right-title/goods-sales-reports-right-title.component';
import { GoodsSalesReportsComponent } from './goods-sales-reports/content/goods-sales-reports-content.component';

import { ClientSalesReportsRightComponent } from './client-sales-reports/right-title/client-sales-reports-right-title.component';
import { ClientSalesReportsComponent } from './client-sales-reports/content/client-sales-reports-content.component';
//模块路由
import { salesRouting } from './sales.routing';

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

        DateSalesReportsRightComponent,
        DateSalesReportsComponent,
        GoodsSalesReportsRightComponent,
        GoodsSalesReportsComponent,

        ClientSalesReportsRightComponent,
        ClientSalesReportsComponent,

    ],
    exports:[
    ],
    providers:[
        
    ]
})

export class SalesModule {}

