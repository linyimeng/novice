import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { StaffHomeComponent } from './staff.component';

import { DepartmentComponent } from './department/department';
import { DepartmentListComponent } from './department/list/component';
import { DepartmentCreateComponent } from './department/create/component';
import { DepartmentDetailComponent } from './department/detail/component';

import { StaffComponent } from './staff/staff';
import { StaffCreatComponent } from './staff/create/component';
import { StaffDetailComponent } from './staff/detail/component';
import { StaffListComponent } from './staff/list/component';

const staffRoutes:Routes = [
    // 当URL为 example.com/staff 时导航到部门
    {
        path:'',
        redirectTo:'/staff/department/list',
        pathMatch:'full',
    },
    { path:'',component:StaffHomeComponent },
    {
        path:'',
        component:StaffHomeComponent,
        children:[
            { 
                path:'department', 
                component:DepartmentComponent,
                children:[
                    { path:'',component:DepartmentListComponent},
                    { path:'list',component:DepartmentListComponent},
                    { path:'create',component:DepartmentCreateComponent},
                    { path:':pk',component:DepartmentDetailComponent },
                ]
            },
            {
                path:'staff',
                component:StaffComponent,
                children:[
                    { path:'', component:StaffListComponent },
                    { path:"create", component:StaffCreatComponent },
                    { path:'list', component:StaffListComponent },
                    { path:':pk',component:StaffDetailComponent },
                ]
            },
        ]
    },
];

export const staffRouting:ModuleWithProviders = RouterModule.forChild(staffRoutes);
