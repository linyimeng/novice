import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { routing } from './app.routing';

import { AppComponent }        from './app.component';
import { NavComponent } from './app.nav.component';

import { LoginComponent } from './modules/auth/login.component';
import { PersonnelModule } from './modules/personnel/personnel.module';
import { PurchasesModule } from './modules/purchases/purchases.module';

@NgModule({
  imports: [
    BrowserModule,
    FormsModule,
    PersonnelModule,
    PurchasesModule,
    routing
  ],

  declarations: [
    AppComponent,
    LoginComponent,
    NavComponent,
  ],

  providers: [
  ],

  bootstrap: [ 
    AppComponent
  ]
})
export class AppModule { }
