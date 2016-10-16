import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { DepartmentComponent } from './department.component';
import { StaffComponent } from './staff.component';

const appRoutes: Routes = [
    {
        path:'department',
        component:DepartmentComponent
    },
    {
        path:'',
        redirectTo:'department',
        pathMatch:'full'
    },
    {
        path:'staff',
        component:StaffComponent
    },
];

export const PersonnelRouting:ModuleWithProviders = RouterModule.forRoot(appRoutes);

