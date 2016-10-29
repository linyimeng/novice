import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PersonnelComponent } from './personnel.component';

import { DepartmentrightComponent } from './department-right/department-right.component';
import { DepartmentCreateComponent } from './departmentcreate/create.component';
import { DepartmentcontentComponent } from './departmentcontent/departmentcontent.component';
import { DepartmentDetailComponent } from './departmentdetail/departmentdetail.component';

import { StaffrightComponent } from './staff-right/staff-right.component';
import { StaffcreatComponent } from './staffcreat/staffcreat.component';
import { StaffcontentComponent } from './staffcontent/staffcontent.component';
import { StaffdetailComponent } from './staffdetail/staffdetail.component';

const personnelRoutes:Routes = [
    // 当URL为 example.com/personnel 时导航到部门
    {
        path:'personnel',
        redirectTo:'/personnel/department',
        pathMatch:'full',
    },
    {
        path:'personnel',
        component:PersonnelComponent,
        children:[
            { 
                path:'department', 
                component:DepartmentrightComponent,
                children:[
                    { path:'',component:DepartmentcontentComponent},
                    { path:'list',component:DepartmentcontentComponent},
                    { path:'create',component:DepartmentCreateComponent},
                    { path:':pk',component:DepartmentDetailComponent },
                ] 
            },
            {
                path:'staff',
                component:StaffrightComponent,
                children:[
                    { path:'', component:StaffcontentComponent },
                    { path:"create", component:StaffcreatComponent },
                    { path:'list', component:StaffcontentComponent },
                    { path:':pk',component:StaffdetailComponent },
                ]
            },
        ]
    },
];

export const personnelRouting:ModuleWithProviders = RouterModule.forChild(personnelRoutes);
