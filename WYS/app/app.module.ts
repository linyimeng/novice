import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule } from '@angular/http';
import { routing } from './app.routing';

import { AppComponent }        from './app.component';

import { PersonnelModule } from './modules/personnel/personnel.module';
import { PurchasesModule } from './modules/purchases/purchases.module';
import { SalesModule } from './modules/Sales/sales.module';
import { WarehouseModule } from './modules/warehouse/warehouse.module';
import { SettingModule } from './modules/setting/setting.module';

import { LoginComponent } from './modules/auth/login.component';
@NgModule({
  imports: [
    BrowserModule,
    HttpModule,
    PersonnelModule,
    PurchasesModule,
    SalesModule,
    WarehouseModule,
    SettingModule,
    routing
  ],

  declarations: [
    AppComponent,
    LoginComponent
  ],

  providers: [
  ],

  bootstrap: [ 
    AppComponent
  ]
})
export class AppModule { }
