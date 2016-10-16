import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { routing } from './app.routing';

import { AppComponent }        from './app.component';
import { NavComponent } from './app.nav.component';

import { PersonnelModule } from './modules/personnel/personnel.module';

@NgModule({
  imports: [
    BrowserModule,
    FormsModule,
    PersonnelModule,
    routing
  ],

  declarations: [
    AppComponent,
    NavComponent,
  ],

  providers: [
  ],

  bootstrap: [ 
    AppComponent
  ]
})
export class AppModule { }
