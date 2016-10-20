import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PersonnelComponent } from './modules/personnel/personnel.component';
import { personnelRouting } from './modules/personnel/personnel.routing';

import { PurchasesComponent } from './modules/purchases/purchases.component';
import { PurchasesRouting } from './modules/purchases/purchases.routing';

import { LoginComponent } from './modules/auth/login.component';

const appRoutes: Routes = [
    {
        path:'personnel',
        component:PersonnelComponent,
        children:personnelRouting,
    },
    {
        path:'purchases',
        component:PurchasesComponent,
        children:PurchasesRouting,
    },
    {
        path:'',
        redirectTo:'personnel',
        pathMatch:'full'
    },
];

export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);

