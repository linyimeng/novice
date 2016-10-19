import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { DepartmenttitleComponent } from './departmenttitle/departmenttitle.component';
import { DepartmentcontentComponent } from './departmentcontent/departmentcontent.component';
import { DepartmentComponent } from './department.component';
import { StaffComponent } from './staff.component';
import { StafflistComponent } from './stafflist/stafflist.component';
import { StaffcreatComponent } from './staffcreat/staffcreat.component';
import { StaffdetailComponent } from './staffdetail/staffdetail.component';
import { StaffrightComponent } from './staff-right/staff-right.component';
import { StaffcontentComponent } from './staffcontent/staffcontent.component';

import { AuthTokenGuard } from '../auth/authtoken.guard';
import { PersonnelRouting } from './personnel.routing';
@NgModule({
    imports:[
        CommonModule,
        PersonnelRouting,
    ],
    declarations:[
        StafflistComponent,
        DepartmenttitleComponent,
        DepartmentcontentComponent,
        DepartmentComponent,
        StaffComponent,
        StaffcontentComponent,
        StaffcreatComponent,
        StaffdetailComponent,
        StaffcreatComponent,
        StaffrightComponent,
    ],
    exports:[
        StaffComponent,
        DepartmentComponent
    ],
    providers:[
        AuthTokenGuard,
    ]
})

export class PersonnelModule {}

