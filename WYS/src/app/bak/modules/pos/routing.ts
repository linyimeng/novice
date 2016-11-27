import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PosComponent } from './component';

import { RetailComponent } from './retail/retail';
import { RetailContentComponent } from './retail/content/component';

import { AuthTokenGuard } from '../auth/authtoken.guard';
const posRoutes:Routes = [
    // 当URL为 example.com/personnel 时导航到部门
    {
        path:'pos',
        redirectTo:'/pos/retail',
        canActivate: [ AuthTokenGuard ],
        pathMatch:'full',
    },
    {
        path:'pos',
        component:PosComponent,
        canActivate:[ AuthTokenGuard ],
        children:[
            { 
                path:'retail',
                component:RetailComponent,
                children:[
                    { path:'',component:RetailContentComponent },
                    { path:'content',component:RetailContentComponent }
                ] 
            },
        ]
    },
];

export const posRouting:ModuleWithProviders = RouterModule.forChild(posRoutes);
