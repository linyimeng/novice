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
var common_1 = require('@angular/common');
var stafflist_component_1 = require('./stafflist/stafflist.component');
var departmenttitle_component_1 = require('./departmenttitle/departmenttitle.component');
var departmentcontent_component_1 = require('./departmentcontent/departmentcontent.component');
var stafftitle_component_1 = require('./stafftitle/stafftitle.component');
var staffcontent_component_1 = require('./staffcontent/staffcontent.component');
var staff_component_1 = require('./staff.component');
var department_component_1 = require('./department.component');
var personnel_routing_1 = require('./personnel.routing');
var PersonnelModule = (function () {
    function PersonnelModule() {
    }
    PersonnelModule = __decorate([
        core_1.NgModule({
            imports: [
                common_1.CommonModule,
                personnel_routing_1.PersonnelRouting,
            ],
            declarations: [
                stafflist_component_1.StafflistComponent,
                departmenttitle_component_1.DepartmenttitleComponent,
                departmentcontent_component_1.DepartmentcontentComponent,
                stafftitle_component_1.StafftitleComponent,
                staffcontent_component_1.StaffcontentComponent,
                staff_component_1.StaffComponent,
                department_component_1.DepartmentComponent
            ],
            exports: [
                staff_component_1.StaffComponent,
                department_component_1.DepartmentComponent
            ],
            providers: []
        }), 
        __metadata('design:paramtypes', [])
    ], PersonnelModule);
    return PersonnelModule;
}());
exports.PersonnelModule = PersonnelModule;
//# sourceMappingURL=personnel.module.js.map