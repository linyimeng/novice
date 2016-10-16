import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { StafflistComponent } from './stafflist/stafflist.component';
import { DepartmenttitleComponent } from './departmenttitle/departmenttitle.component';
import { DepartmentcontentComponent } from './departmentcontent/departmentcontent.component';
import { StafftitleComponent } from './stafftitle/stafftitle.component';
import { StaffcontentComponent } from './staffcontent/staffcontent.component';
import { StaffComponent } from './staff.component';
import { DepartmentComponent } from './department.component';

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
        DepartmentComponent
    ],
    exports:[
        StaffComponent,
        DepartmentComponent
    ],
    providers:[]
})

export class PersonnelModule {}

