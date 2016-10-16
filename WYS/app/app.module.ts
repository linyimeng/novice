import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';

import { routing } from './app.routing';

import { AppComponent }        from './app.component';
import { StafflistComponent } from './component/personnel/stafflist/stafflist.component';
import { StaffComponent } from './component/personnel/staff.component';

import { DepartmenttitleComponent } from './component/personnel/departmenttitle/departmenttitle.component';
import { StafftitleComponent } from './component/personnel/stafftitle/stafftitle.component';

import { DepartmentcontentComponent } from './component/personnel/departmentcontent/departmentcontent.component';
import { DepartmentComponent } from './component/personnel/department.component';
import { StaffcontentComponent } from './component/personnel/staffcontent/staffcontent.component';

import { NavComponent } from './app.nav.component';

@NgModule({
  imports: [
    BrowserModule,
    FormsModule,
    routing
  ],

  declarations: [
    AppComponent,
    NavComponent,
    StafflistComponent,
    DepartmenttitleComponent,
    DepartmentcontentComponent,
    StafftitleComponent,
    StaffcontentComponent,
    DepartmentComponent,
    StaffComponent,
  ],

  providers: [
   
  ],

  bootstrap: [ 
    AppComponent 
  ]
})
export class AppModule { }
