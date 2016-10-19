import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { DepartmentrightComponent } from './department-right/department-right.component';

import { StaffrightComponent } from './staff-right/staff-right.component';
import { StaffcreatComponent } from './staffcreat/staffcreat.component';
import { StaffcontentComponent } from './staffcontent/staffcontent.component';

export const personnelRouting = [
    {
        path:'',
        redirectTo:'department',
        pathMatch:'full'
    },
    {
        path:'department',
        component:DepartmentrightComponent
    },
    {
        path:'staff',
        component:StaffrightComponent,
        children:[
            {
                path:'',
                component:StaffcontentComponent
            },
            {
                path:"create",
                component:StaffcreatComponent
            },
            {
                path:'list',
                component:StaffcontentComponent
            },
        ]
    },
];

