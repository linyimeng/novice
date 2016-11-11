import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { HttpModule } from '@angular/http';
import { routing } from './app.routing';

import { AppComponent }        from './app.component';

import { PersonnelModule } from './modules/personnel/module';
import { PurchasesModule } from './modules/purchases/module';
import { SalesModule } from './modules/sales/module';
import { PosModule } from './modules/pos/module';
import { WarehouseModule } from './modules/warehouse/warehouse.module';
import { SettingModule } from './modules/setting/setting.module';


import { LoginComponent } from './modules/auth/login.component';
import { AuthService } from './modules/wysservices/auth.service';
import { StaffService } from './modules/wysservices/staff.service';

@NgModule({
  imports: [
    BrowserModule,
    HttpModule,
    FormsModule,
    PersonnelModule,
    SalesModule,
    PurchasesModule,
    PosModule,
    WarehouseModule,
    SettingModule,
    routing
  ],

  declarations: [
    AppComponent,
    LoginComponent
  ],

  providers: [
    StaffService,
    AuthService,
  ],

  bootstrap: [ 
    AppComponent
  ]
})
export class AppModule { }
