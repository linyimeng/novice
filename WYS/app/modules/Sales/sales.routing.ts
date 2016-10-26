import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { SalesComponent } from './sales.component';

import { ClientRightComponent } from './client/right-title/client-right.component';
import { ClientListComponent } from './client/list/client-list.component';
const salesRoutes:Routes = [
    // '' 当路径为空时导航到首页，首页为部门
    { 
        path:'sales',
        redirectTo:'/sales/client',
        pathMatch:'full'
    },
    { path:'sales',component:SalesComponent },
    { 
        path:'sales',
        component:SalesComponent,
        children:[
            {
                path:'client',
                component:ClientRightComponent,
                children:[
                    { path:'',component:ClientListComponent },
                    { path:'list',component:ClientListComponent },
                ]
            },
        ]
    },
];

export const salesRouting:ModuleWithProviders = RouterModule.forChild(salesRoutes);
