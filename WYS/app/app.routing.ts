import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PersonnelComponent } from './modules/personnel/personnel.component';
import { personnelRouting } from './modules/personnel/personnel.routing';

import { LoginComponent } from './modules/auth/login.component';

const appRoutes: Routes = [
    {
        path:'personnel',
        component:PersonnelComponent,
        children:personnelRouting,
    },
    {
        path:'',
        redirectTo:'personnel',
        pathMatch:'full'
    },
];

export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);

