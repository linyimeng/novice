"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var core_1 = require('@angular/core');
var platform_browser_1 = require('@angular/platform-browser');
var forms_1 = require('@angular/forms');
var app_routing_1 = require('./app.routing');
var app_component_1 = require('./app.component');
var stafflist_component_1 = require('./component/personnel/stafflist/stafflist.component');
var staff_component_1 = require('./component/personnel/staff.component');
var departmenttitle_component_1 = require('./component/personnel/departmenttitle/departmenttitle.component');
var stafftitle_component_1 = require('./component/personnel/stafftitle/stafftitle.component');
var departmentcontent_component_1 = require('./component/personnel/departmentcontent/departmentcontent.component');
var department_component_1 = require('./component/personnel/department.component');
var staffcontent_component_1 = require('./component/personnel/staffcontent/staffcontent.component');
var app_nav_component_1 = require('./app.nav.component');
var AppModule = (function () {
    function AppModule() {
    }
    AppModule = __decorate([
        core_1.NgModule({
            imports: [
                platform_browser_1.BrowserModule,
                forms_1.FormsModule,
                app_routing_1.routing
            ],
            declarations: [
                app_component_1.AppComponent,
                app_nav_component_1.NavComponent,
                stafflist_component_1.StafflistComponent,
                departmenttitle_component_1.DepartmenttitleComponent,
                departmentcontent_component_1.DepartmentcontentComponent,
                stafftitle_component_1.StafftitleComponent,
                staffcontent_component_1.StaffcontentComponent,
                department_component_1.DepartmentComponent,
                staff_component_1.StaffComponent,
            ],
            providers: [],
            bootstrap: [
                app_component_1.AppComponent
            ]
        }), 
        __metadata('design:paramtypes', [])
    ], AppModule);
    return AppModule;
}());
exports.AppModule = AppModule;
//# sourceMappingURL=app.module.js.map