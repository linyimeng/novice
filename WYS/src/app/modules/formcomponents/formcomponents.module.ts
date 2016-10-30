import { NgModule }      from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpModule } from '@angular/http';
import { FormsModule }   from '@angular/forms';

import { DepartmentSelectComponent } from './department-select.component';
@NgModule({
  imports: [
      CommonModule,
      FormsModule,
  ],

  declarations: [
    DepartmentSelectComponent,
  ],

  providers: [
  ],
})
export class WYSFormComponentsModule { }