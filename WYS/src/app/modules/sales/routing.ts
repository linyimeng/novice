import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { SalesComponent } from './sales';

import { ClientRightComponent } from './client/component';
import { ClientListComponent } from './client/list/component';
import { ClientCreateComponent } from './client/create/component';
import { ClientDetailComponent } from './client/detail/component';

import { SalesOrdersRightComponent } from './sales-order/component';
import { SalesOrdersListComponent } from './sales-order/list/component';
import { SalesOrdersCreateComponent } from './sales-order/create/component';

import { GoodsSalesReportsRightComponent } from './goods-sales-reports/component';
import { GoodsSalesReportsComponent } from './goods-sales-reports/content/component';
const salesRoutes:Routes = [
    // '' 当路径为空时导航到首页，首页为部门
    {
        path:'sales',
        redirectTo:'/sales/reports/goodssales',
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
                    { path:'create',component:ClientCreateComponent},
                    { path:'detail',component:ClientDetailComponent },
                ]
            },
            {
                path:'salesorder',
                component:SalesOrdersRightComponent,
                children:[
                    { path:'',component:SalesOrdersListComponent },
                    { path:'list',component:SalesOrdersListComponent },
                    { path:'create',component:SalesOrdersCreateComponent },
                ]
            },
            {
                path:'reports',
                children:[
                    {
                        path:'goodssales',
                        component:GoodsSalesReportsRightComponent,
                        children:[
                            { path:'',component:GoodsSalesReportsComponent },
                        ]
                    },
                ]
            },
        ]
    },
];

export const salesRouting:ModuleWithProviders = RouterModule.forChild(salesRoutes);
