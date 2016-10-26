import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { SalesComponent } from './sales.component';

import { ClientRightComponent } from './client/right-title/client-right.component';
import { ClientListComponent } from './client/list/client-list.component';

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
    ],
    exports:[
    ],
    providers:[
        
    ]
})

export class SalesModule {}

