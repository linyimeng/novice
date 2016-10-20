import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PersonnelComponent } from './personnel.component';

import { DepartmentrightComponent } from './department-right/department-right.component';

import { StaffrightComponent } from './staff-right/staff-right.component';
import { StaffcreatComponent } from './staffcreat/staffcreat.component';
import { StaffcontentComponent } from './staffcontent/staffcontent.component';
import { StaffdetailComponent } from './staffdetail/staffdetail.component';

const personnelRoutes:Routes = [
    // '' 当路径为空时导航到首页，首页为部门
    {
        path:'',
        redirectTo:'/personnel/department',
        pathMatch:'full'
    },
    // 当URL为 example.com/personnel 时导航到部门
    {
        path:'personnel',
        redirectTo:'/personnel/department',
        pathMatch:'full',
    },
    {
        path:'personnel',
        component:PersonnelComponent
    },
    {
        path:'personnel',
        component:PersonnelComponent,
        children:[
            { path:'department', component:DepartmentrightComponent },
            {
                path:'staff',
                component:StaffrightComponent,
                children:[
                    { path:'', component:StaffcontentComponent },
                    { path:"create", component:StaffcreatComponent },
                    { path:'list', component:StaffcontentComponent },
                    { path:'detail',component:StaffdetailComponent },
                ]
            },
        ]
    },
];

export const personnelRouting:ModuleWithProviders = RouterModule.forChild(personnelRoutes);
