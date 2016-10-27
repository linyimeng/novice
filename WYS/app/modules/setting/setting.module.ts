import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { SettingComponent } from './setting.component';

import { UsersRightComponent } from './users/right-title/setting-users-right-title.component';
import { UsersListComponent } from './users/list/setting-users-list.component';
import { UsersCreateComponent } from './users/create/setting-users-create.component';
//模块路由
import { SettingRouting } from './setting.routing';


@NgModule({
    imports:[
        CommonModule,
        SettingRouting,
    ],
    declarations:[
        SettingComponent,

        UsersRightComponent,
        UsersListComponent,
        UsersCreateComponent,

    ],
    exports:[
    ],
    providers:[
        
    ]
})

export class SettingModule {}

