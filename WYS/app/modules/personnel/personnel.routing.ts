import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { DepartmentComponent } from './department.component';
import { StaffComponent } from './staff.component';
import { StaffcreatComponent } from './staffcreat/staffcreat.component';
import { StaffcontentComponent } from './staffcontent/staffcontent.component';

export const PersonnelRouting:ModuleWithProviders = RouterModule.forRoot([
    {
        path:'',
        redirectTo:'department',
        pathMatch:'full'
    },
    {
        path:'department',
        component:DepartmentComponent
    },
    {
        path:'staff',
        component:StaffComponent,
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
]);

