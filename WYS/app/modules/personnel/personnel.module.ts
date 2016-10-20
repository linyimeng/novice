import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PersonnelComponent } from './personnel.component';

import { DepartmentrightComponent } from './department-right/department-right.component';
import { DepartmentcontentComponent } from './departmentcontent/departmentcontent.component';


import { StaffcreatComponent } from './staffcreat/staffcreat.component';
import { StaffdetailComponent } from './staffdetail/staffdetail.component';
import { StaffrightComponent } from './staff-right/staff-right.component';
import { StaffcontentComponent } from './staffcontent/staffcontent.component';

//模块路由
import { personnelRouting } from './personnel.routing';

@NgModule({
    imports:[
        CommonModule,
        personnelRouting,
    ],
    declarations:[
        PersonnelComponent,

        DepartmentrightComponent,
        DepartmentcontentComponent,
        
        StaffcontentComponent,
        StaffcreatComponent,
        StaffdetailComponent,
        StaffcreatComponent,
        StaffrightComponent,
    ],
    exports:[
    ],
    providers:[
        
    ]
})

export class PersonnelModule {}

