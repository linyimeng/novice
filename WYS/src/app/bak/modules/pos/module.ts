import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule }   from '@angular/forms';

import { PosComponent } from './component';

import { RetailComponent } from './retail/retail';
import { RetailContentComponent } from './retail/content/component';

import { posRouting } from './routing';
import { SelectModule } from 'ng2-select';

@NgModule({
    imports:[
        CommonModule,
        FormsModule,
        posRouting,
        SelectModule
    ],
    declarations:[
        PosComponent,

        RetailComponent,
        RetailContentComponent
    ],
    providers:[
    ]
})

export class PosModule {}

