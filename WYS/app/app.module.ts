import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { routing } from './app.routing';

import { AppComponent }        from './app.component';

import { PersonnelModule } from './modules/personnel/personnel.module';
import { PurchasesModule } from './modules/purchases/purchases.module';
import { SalesModule } from './modules/Sales/sales.module';

@NgModule({
  imports: [
    BrowserModule,
    FormsModule,
    PersonnelModule,
    PurchasesModule,
    SalesModule,
    routing
  ],

  declarations: [
    AppComponent,
  ],

  providers: [
  ],

  bootstrap: [ 
    AppComponent
  ]
})
export class AppModule { }
