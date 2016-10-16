import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { DepartmentComponent } from './component/personnel/department.component';
import { AppComponent } from './app.component';
import { StaffComponent } from './component/personnel/staff.component';

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

export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);

