import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule }   from '@angular/forms';

import { StaffHomeComponent } from './staff.component';

import { DepartmentComponent } from './department/department';
import { DepartmentListComponent } from './department/list/component';
import { DepartmentCreateComponent } from './department/create/component';
import { DepartmentDetailComponent } from './department/detail/component';

import { StaffComponent } from './staff/staff';
import { StaffCreatComponent } from './staff/create/component';
import { StaffDetailComponent } from './staff/detail/component';
import { StaffListComponent } from './staff/list/component';

import { DepartmentSelectComponent } from '../erpform/department-select';
import { JobsSelectComponent } from '../erpform/jobs-select';
import { SImgUploadComponent } from '../erpform/simgupload';
//模块路由
import { staffRouting } from './staff.routing';

@NgModule({
    imports:[
        CommonModule,
        FormsModule,
        staffRouting,
    ],
    declarations:[
        StaffHomeComponent,

        DepartmentComponent,
        DepartmentListComponent,
        DepartmentCreateComponent,
        DepartmentDetailComponent,

        StaffComponent,
        StaffCreatComponent,
        StaffDetailComponent,
        StaffListComponent,

        /** 表单组件依赖 */
        DepartmentSelectComponent,
        JobsSelectComponent,
        SImgUploadComponent,
    ],
})

export default class StaffModule {}

