import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule }   from '@angular/forms';

import { PersonnelComponent } from './component';

import { DepartmentComponent } from './department/department';
import { DepartmentListComponent } from './department/list/component';
import { DepartmentCreateComponent } from './department/create/component';
import { DepartmentDetailComponent } from './department/detail/component';

import { StaffComponent } from './staff/staff';
import { StaffCreatComponent } from './staff/create/component';
import { StaffDetailComponent } from './staff/detail/component';
import { StaffListComponent } from './staff/list/component';

import { DepartmentSelectComponent } from '../formcomponents/department-select';
import { JobsSelectComponent } from '../formcomponents/jobs-select';
//模块路由
import { personnelRouting } from './routing';
import { AuthTokenGuard } from '../auth/authtoken.guard';
@NgModule({
    imports:[
        CommonModule,
        FormsModule,
        personnelRouting,
    ],
    declarations:[
        PersonnelComponent,

        DepartmentComponent,
        DepartmentListComponent,
        DepartmentCreateComponent,
        DepartmentDetailComponent,
        
        StaffComponent,
        StaffCreatComponent,
        StaffDetailComponent,
        StaffListComponent,

        DepartmentSelectComponent,
        JobsSelectComponent,
    ],
    exports:[
    ],
    providers:[
        AuthTokenGuard,
    ]
})

export class PersonnelModule {}

