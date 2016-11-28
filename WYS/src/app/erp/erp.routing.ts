import { Routes, RouterModule } from '@angular/router';

import { ErpHomeComponent } from './erp.component';

export const ErpRoutes: Routes = [
    {
        path:'',
        redirectTo:'/staff',
        pathMatch:'full',
    },
    { 
        path:'',
        component:ErpHomeComponent,
        children:[
            { path:'staff',loadChildren:()=>System.import('./modules/staff') },
            { path:'purchases',loadChildren:()=>System.import('./modules/purchases') },
            { path:'sales',loadChildren:()=>System.import('./modules/sales') },
            { path:'warehouse',loadChildren:()=>System.import('./modules/warehouse') },
        ]
    },
];