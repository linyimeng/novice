import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { SalesComponent } from './sales.component';

import { ClientRightComponent } from './client/right-title/client-right.component';
import { ClientListComponent } from './client/list/client-list.component';
import { ClientCreateComponent } from './client/create/client-create.component';
import { ClientDetailComponent } from './client/detail/client-detail.component';

import { SalesOrdersRightComponent } from './sales-order/right-title/sales-order-right-title.component';
import { SalesOrdersListComponent } from './sales-order/list/sales-order-list.component';
import { SalesOrdersCreateComponent } from './sales-order/create/sales-order-create.component';

import { DateSalesReportsRightComponent } from './date-sales-reports/right-title/date-sales-reports-right-title.component';
import { DateSalesReportsComponent } from './date-sales-reports/content/date-sales-reports-content.component';

import { GoodsSalesReportsRightComponent } from './goods-sales-reports/right-title/goods-sales-reports-right-title.component';
import { GoodsSalesReportsComponent } from './goods-sales-reports/content/goods-sales-reports-content.component';

import { ClientSalesReportsRightComponent } from './client-sales-reports/right-title/client-sales-reports-right-title.component';
import { ClientSalesReportsComponent } from './client-sales-reports/content/client-sales-reports-content.component';
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
                        path:'datesales',
                        component:DateSalesReportsRightComponent,
                        children:[
                            { path:'',component:DateSalesReportsComponent}
                        ]
                    },
                    {
                        path:'goodssales',
                        component:GoodsSalesReportsRightComponent,
                        children:[
                            { path:'',component:GoodsSalesReportsComponent },
                        ]
                    },
                    {
                        path:'clientsales',
                        component:ClientSalesReportsRightComponent,
                        children:[
                            { path:'',component:ClientSalesReportsComponent }
                        ]
                    },
                ]
            },
        ]
    },
];

export const salesRouting:ModuleWithProviders = RouterModule.forChild(salesRoutes);
