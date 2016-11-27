import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { SettingComponent } from './setting.component';

import { UsersRightComponent } from './users/right-title/setting-users-right-title.component';
import { UsersListComponent } from './users/list/setting-users-list.component';
import { UsersCreateComponent } from './users/create/setting-users-create.component';

const settingRoutes:Routes = [
    {
        path:'setting',
        redirectTo:'/setting/users',
        pathMatch:'full'
    },
    {
        path:'setting',
        component:SettingComponent,
        children:[
            {
                path:'users',
                component:UsersRightComponent,
                children:[
                    { path:'',component:UsersListComponent },
                    { path:'list',component:UsersListComponent},
                    { path:'create',component:UsersCreateComponent},
                ]
            }
        ]
    },
];

export const SettingRouting:ModuleWithProviders = RouterModule.forChild(settingRoutes);
