import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { DepartmenttitleComponent } from './departmenttitle/departmenttitle.component';
import { DepartmentcontentComponent } from './departmentcontent/departmentcontent.component';
import { DepartmentComponent } from './department.component';
import { StafftitleComponent } from './stafftitle/stafftitle.component';
import { StaffcontentComponent } from './staffcontent/staffcontent.component';
import { StaffComponent } from './staff.component';
import { StafflistComponent } from './stafflist/stafflist.component';
import { StaffcreatComponent } from './staffcreat/staffcreat.component';
import { StaffdetailComponent } from './staffdetail/staffdetail.component';


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
        StafftitleComponent,
        StaffcontentComponent,
        StaffComponent,
        DepartmentComponent,
        StaffdetailComponent,
        StaffcreatComponent
    ],
    exports:[
        StaffComponent,
        DepartmentComponent
    ],
    providers:[]
})

export class PersonnelModule {}

