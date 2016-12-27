import { CommonModule } from '@angular/common';
import { NgModule }      from '@angular/core';
import { FormsModule }   from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule } from '@angular/router';

import { ErpHomeComponent } from './erp.component';
import { ErpRoutes } from './erp.routing';
 
@NgModule({
  imports: [
    CommonModule,
    HttpModule,
    FormsModule,
    RouterModule.forChild(ErpRoutes)
  ],

  declarations: [
    ErpHomeComponent,
  ],

  providers: [
  ],
})
export default class ErpModule { }
