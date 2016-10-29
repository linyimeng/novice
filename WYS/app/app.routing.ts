import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { LoginComponent } from './modules/auth/login.component';

const appRoutes: Routes = [
    {
        path:'',
        redirectTo:'/personnel/department',
        pathMatch:'full'
    },
    { path:'login',component: LoginComponent}
];

export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);

